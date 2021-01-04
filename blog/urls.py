from django.urls import path, include
from blog.views import HomePageView, PostDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('<int:pk>/', PostDetailsView.as_view(), name = 'post_detail'),
]
