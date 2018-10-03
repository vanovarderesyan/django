from django.shortcuts import render,get_object_or_404
from firstapp.models import Pizza
# Create your views here.
from firstapp.form import OrderForm
def home(request,pizza_id):
    print(pizza_id)
    pizza = get_object_or_404(Pizza,id=pizza_id)
    form = OrderForm(initial={
        'pizza':pizza
    })
    return render(request,'home.html',{
        'form':form,
        'pizza':pizza
    })
