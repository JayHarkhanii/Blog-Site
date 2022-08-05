from django.conf.urls import url
from blog import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^accounts/login/$',auth_views.LoginView.as_view(),{'template_name':'login.html'} ,name="login"),
    url(r'^accounts/logout/$',auth_views.LogoutView.as_view(),{'next_page':settings.LOGIN_REDIRECT_URL} ,name="logout"),
    url(r'^about$',views.AboutView.as_view(),name="about"),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
    url(r'^post/new/$',views.CreatePostView.as_view(),name="post_new"),
    url(r'^post/(?P<pk>\d+)/edit$',views.PostUpdateView.as_view(),name="post_edit"),
    url(r'^post/(?P<pk>\d+)/remove$',views.PostDeleteView.as_view(),name="post_remove"),
    url(r'^drafts/$',views.DraftListView.as_view(),name="post_draft_list"),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name="add_comment_to_post"),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name="comment_approve"),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name="comment_remove"),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name="post_publish"),
]
