from django.contrib import admin
from blog import views
from django.urls import path


urlpatterns = [
    path('^about/$', views.AboutView.as_view(),name = 'about'),
    path('^about/$',views.AboutView.as_view(),name='about'),
    path('^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    path('^postnew/$',views.PostCreateView.as_view(),name='new'),
    path('^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    path('^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    path('^draft/$',views.DraftListView.as_view(),name='post_draft_list'),
    path('^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    path('^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    path('^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    path('^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
