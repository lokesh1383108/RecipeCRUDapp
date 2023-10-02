

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from recepie.models import *   # here we import the apps model in the view file of root directory
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


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
        return redirect('/')
    querySet = Recipe.objects.all()
    context = {'recipe' : querySet}
        
    return render(request,"recepie/index.html",context)

def register(request):
    if request.method=="POST":
     data = request.POST

     first_name = request.POST.get('first_name')
     last_name = request.POST.get('last_name')
     username = request.POST.get('username')
     password = request.POST.get('password')

     user = User.objects.create(
     first_name= first_name,
     last_name = last_name,
     username = username,
     password = password

     )
     user.save()
     return redirect('/login/')
     
    return render(request, "recepie/register.html")

def loginpage(request):
   if request.method=="POST":
      username = request.POST.get('username') # username = request.POST['username']
      password = request.POST.get('password')
      print(username)
      print(password)
      user = authenticate(username = username, password= password)
      print(user)
      if user is not None:
         print('This login is authenticate ')
         login(request,user)
         return redirect('/')
      else:
         print('else condition is running ')
         return HttpResponse("<h1>This is not working</h1>")
      
   return render(request, "recepie/login.html")