from django.http import HttpResponse
from django.shortcuts import render

from .dice import roll_dice
from .models import Player


def roll(request):
    return render(
        request,
        "board/roll.html",
        context={
            "dice": roll_dice(),
        }
    )


def test(request):
    return render(
        request,
        "board/index.html",
        #context={
        #    "player": Player.objects.last()
        #}
    )
