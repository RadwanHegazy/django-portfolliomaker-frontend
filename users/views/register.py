from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages

class register_view (View) : 
    def get(self,request,**kwargs) : 
        return render(request,'register.html')

    def post (self,request,**kwargs) : 
        data = {
            'email' : request.POST.get('email'),
            'full_name' : request.POST.get('full_name'),
            'password' : request.POST.get('password'),
        }

        action = Action(
            url = MAIN_URL + '/user/auth/register/',
            data=data
        )

        if 'picture' in request.FILES : 
            action.files = {
                'picture' : request.FILES.get('picture')
            }

        action.post()
        print(action.json_data)
        if action.is_valid() : 
            response = redirect('profile')
            response.set_cookie('user',action.json_data['token'])
            return response
        else:
            messages.error(request,'an error accoured')
            return redirect('register')