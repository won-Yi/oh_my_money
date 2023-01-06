from django.shortcuts import render
from .models import Ledger
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def record(request):
    if request.method == 'POST':
        print('post실행')
        user = request.user
        ledger = Ledger()
        ledger.user = user
        ledger.money = request.POST.get('money')
        ledger.memo = request.POST.get('memo','')
        ledger.save()
        
        return redirect('/')

@login_required
def update_ledge(request, ledger_id):
    ledger = Ledger.objects.get(id = ledger_id)
    if request.method == "POST":
        ledger.money = request.POST.get('update_money')
        ledger.memo = request.POST.get('update_memo')

        ledger.save()
        return redirect('/')

@login_required
def delete_ledger(request, ledger_id):
    ledger = Ledger.objects.get(id = ledger_id)
    ledger.delete()
    return redirect('/')

@login_required
def detail_ledger(request, ledger_id):
    if request.method == 'GET':
        ledger = Ledger.objects.get( id = ledger_id )
        return render(request, 'ledger/ledger_detail.html',{'detail' : ledger})