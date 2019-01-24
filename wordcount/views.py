from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for ddd in words:
        if ddd in word_dictionary:
            #increase
            word_dictionary[ddd]+=1
        else:
            # add to dictionary
            word_dictionary[ddd]=1
    
    return render(request, 'result.html', {'full': text, 'length': len(words), 'list': word_dictionary.items()})