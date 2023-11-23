from django.shortcuts import render, get_object_or_404
from news.models import News
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
