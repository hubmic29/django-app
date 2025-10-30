from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, AdForm
from django.contrib import messages
from .models import Ad
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def home(request):
    ads = Ad.objects.order_by("-created_at")
    return render(request, "core/home.html", {'ads': ads})


@login_required
def add_offer(request):
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            if request.user.is_authenticated:
                ad.owner = request.user  # zalogowany → przypisz właściciela
            # niezalogowany → owner zostaje None
            ad.save()
            messages.success(request, "Ogłoszenie opublikowane!")
            return redirect("home")  # po publikacji wróć na stronę główną
    else:
        form = AdForm()
    return render(request, "core/add_offer.html", {"form": form})
