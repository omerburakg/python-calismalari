from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def blog_details(request, id):
    return render(request, "blog_details.html", {
        "id":id
    })