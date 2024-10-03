from django.shortcuts import render, redirect

from users.models import CustomerUser
from .forms import OrderForm
from .models import Uzum


def main_page(request):
    products = Uzum.objects.all()  # SELECT * FROM Shop;
    context = {'products': products}
    return render(request, 'index.html', context)


def add_product_view(request):
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        price = form.get('price')
        count = form.get('count')
        image = request.FILES.get('image')
        product = Uzum.objects.create(name=name, price=price, count=count, image=image)
        product.save()
        return redirect('home')
    return render(request, 'add_product.html')


def order_view(request, id):
    product = Uzum.objects.get(id=id)
    form = OrderForm()
    context = {'form':form, 'product':product}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'order.html', context)





def buy_product_view(request, id):
    student = CustomerUser.objects.get(id=request.user.id)
    product = Uzum.objects.get(id=id)
    if product.count > 0:
        if student.coins >= product.price:
            student.coins -= product.price
            student.save()
            product.count -= 1
            product.save()
            return redirect('home')
        else:
            message = "Sizda koinlar yetarli emas"
            return render(request, 'index.html', {'message': message})
    else:
        message = "Maxsulot qolmagan"
        return render(request, 'index.html', {'message': message})


