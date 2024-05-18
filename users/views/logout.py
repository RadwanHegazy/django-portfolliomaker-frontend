from django.views import View
from django.shortcuts import redirect

class logout_view (View) : 
    def get(self,request,**kwargs) : 
        response = redirect('profile')
        response.delete_cookie('user')
        return response
