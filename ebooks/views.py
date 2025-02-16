from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods

from .models import myBooks
from .form import myBooksForm
from .form import ContactForm
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
def books1(request):
    books=myBooks.objects.all()
    context={'books':books}
    return render (request, 'books1.html', context )
def books(request):
    form =myBooksForm()
    book=myBooks.objects.all()
    context={'book':book}
    #CREATE part of CRUD
    if request.method=='POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form=myBooksForm(request.POST)
            else:
                ebooks = myBooks.objects.get(id=pk)
                form = myBooksForm(request.POST, instance=ebooks)
            form.save()
            form = myBooksForm()
        elif 'delete' in request.POST:
            pk=request.POST.get('delete')
            ebooks=myBooks.objects.get(id=pk)
            ebooks.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            ebooks = myBooks.objects.get(id=pk)
            #populating blank form with record associated with update button
            form = myBooksForm(instance=ebooks)
    context['form']=form
    return render (request, 'books.html', context )
def product_detail(request, pk):
    book1 = myBooks.objects.get(pk=pk)
    context={'book1': book1}
    return render(request, 'index2.html', context )

@require_http_methods(["GET", "POST"])
def mycart(request):
    book=myBooks.objects.all()
    context={'book':book}
    return render (request, 'cart.html', context )

def contact_view(request):
    if request.method=='POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return  redirect('contact-success')
    else:
        form=ContactForm()
    context={'form':form}
    return render (request, 'contact.html', context)
#I have added a formspree endpoint for success message
def contact_success(request):
    return  render(request, 'success.html')
