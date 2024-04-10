from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.apps import apps


# Create your views here.
def home(request):
    return render(request, "index.html")



@csrf_exempt
def predict(request):
    if request.method == "POST":
        
        model = apps.get_app_config('SenTilyser').model
        processor = apps.get_app_config('SenTilyser').processor

        audio = request.FILES.get("audio")

        X = processor.pre_process([audio])

        res = model.predict(X)

        res = processor.post_process(res)

        print(res)
        data = {"review": res[0]}


        return  JsonResponse(data)
    else:
        return render(request, "index.html")