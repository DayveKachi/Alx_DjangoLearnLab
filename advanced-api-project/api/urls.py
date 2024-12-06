#from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ListView, CreateView, DetailView, UpdateView, DeleteView

#router = DefaultRouter()

urlpatterns = [
    path("books/", ListView.as_view(), name="books_list"),
    path("books/create/", CreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", DetailView.as_view(), name="book_detail"),
    path("books/update/<int:pk>/", UpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", DeleteView.as_view(), name="book_delete"),
]

#urlpatterns += router.urls
