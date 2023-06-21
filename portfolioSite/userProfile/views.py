from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import  Proposal
from django.http import Http404
from .forms import ProposalForm


def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect("portfolio:index")

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logoutt(request):
    logout(request)
    return redirect("portfolio:index")

# def profile(request):
#     return render(request, 'registration/profile.html')
#

def profile(request):
    print(request.user)
    if request.method != "POST":
        form = ProposalForm()
    else:
        form = ProposalForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.ower = request.user
            new_topic.save()
            return redirect("userProfile:profile")
    context = {"form": form}
    return  render(request, 'registration/profile.html', context)

