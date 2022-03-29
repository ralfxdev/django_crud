from django.urls import path
from Api import views
from django.db import router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cervezas', views.CervezaViewSet)
router.register(r'botellas', views.BotellaViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('helloworld/', views.HelloAPIView.as_view()),
]