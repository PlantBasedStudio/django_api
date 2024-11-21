from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductsForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Products
from .serializers import ProductsSerializer


# Response sert a retourner des réponses comme la librairie python Request.render pour afficher tout en JSON. 
# Le decorator c'est pour afficher la vue API

@api_view(['GET'])
def getData(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def addProduct(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products') 
    else:
        form = ProductsForm()
    return render(request, 'add_product.html', {'form': form})

def index(request):
    return render(request, 'index.html')