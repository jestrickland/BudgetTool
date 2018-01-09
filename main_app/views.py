from django.contrib.auth.models import User
from django.db.transaction import commit
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Budget_Item
from .forms import BudgetForm
#import datetime
from datetime import datetime, timedelta, date

#Current Date Structure
now = datetime.now()
budget_items_current = Budget_Item.objects.filter(entry_day=now.day, entry_month=now.month, entry_year=now.year)
budget_items_mtd = Budget_Item.objects.filter(entry_month=now.month, entry_year=now.year)
budget_items_ytd = Budget_Item.objects.filter(entry_year=now.year)

#Rolling Date Structure
#entry_date = date(Budget_Item.objects.get(entry_year))
#nowminus7 = now - timedelta(days=7)
#budget_items_7day = Budget_Item.objects.filter(entry_day__gte=now.day, entry_day__lte=nowminus7.day, entry_month__gte=now.month, entry_month__lte=nowminus7.month, entry_year__gte=now.year, entry_year__lte=nowminus7.year)

#Main View
def index(request):
    budget_items = Budget_Item.objects.all()
    form = BudgetForm
    return render(request, 'index.html', {'budget_items':budget_items, 'budget_items_current':budget_items_current, 'budget_items_mtd':budget_items_mtd,'budget_items_ytd':budget_items_ytd,'form':form})

#Current Day View
def current(request):
    form = BudgetForm
    return render(request, 'current.html', {'budget_items_current':budget_items_current,'form':form})

#Month to Date Day View
def monthtodate(request):
    form = BudgetForm
    return render(request, 'monthtodate.html', {'budget_items_mtd':budget_items_mtd,'form':form})

#Year to Date Day View
def yeartodate(request):
    form = BudgetForm
    return render(request, 'yeartodate.html', {'budget_items_ytd':budget_items_ytd,'form':form})

#Detail View
def detail(request, Budget_Item_id):
    form = BudgetForm
    budget_item = Budget_Item.objects.get(id=Budget_Item_id)
    return render(request, 'detail.html', {'budget_item':budget_item,'form':form})

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
