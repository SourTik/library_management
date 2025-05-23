from django.db import models
from django.utils import timezone
from decimal import Decimal
import uuid
from datetime import timedelta
import math

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Shelf(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, null=True, related_name='books')
    description = models.TextField(blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    library_card_number = models.CharField(max_length=20, unique=True, blank=True)
    join_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.library_card_number:
            while True:
                number = str(uuid.uuid4().int)[:20]
                if not Member.objects.filter(library_card_number=number).exists():
                    self.library_card_number = number
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name or self.library_card_number


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='loans')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    late_fee_per_day = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.50'))


    class Meta:
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.full_name}"

    @property
    def is_overdue(self):
        if not self.due_date:
            return False  # or handle as you wish
        if self.return_date:
            return self.return_date > self.due_date
        return timezone.now() > self.due_date

    @property
    def late_fee(self):
        """
        Calculate total late fee based on days overdue.
        """
        if not self.due_date:
            return 0  # No due date, no late fee
        end = self.return_date or timezone.now()
        if end <= self.due_date:
            return 0
        overdue_seconds = (end - self.due_date).total_seconds()
        days_overdue = math.ceil(overdue_seconds / 86400)
        return days_overdue * self.late_fee_per_day

    def save(self, *args, **kwargs):
        # Auto-set due_date if not provided
        if not self.due_date:
            self.due_date = self.borrow_date + timedelta(days=14)

        # adjust available copies on borrow and return
        if not self.pk:
            # new loan
            self.book.available_copies = models.F('available_copies') - 1
            self.book.save()
        elif self.return_date and not Loan.objects.get(pk=self.pk).return_date:
            # book being returned
            self.book.available_copies = models.F('available_copies') + 1
            self.book.save()
        super().save(*args, **kwargs)
