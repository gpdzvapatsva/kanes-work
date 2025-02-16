from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.books1, name='books1'),
    path('bookshop/', views.books, name='books'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.contact_success, name='success'),
    path('cart/', views.mycart, name='mycart'),
    path('booksposts/', views.myBooksListCreate.as_view(), name="bookposts_view_create"),
    path('booksposts/<int:pk>', views.myBooksRetrieveUpdateDestroy.as_view(), name="bookposts_view_update")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)