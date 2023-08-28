from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get(request):
    title = request.POST['title']
    # following seven lines that allow for a title to be dictated 
    # were made with the assitance of cs50.ai chatbot
    # I also learned how to use visual studio's python debugger
    # in the process
    markdown_text = util.get_entry(title)
    if markdown_text != None:
        lines = markdown_text.split('\n')
        title = title.lstrip('# ')
        title = lines[0] if lines else None
        markdown_text = markdown_text.lstrip(title)
    else :
        title = None
    return render (request, "encyclopedia/get.html", {
        "title": title,
        "get": markdown_text
    })