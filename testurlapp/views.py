from django.shortcuts import render, get_object_or_404
from firstapp.models import Pizza, PizzaShop
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt, csrf_protect  # Add this
# Create your views here.
from firstapp.form import OrderForm

# add this snippet in your view section
from django.core.exceptions import ValidationError


@csrf_exempt
def home(request, pizza_id):
    print(pizza_id)
    print('----------------------', request.method)
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(request.POST or None, initial={
        'pizza': pizza
    })
    #print(form)
    if request.method == 'POST':
        print(request.body)
        #json_string = json.dumps(datastore)

        dic = json.loads(request.body)
        foo_instance = PizzaShop(**dic)
        try:
            foo_instance.full_clean(exclude=None)            
        except ValidationError as e:
            return HttpResponse(e)

    # Do something based on the errors contained in e.message_dict.
    # Display them to a user, or handle them programmatically.
        
        foo_instance.save()
        return HttpResponse(foo_instance)
