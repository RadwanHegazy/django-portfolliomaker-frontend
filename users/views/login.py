from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages

class login_view (View) : 
    def get(self,request,**kwargs) : 
        return render(request,'login.html')

    def post (self,request,**kwargs) : 
        data = {
            'email' : request.POST.get('email'),
            'password' : request.POST.get('password'),
        }
        action = Action(
            url = MAIN_URL + '/user/auth/login/',
            data=data
        )

        action.post()

        if action.is_valid() : 
            response = redirect('profile')
            response.set_cookie('user',action.json_data['token'])
            return response
        else:
            messages.error(request,action.json_data['message'])
            return redirect('login')