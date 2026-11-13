from django.urls import path
from .views import home_page_view, post_detail

urlpatterns = [
    path("", home_page_view.as_view(), name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]