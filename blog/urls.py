from blog import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path('about/', views.AboutView.as_view(), name="about"),

    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/publish/', views.post_publish, name="post_publish"),

    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name="add_comment_to_post"),
    path('comment/<int:pk>/approve/',
         views.comment_approval, name="comment_approval"),
    path('comment/<int:pk>/remove/', views.comment_remove, name="comment_remove"),

    path('drafts/', views.DraftPostListView.as_view(), name="draft_list"),
]
