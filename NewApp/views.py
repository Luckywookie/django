from django.shortcuts import render, render_to_response

# Create your views here.


def main(request):
    return render_to_response('index.html')


def first(request):
    return render_to_response('first.html')


def second(request):
    return render_to_response('second.html')
