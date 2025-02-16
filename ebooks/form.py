from django import  forms
from .models import myBooks

class myBooksForm(forms.ModelForm):
    class Meta:
        model=myBooks
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print(f"Send message: {self.cleaned_data ['email']} with message: {self.cleaned_data ['message']}")