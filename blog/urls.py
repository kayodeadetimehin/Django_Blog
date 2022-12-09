from django.urls import path
from blog.views import PostTemplateView, PostListView, PostDetailView, PolicyView


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name= 'home'),
    path('about/', PostTemplateView.as_view(), name= 'about'),
    path('policy/', PolicyView.as_view(), name= 'policy'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post_detail')
]