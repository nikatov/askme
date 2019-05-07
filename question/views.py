from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    questions_list = [
        {"name": "my best questiion", "id": 1},
        {"name": "my best questiion2", "id": 2},
    ]
    return render(request, "question/base.html", {
        "questions": questions_list,
    })
