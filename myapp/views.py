from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import auth

# Create your views here.
def index(request):
    posts = CustomUser.objects.all()
    context = {"posts":posts}
    return render(request,'index.html',context)

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = CustomUser.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                address = request.POST['address'],
                phone = request.POST['phone'],
                birth = request.POST['birth'],
                gender = request.POST['gender'],
                age = request.POST['age'],
            )
            return redirect('login')
        return render(request,'signup.html',{'error':'비밀번호 확인이 맞지 않습니다.'})

    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        return render(request, 'login.html',{'error':'아이디나 비밀번호가 틀립니다.'})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')