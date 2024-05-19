from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from globals.decorators import login_required

class profile_view (View) : 
    
    @login_required
    def get(self,request,**kwargs) : 

        return render(request,'profile.html')
    

    @login_required
    def post(self,request, **kwargs) :
        
        
        data = {
            'about' : request.POST.get('about'),
            'jop_title' : request.POST.get('jop_title'),
            'is_working' :1 if request.POST.get('is_working') == 'on' else 0,
        } 
        action = Action(
            url = MAIN_URL + "/update/",
            headers=kwargs['headers'],
            data=data
        )

        action.put()
        print(action.json_data)
        return redirect('profile')
    