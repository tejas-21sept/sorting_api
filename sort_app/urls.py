from django.urls import include, path
from .views import SortArrayAPIView

urlpatterns = [
    path("sort/", SortArrayAPIView.as_view(), name=""),
    
]
