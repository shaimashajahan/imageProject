from django.shortcuts import render,redirect
import os 
from .models import Product
# Create your views here.
def index(request):
    return render(request,'add_product.html')
def add_product(request):
    if request.method == 'POST':
        pname=request.POST['p_name']
        price=request.POST['p_price']
        pqty=request.POST['p_qty']
        image=request.FILES.get('file')
        product=Product(Product_name=pname,Product_price=price,Product_qty=pqty,image=image)
        print("Save data...")
        product.save()
        return redirect("show_product")
def show_product(request):
    product=Product.objects.all()
    return render(request,'show_product.html',{'product':product})
def updatepage(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'update_product.html',{'product':product})
def update_product(request,pk):
    if request.method=='POST':
        product=Product.objects.get(id=pk)
        product.Product_name=request.POST.get('p_name')
        product.Product_price=request.POST.get('p_price')
        product.Product_qty=request.POST.get('p_qty')
        if len(request.FILES) != 0:
            if len(product.image) > 0:
                os.remove(product.image.path)
            product.image=request.FILES.get('file')
        product.save()
        return redirect('show_product')
    return render(request,'update_product.html')
def deletepage(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect('show_product')

