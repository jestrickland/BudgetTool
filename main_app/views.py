from django.shortcuts import render
from .models import Budget_Item
# Create your views here.
def index(request):
    budget_items = Budget_Item.objects.all()
    return render(request, 'index.html', {'budget_items':budget_items})

def detail(request, Budget_Item_id):
    budget_item = Budget_Item.objects.get(id=Budget_Item_id)
    return render(request, 'detail.html', {'budget_item':budget_item})

#class Budget_Item:
    #def __init__(self, name, amount, date, description):
        #self.name = name
        #self.amount = amount
        #self.date = date
        #self.description = description

#budget_items = [
    #Budget_Item('Grocery', 50.76, '12/3/17', 'City Market'),
    #Budget_Item('Gas', 44.34, '12/1/17', 'Giant'),
    #Budget_Item('Fun', 50, '12/4/17', 'Walgreens')
#]