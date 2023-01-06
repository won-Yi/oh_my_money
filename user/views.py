from django.shortcuts import render, redirect
# from .models import UserModel, FollowModel
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# model
from .models import User
from ledger.models import Ledger


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            print('get실행')
            all_outlay = Ledger.objects.all().order_by('-created_at')
            print(all_outlay)
            return render(request, 'index.html',{'outlay_lists':all_outlay})
    
        else:
            return render(request, 'user/login.html')
    

# 회원가입 페이지
def join(request):
    if request.method == 'GET':
        return render(request, 'user/join.html')
    elif request.method == 'POST':
        # 포스트 요청 처리
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            exist_user = get_user_model().objects.filter(email = email)
            if exist_user :
                return render(request, 'user/login.html')
            else:
                User.objects.create_user(username=name, password=password, email=email)
                return render(request, 'user/login.html')
        return render(request, 'user/join.html')


#로그인 
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            auth.login(request, user)  
            return redirect('/')
        else:
            return redirect('/join/')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login/')