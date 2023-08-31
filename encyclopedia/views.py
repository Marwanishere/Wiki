from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request):
    title = request.POST['title']
    # following six lines that allow for a title to be dictated 
    # were made with the assitance of cs50.ai chatbot
    # I also learned how to use visual studio's python debugger
    # in the process
    markdown_text = util.get_entry(title)
    if markdown_text != None:
        lines = markdown_text.split('\n')
        title = title.lstrip('# '),
        title = lines[0] if lines else None
        markdown_text = markdown_text.lstrip(title)
        return render (request, "encyclopedia/get.html", {
            "title": title.lstrip('# '),
            "get": markdown_text
        })
    else :
        return render (request, "encyclopedia/searchlist.html", {
            "title": title
        })

def inside(request, title):
    entrieslist = util.list_entries()
    # technique in line below attained from cs50.ai chatbot
    result = [x for x in entrieslist if title in x]
    # return function assisted by cs50.ai chatbot
    return render(request, "encyclopedia/searchlist.html", {
    "result": result
})