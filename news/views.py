from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CreateCategoryModelForm
from django.http import Http404


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def new_details(request, id):
    try:
        new = get_object_or_404(News, id=id)
        return render(request, 'news_details.html', {'new': new})
    except Http404:
        return render(request, '404.html')


def categories(request):
    form = CreateCategoryModelForm()

    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)
