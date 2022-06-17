from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

def currency(request):
    return render(request, 'currency.html')

def currency_alter(request):
    return render(request, 'currency_alter.html')

def stock_grp(request):
    return render(request, 'stock_grp.html')

def stock_items(request):
    return render(request, 'stock_items.html')

def stock_cat(request):
    return render(request, 'stock_cat.html')

def units(request):
    return render(request, 'units.html')

def godwn(request):
    return render(request, 'godwn.html')

def godwn_alter(request):
    return render(request, 'godwn_alter.html')

def emp_cat(request):
    return render(request, 'emp_cat.html')

def emp_cat_alter(request):
    return render(request, 'emp_cat_alter.html')

def emp_grp(request):
    return render(request, 'emp_grp.html')

def emp(request):
    return render(request, 'emp.html')

def atndnce_list(request):
    return render(request, 'atndnce_list.html')

def pay(request):
    return render(request, 'pay.html')












