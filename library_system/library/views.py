from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AuthorForm, BookForm, ShelfForm, MemberForm, LoanForm
from collections import defaultdict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from . import models

@login_required
def home(request):
    authors = models.Author.objects.all()
    shelves = models.Shelf.objects.all()
    books = models.Book.objects.all()
    members = models.Member.objects.all()
    loans = models.Loan.objects.all()
    context = {
        'authors': authors,
        'shelves': shelves,
        'books': books,
        'members': members,
        'loans': loans,
    }
    return render(request, 'library/home.html', context)

def search(request):
    query = request.GET.get('q', '')
    authors = models.Author.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query)
    )
    books = models.Book.objects.filter(
        Q(title__icontains=query) | Q(isbn__icontains=query)
    )
    members = models.Member.objects.filter(
        Q(full_name__icontains=query) | Q(library_card_number__icontains=query)
    )
    shelves = models.Shelf.objects.filter(
        Q(name__icontains=query)
    )
    loans = models.Loan.objects.filter(
        Q(book__title__icontains=query) |
        Q(member__full_name__icontains=query) |
        Q(book__isbn__icontains=query)
    )
    context = {
        'query': query,
        'authors': authors,
        'books': books,
        'members': members,
        'shelves': shelves,
        'loans': loans,
    }
    return render(request, 'library/search_results.html', context)

# Views of Author

class AuthorListView(LoginRequiredMixin, ListView):
    model = models.Author
    template_name = 'library/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = models.Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'
    pk_url_kwarg = 'pk'

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = models.Author
    form_class = AuthorForm
    template_name = 'library/author_create.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Author
    form_class = AuthorForm
    template_name = 'library/author_update.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Author
    template_name = 'library/author_delete.html'
    success_url = reverse_lazy('author_list')

# Views of Sheleves

class ShelfListView(LoginRequiredMixin, ListView):
    model = models.Shelf
    template_name = 'library/shelf_list.html'
    context_object_name = 'shelves'

class ShelfDetailView(LoginRequiredMixin, DetailView):
    model = models.Shelf
    template_name = 'library/shelf_detail.html'
    success_url = reverse_lazy('shelf_list')
    context_object_name = 'shelf'
    pk_url_kwarg = 'pk'

class ShelfCreateView(LoginRequiredMixin, CreateView):
    model = models.Shelf
    form_class = ShelfForm
    template_name = 'library/shelf_create.html'
    success_url = reverse_lazy('shelf_list')

class ShelfUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Shelf
    form_class = ShelfForm
    template_name = 'library/shelf_update.html'
    success_url = reverse_lazy('shelf_list')

class ShelfDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Shelf
    template_name = 'library/shelf_delete.html'
    success_url = reverse_lazy('shelf_list')

# Views of Books

class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = context['books']
        books_by_shelf = defaultdict(list)
        for book in books:
            books_by_shelf[book.shelf].append(book)
        context['books_by_shelf'] = books_by_shelf.items()  # .items() for template unpacking
        return context

class BookDetailView(LoginRequiredMixin, DetailView):
    model = models.Book
    template_name = 'library/book_detail.html'
    success_url = reverse_lazy('book_list')
    pk_url_kwarg = 'pk'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    template_name = 'library/book_create.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    template_name = 'library/book_update.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    template_name = 'library/book_delete.html'
    success_url = reverse_lazy('book_list')

# Member Views

class MemberListViews(ListView):
    model = models.Member
    template_name = 'library/member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = models.Member
    template_name = 'library/member_detail.html'
    success_url = reverse_lazy('book_list')
    pk_url_kwarg = 'pk'

class MemberCreateView(CreateView):
    model = models.Member
    template_name = 'library/member_create.html'
    form_class = MemberForm
    success_url = reverse_lazy('book_list')

class MemberUpdateView(UpdateView):
    model = models.Member
    template_name = 'library/member_update.html'
    form_class = MemberForm
    success_url = reverse_lazy('book_list')

class MemberDeleteView(DeleteView):
    model = models.Member
    template_name = 'library/member_delete.html'
    success_url = reverse_lazy('book_list')

# Loan Views

class LoanListView(ListView):
    model = models.Loan
    template_name = 'library/loan_list.html'
    context_object_name = 'loans'

class LoanDetailView(DetailView):
    model = models.Loan
    template_name = 'library/loan_detail.html'
    success_url = reverse_lazy('loan_list')
    pk_url_kwarg = 'pk'

class LoanCreateView(CreateView):
    model = models.Loan
    template_name = 'library/loan_create.html'
    form_class = LoanForm
    success_url = reverse_lazy('loan_list')

class LoanUpdateView(UpdateView):
    model = models.Loan
    template_name = 'library/loan_update.html'
    form_class = LoanForm
    success_url = reverse_lazy('loan_list')

    def form_valid(self, form):
        loan = form.save(commit=False)
        if 'return_book' in self.request.POST:
            loan.return_date = timezone.now()
        loan.save()
        return super().form_valid(form)

class LoanDeleteView(DeleteView):
    model = models.Loan
    template_name = 'library/loan_delete.html'
    success_url = reverse_lazy('loan_list')
    
# User Views for Signup, Login, Logout

class StaffSignupView(FormView):
    template_name = 'library/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        user.save()
        login(self.request, user)
        return super().form_valid(form)
    

class StaffLoginView(LoginView):
    template_name = 'library/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class StaffLogoutView(TemplateView):
    template_name = 'library/logout.html'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')