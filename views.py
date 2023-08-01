from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

Plans = [
    {"id": "1",
     "month": "January",
     "plan": "Recover after the New Year"},

    {"id": "2",
     "month": "February",
     "plan": "Survive the shortest month and look forward to the spring"},

    {"id": "3",
     "month": "March",
     "plan": "Welcome the spring and wait for more sun"},

    {"id": "4",
     "month": "April",
     "plan": "Enjoy the first warm days and the blossoming nature"},

    {"id": "5",
     "month": "May",
     "plan": "Wait for the much-desired end of kids' school year"},

    {"id": "6",
     "month": "June",
     "plan": "Give the kids to their grandparents and relax"},

    {"id": "7",
     "month": "July",
     "plan": "Take care of health, rest, and sleep"},

    {"id": "8",
     "month": "August",
     "plan": "Celebrate two birthdays"},

    {"id": "9",
     "month": "September",
     "plan": "Launch the new academic year at school"},

    {"id": "10",
     "month": "October",
     "plan": "Enjoy autumn rains and nature getting to sleep"},

    {"id": "11",
     "month": "November",
     "plan": "Sleep in the rhythm with nature"},

    {"id": "12",
     "month": "December",
     "plan": "Look forward to the New Year"},
]

def year_plans(request):
    string = ''
    for item in Plans:
        url = "" + item['id']
        string += f"""
        <div>
        <a href={url}><button>{item['id']}\n </button></a>
        <br>
        </div>

        """

    return HttpResponse(string)


def month_plan(request, title):
    string = ''
    for item in Plans:
        if item['id'] == title:
            title = item['month']
            string += f"""
                    <div>
                    <h1>{item['month']}</h1>
                    <h2>{item['plan']}</h2>
                    <br>
                    </div>

                    """
    return redirect("http://127.0.0.1:8000/{item['month']}")


#def redirect_to(request, title):
    #for item in Plans:
        #if item['id'] == title:
            #title = item['month']
            #response = redirect(title)
        #return response






