
from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'cliente',views.ClienteViewSet,basename='api_cliente')


urlpatterns = [
	path('', include(router.urls)),
]
