from django.shortcuts import render
from .models import Budget_Item
# Create your views here.
def index(request):
    budget_items = Budget_Item.objects.all()
    return render(request, 'index.html', {'budget_items':budget_items})

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