import requests
from django.shortcuts import redirect
from .request_manager import Action
from frontend.settings import MAIN_URL

def login_required (function) : 

    def wrapper (self, request, **kwargs) : 

        user = request.COOKIES.get('user',None)

        if user is None :
            return redirect('login')
        
        action = Action(
            url = MAIN_URL + '/user/profile/',
            headers = {'Authorization':f"Bearer {user}"}
        )

        action.get()

        if not action.is_valid() : 
            return redirect('login')

        kwargs['headers'] = {'Authorization':f"Bearer {user}"}
        kwargs['user'] = action.json_data
        
        func = function(self,request,**kwargs)
        return func
    
    return wrapper
