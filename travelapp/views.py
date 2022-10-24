
from django.shortcuts import render

from travelapp.models import place, review

def index(request):

   obj=place.objects.all()
   obj2=review.objects.all()
   return render(request,'index.html',{'res':obj,'rev':obj2})
# Create your views here.
