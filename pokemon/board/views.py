from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return render(request, "board/index.html")
    #return render(
    #    request,
    #    "pokemon/index.html",
    #    context={
    #        "tiles": [123, 456]
    #    }
    #)
