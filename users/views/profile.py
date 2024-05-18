from django.views import View
from globals.request_manager import Action
from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from django.contrib import messages
from globals.decorators import login_required


class profile_view (View) : 
    
    @login_required
    def get(self,request,**kwargs) : 
        
        return render(request,'profile.html')