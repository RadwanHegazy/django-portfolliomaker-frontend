from dataclasses import dataclass
from .request_manager import Action
from frontend.settings import MAIN_URL
from django.http import Http404

@dataclass
class TenantManager :
    request:object
    @property
    def has_tenant (self):
        if self.has_tenant_from_host:
            url = self.get_tenant_url
            action = Action(
                url=url
            )
            action.get()

            if action.is_valid() :
                if action.json_data['tenant']['is_working'] == False:
                    raise Http404(self.request)
                self.tenant = action.json_data
                return True
            
            raise Http404(self.request)
        
    @property
    def get_tenant_url (self) -> str: 
        tenant_name = self.request.get_host().split('.')[0]
        url = MAIN_URL + f"/get/tenant/{tenant_name}/"
        return url
    
    @property
    def has_tenant_from_host(self) -> bool: 
        hostname:str = self.request.get_host()
        split_tenant_name = hostname.split('.')
        if len(split_tenant_name) > 1:
            return True
        return False