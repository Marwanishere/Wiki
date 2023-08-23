from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request):
    return render (request, "encyclopedia/get.html", {
        "get": util.get_entry(title)
    })