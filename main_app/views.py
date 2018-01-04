from django.contrib.auth.models import User
from django.db.transaction import commit
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Budget_Item
from .forms import BudgetForm
import datetime

now = datetime.datetime.now()

#Main View
def index(request):
    budget_items = Budget_Item.objects.all()
    form = BudgetForm
    return render(request, 'index.html', {'budget_items':budget_items, 'form':form})

#Current Day View
def current(request):
    budget_item_current = Budget_Item.objects.get(entry_day = now.day, entry_month = now.month, entry_year = now.year)
    return render(request, 'current.html', {'budget_item_current':budget_item_current})

#Detail View
def detail(request, Budget_Item_id):
    budget_item = Budget_Item.objects.get(id=Budget_Item_id)
    return render(request, 'detail.html', {'budget_item':budget_item})

#User Name View
def profile(request, username):
    user = User.objects.get(username=username)
    budget_item = Budget_Item.objects.filter(user=user)
    return render(request, 'profile.html',
                  {'username': username,
                  'budget_item': budget_item})

#Form Save View
def post_budgetitem(request):
    form = BudgetForm(request.POST)
    if form.is_valid():
        budget_item = form.save(commit = False)
        budget_item.user=request.user
        budget_item.save()
    return HttpResponseRedirect('/')
