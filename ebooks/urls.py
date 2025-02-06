from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('booksposts/', views.myBooksListCreate.as_view(), name="bookposts_view_create"),
    path('booksposts/<int:pk>', views.myBooksRetrieveUpdateDestroy.as_view(), name="bookposts_view_update")
]