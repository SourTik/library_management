from django.urls import path
from . import views


urlpatterns = [
    # Home Url
    path('', views.home, name="home"),
    path('search/', views.search, name='search'),

    # Author URLs
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', views.AuthorCreateView.as_view(), name="author_create"),
    path('authors/update/<int:pk>', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/delete/<int:pk>', views.AuthorDeleteView.as_view(), name='author_delete'),

    # Shelf URLs
    path('shelves/', views.ShelfListView.as_view(), name='shelf_list'),
    path('shelves/<int:pk>/', views.ShelfDetailView.as_view(), name='shelf_detail'),
    path('shelves/create/', views.ShelfCreateView.as_view(), name='shelf_create'),
    path('shelves/update/<int:pk>', views.ShelfUpdateView.as_view(), name='shelf_update'),
    path('shelves/delete/<int:pk>', views.ShelfDeleteView.as_view(), name='shelf_delete'),

    # Book URLs
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(), name= 'book_update'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name= 'book_delete'),

    # Member URls
    path('members/', views.MemberListViews.as_view(), name='member_list'),
    path('member/<int:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
    path('member/create/', views.MemberCreateView.as_view(), name='member_create'),
    path('member/update/<int:pk>', views.MemberUpdateView.as_view(), name='member_update'),
    path('member/delete/<int:pk>', views.MemberDeleteView.as_view(), name='member_delete'),

    # Loan URLs
    path('loans/', views.LoanListView.as_view(), name='loan_list'),
    path('loan/<int:pk>/', views.LoanDetailView.as_view(), name='loan_detail'),
    path('loan/create/', views.LoanCreateView.as_view(), name='loan_create'),
    path('loan/update/<int:pk>', views.LoanUpdateView.as_view(), name='loan_update'),
    path('loan/delete/<int:pk>', views.LoanDeleteView.as_view(), name='loan_delete'),

    # Staff Signup ,Login, Logout

    path('signup/', views.StaffSignupView.as_view(), name='signup'),
    path('login/', views.StaffLoginView.as_view(), name='login'),
    path('logout/', views.StaffLogoutView.as_view(), name='logout')
]