from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import myBooks
from .forms import myBooksForm
from rest_framework import generics
from .serialisers import myBooksSerializers


#linking the serialiser with the views
class myBooksListCreate(generics.ListCreateAPIView):
    queryset = myBooks.objects.all()
    serializer_class = myBooksSerializers

#Deleting individual blogpost
class myBooksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = myBooks.objects.all()
    serializer_class = myBooksSerializers
    lookup_field = 'pk' #deleting using the primary key


# Create your views here.
@require_http_methods(["GET", "POST"])
def books(request):
    form =myBooksForm()
    book=myBooks.objects.all()
    context={'book':book}
    context['form']=form
    return render (request, 'books.html', context )
