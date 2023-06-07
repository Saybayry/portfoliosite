from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect("storeStaffForArt:startpage")

    context = {'form': form}
    return render(request, 'registration/register.html', context)
def logoutt(request):
    logout(request)
    return redirect("storeStaffForArt:startpage")

