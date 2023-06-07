from django.shortcuts import render

# главнная
def index(request, *args, **kwargs):
    return  render(request, "index.html", {})

# авторы
def autors(request, *args, **kwargs):
    return  render(request, "autors.html", {})

# Альбом
def album(request, *args, **kwargs):
    return  render(request, "album.html", {})

# главнная
# def index(request):
#     return render(request)