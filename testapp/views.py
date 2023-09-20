

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from recepie.models import *   # here we import the apps model in the view file of root directory



def listOfFood(request):
    return render(request,"testapp/index.html")

def recepie(request):
    if request.method=="POST":
        # below line is used to get data from frontend to backend 
        data = request.POST

        # we need get the data or print the data from the model for that we can use the below code 
        recipi_img = request.FILES.get('recipe_image')
        recipi_name = data.get("recipe_name")
        recipi_description = data.get("recipe_description")

        # Now we need to save the data of the models , after this data save into the db 
        Recipe.objects.create(
            recipe_image= recipi_img,
            recipe_name = recipi_name,
            recipe_description = recipi_description,
        )
        return redirect('/recipi/')
        
    return render(request,"recepie/index.html")