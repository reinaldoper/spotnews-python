from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category, User
from news.forms import CreateCategoryModelForm, CreateNewsModelForm
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


def news(request):
    form = CreateNewsModelForm()

    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    authors = User.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        'news_form.html',
        {'form': form, 'authors': authors, 'categories': categories}
    )
