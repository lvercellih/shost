from django.conf.urls import url, include

urlpatterns = [
    url(r'^rest/', include('shost.api.rest.urls', namespace='rest')),
]