from django.urls import path
from .import views

app_name = 'resume_blog'

urlpatterns = [
    path("",views.index, name="index")
    # path("",views)
]
