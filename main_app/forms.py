from django import forms
from .models import Budget_Item

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget_Item
        fields = ['name', 'expend_category', 'amount', 'entry_month', 'entry_day', 'entry_year', 'description']



#class BudgetForm(forms.Form):

    #name = forms.CharField(label='Name', max_length=100)
    #amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    #entry_month = forms.IntegerField(label='Entry Month')
    #entry_day = forms.IntegerField(label='Entry Day')
    #entry_year = forms.IntegerField(label='Entry Year')
    #entry_date = forms.DateField(label='Date')
    #description = forms.CharField(label='Description', max_length=100)