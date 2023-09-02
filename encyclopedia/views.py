from django.shortcuts import render

from django.http import HttpResponse

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# psuedocode for function below provided by cs50.ai chatbot
def newfile(request):
    if request.method == 'POST':
        title = request.POST['newfilename']
        content = "#" + request.POST['newfilename'] + "\n" + request.POST['newpage']
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/errorpageexists.html")
        else:
            util.save_entry(title, content)
        return render(request, "encyclopedia/newfile.html")
    else:
        return render(request, "encyclopedia/newfile.html")

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
        # following 4 lines made with assistance from cs50.ai chatbot
        all_entries = util.list_entries()
        matching_entries = [entry for entry in all_entries if title in entry]
        return render(request, "encyclopedia/searchlist.html", {
            "entries": matching_entries,
            "title" : title.lstrip('# ')
            })

