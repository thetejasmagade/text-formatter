from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removepunctuations(request):
    return render(request, 'removepunctuations.html')

def uppercase(request):
    return render(request, 'uppercase.html')

def newlineremv(request):
    return render(request, 'newlineremv.html')

def extraspaceremv(request):
    return render(request, 'extraspaceremv.html')

def lowercase(request):
    return render(request, 'lowercase.html')

def capitalizesentence(request):
    return render(request, 'capitalizesentence.html')

def numberremv(request):
    return render(request, 'numberremv.html')

def measure(request):
    return render(request, 'measure.html')

def analyze(request):
    receivedtext = request.POST.get('text', 'default')
    receivedcase = request.POST.get('case', 'default')

    if receivedcase == '1': # removepunctuations = 1
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in receivedtext:
            if char not in punctuations:
                analyzed += char
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    elif receivedcase == '2':
        analyzed = ""
        for char in receivedtext:
            analyzed += char.upper()
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)
    
    elif receivedcase == '3':
        analyzed = ""
        for char in receivedtext:
            if char != "\n" and char != "\r":
                analyzed += char
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    elif receivedcase == '4':
        analyzed = ""
        for index, char in enumerate(receivedtext):
            if not(receivedtext[index] == " " and receivedtext[index + 1] == " "):
                analyzed += char
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    elif receivedcase == '5':
        analyzed = ""
        for char in receivedtext:
            analyzed += char.lower()
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    elif  receivedcase == '6':
        import re
        analyzed = ""
        analyzed = re.sub(r'(?:^|(?<=\.))(\s*.)', lambda match: r'{}'.format(match.group(1).upper()), receivedtext)
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    elif receivedcase == '7':
        analyzed = ""
        numbers = '0123456789'
        for char in receivedtext:
            if char not in numbers:
                analyzed = analyzed + char
        count = len(analyzed)
        params = {'text':analyzed, 'count': count}
        return render(request, 'analyze.html', params)

    