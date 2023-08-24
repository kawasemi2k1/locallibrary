from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('book/<int:primary_key>', views.book_detail_view, name='book-detail'),
    path('book/all-borrowed/', views.AllBorrowedBooksListView.as_view(), name='all-borrowed'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('author/<int:primary_key>', views.author_detail_view, name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
