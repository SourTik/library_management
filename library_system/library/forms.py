from dataclasses import fields
from . import models
from django.forms import ModelForm

# Author Form
class AuthorForm(ModelForm):
    class Meta:
        model = models.Author
        fields = ['first_name', 'last_name', 'biography']

# Shelf Form

class ShelfForm(ModelForm):
    class Meta:
        model = models.Shelf
        fields = ['name', 'description']


# Book Form
class BookForm(ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'authors', 'isbn', 'shelf', 'description', 'total_copies', 'available_copies', 'image']

# Member Form
class MemberForm(ModelForm):
    class Meta:
        model = models.Member
        fields = ['full_name', 'join_date']
        exclude = ['library_card_number']

# Loan Form

class LoanForm(ModelForm):

    class Meta:
        model = models.Loan
        fields = ['member', 'book', 'due_date', 'return_date', 'late_fee_per_day']