from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

import challenges

# Create your views here.

challenges = {
    "january": "Dont eat meat for 30 days",
    "february": "Pray 5 times a day for 30 days",
    "march": "Walk for 30 minutes everyday",
    "april": "Fast for 1 day after every 2 days",
    "may": "Run for 1 mile a day",
    "june": "Dont swear for 30 days",
    "july": "Give $5 to charity everyday",
    "august": "Don't lie at all for 30 days",
    "september": "Walk for 1 hour everyday",
    "october": "Fast for 15 days in a month",
    "november": "Pray 5 times with congregation",
    "december": "Run for 2 miles everyday"
}

def index(request):
    months = list(challenges.keys())
    list_items = ""
    for month in months:
        caps = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href = \"{month_path}\"><h1>{caps}</h1></a></li>"

    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)


def monthly_challenge_num(request, month):
    months = list(challenges.keys())
    try:
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args = [redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month")

def monthly_challenge(request, month):
    challenge_text = ""
    caps = str(month).capitalize()
    try:
        challenge_text = challenges[month]
    except:
        return HttpResponseNotFound("Invalid Month")
    return render(request, "challenges/challenge.html", {
        "text": challenge_text,
        "month": caps
    })