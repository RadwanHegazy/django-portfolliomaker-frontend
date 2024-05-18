from django.shortcuts import render, HttpResponse
from django.views import View
from globals.tenant_utils import TenantManager
from django.http import Http404
from frontend.settings import MAIN_URL
from globals.request_manager import Action

class home_view (View) : 
    
    def get(self,request,**kwargs) : 
        tenant = TenantManager(request)
        context = {}

        if tenant.has_tenant:
            context['tenant'] = tenant.tenant
            return render(request,'user-tenant.html',context)
        
        # action to get all
        action = Action(
            url = MAIN_URL + '/get/all/'
        )

        action.get()

        print(action.json_data)
        context['tenants'] = action.json_data
        return render(request,'index.html', context)