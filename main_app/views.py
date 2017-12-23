from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Budget_Item
from .forms import BudgetForm
# Create your views here.
def index(request):
    budget_items = Budget_Item.objects.all()
    form = BudgetForm
    return render(request, 'index.html', {'budget_items':budget_items, 'form':form})

def detail(request, Budget_Item_id):
    budget_item = Budget_Item.objects.get(id=Budget_Item_id)
    return render(request, 'detail.html', {'budget_item':budget_item})

def post_treasure(request):
    form = BudgetForm(request.POST)
    if form.is_valid():
        budget_item = Budget_Item(name = form.cleaned_data['name'],
                                  amount = form.cleaned_data['amount'],
                                  entry_month = form.cleaned_data['entry_month'],
                                  entry_day = form.cleaned_data['entry_day'],
                                  entry_year = form.cleaned_data['entry_year'],
                                  entry_date = form.cleaned_data['entry_date'],
                                  description = form.cleaned_data['description'])
        budget_item.save()
    return HttpResponseRedirect('/')

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