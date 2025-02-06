from rest_framework import serializers
from .models import myBooks
class myBooksSerializers(serializers.ModelSerializer):
     class Meta:
         model=myBooks
         fields=['id','title', 'author','genre', 'price', 'stock']