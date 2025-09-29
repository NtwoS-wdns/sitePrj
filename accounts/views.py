from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def fmap(request):
    return render(request, "fmap.html")
def map(request):
    return render(request, "map.html")
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # важно: берём данные формы
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            # логиним через стандартный backend
            user = authenticate(username=username, password=raw_password)
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile(request):
    return render(request, "profile.html")

def home(request):
    slides = [
        {
            "name": "Барсик",
            "sex": "М",
            "desc": "Я тут ничего не придумал, увы",
            "image": "https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/475B/production/_98776281_gettyimages-521697453.jpg.webp"
        },
        {
            "name": "Рекс",
            "sex": "М",
            "desc": "Чумоваая псина.",
            "image": "https://placedog.net/400/500"
        },
        {
            "name": "Шмель",
            "sex": "Ж",
            "desc": "Игривый характер, обожает бегать и охотиться на шмелей.",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQPBS1zjNqvM-5-gcjQOsLKBEL8ljzl-5_Ddu-0MqWSjelvY1TR0JVZXnPtYwDWy7Ak5w&usqp=CAU"
        }
    ]
    return render(request, "home.html", {"slides": slides})