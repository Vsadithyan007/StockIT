from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    workers=User.objects.all()
    wc= workers.count()
    pc=products.count()
    oc=orders.count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'wc':wc,
        'pc':pc,
        'oc':oc
    }
    return render(request,'dashboard/index.html',context)


@login_required
def staff(request):
    workers=User.objects.all()
    wc= workers.count()
    context={
        'workers':workers,
        'wc':wc
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers=User.objects.get(id=pk)
    context={
        'workers':workers
    }
    return render(request,'dashboard/staff_details.html',context)


@login_required
def product(request):
    items = Product.objects.all()
    pc=items.count()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('Name')
            messages.success(request,f'{product_name} has been inserted')
            return redirect('d-product')
    else:
        form=ProductForm()
        
    context={
        'items':items,
        'form':form,
        'pc':pc
    }
    return render(request,'dashboard/product.html',context)

@login_required
def product_delete(request,pk):
    obj=Product.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return product(request)
    return render(request,'dashboard/product_delete.html')

@login_required
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return product(request)
    else:
        form=ProductForm(instance=item)
        
    context={
        'form':form
    }
    return render(request,'dashboard/product_update.html',context)




@login_required
def order(request):
    orders=Order.objects.all()
    oc=orders.count()
    context={
        'orders':orders,
        'oc':oc
    }
    return render(request,'dashboard/order.html',context)





