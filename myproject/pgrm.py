from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'bootstrap.html')
def  AboutUs(request):
    return render(request,'AboutUs.html')

def about(request):
    kk = request.POST.get('text', 'default')
    checkbox = request.POST.get('check', 'off')       # Remove digits
    checkbox2 = request.POST.get('upper', 'off')      # Convert to uppercase
    checkbox3 = request.POST.get('count', 'off')      # Count characters

    if not kk:
        return render(request, 'about.html', {'error': "❌ Please enter text in the field."})

    result = kk

    if checkbox == "on":
        temp = ""
        for char in result:
            if not char.isdigit():
                temp += char
        result = temp

    if checkbox2 == "on":
        result = result.upper()

    char_count = None
    if checkbox3 == "on":
        char_count = len(result)

    # Pass result and count to the template
    context = {
        'result': result,
        'char_count': char_count,
    }


    return render(request, 'about.html', context)

