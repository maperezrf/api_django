from django.urls import path,include
from . import views

app_name = 'query'

urlpatterns = [
	path('',views.ClienteView.as_view(), name='query_cliente'),

	#*
	path("api/query/",include('apps.query.api.urls')),

]