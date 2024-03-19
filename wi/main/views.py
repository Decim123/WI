from django.shortcuts import render

def main_page(request):
    return render(request, 'html\main_page.html')