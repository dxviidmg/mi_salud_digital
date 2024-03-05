from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'consultations'

router = DefaultRouter() 
router.register('consultations', ConsultationViewSet, basename='consultations')
urlpatterns = router.urls