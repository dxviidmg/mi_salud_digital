from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'patients'

router = DefaultRouter() 
router.register('patients', PatienViewSet, basename='patients')
urlpatterns = router.urls