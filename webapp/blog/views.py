from django.shortcuts import render

# Create your views here.


# handle routes

# home page
def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})
# about page
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
