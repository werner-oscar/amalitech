from django.urls import path
from .views import Greatings,DetectFace

urlpatterns = [
    path("",Greatings.as_view()),
    path("detect",DetectFace.as_view()),
]
