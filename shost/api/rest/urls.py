from django.conf.urls import url, include

from shost.api.rest import swagger

urlpatterns = [
    url(r'^admin/', include('shost.api.rest.admin.urls', namespace='admin')),
]