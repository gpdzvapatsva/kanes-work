from django import  forms
from .models import myBooks

class myBooksForm(forms.ModelForm):
    class Meta:
        model=myBooks
        fields = '__all__'