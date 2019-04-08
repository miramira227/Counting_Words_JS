from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    oldtextlist = text.split(' ')
    wordcount = len(oldtextlist)

    textsetlist = list(set(oldtextlist))
    textdic = {}
    for i in textsetlist:
        textdic[i] = 0
    for i in oldtextlist:
        textdic[i] += 1

    return render(request, 'result.html', {
        'wordcount': wordcount,
        'text': text, 
        'textdic': textdic.items(),
    })
