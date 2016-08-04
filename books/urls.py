from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
	url(r'^books/$', views.book_list),
	url(r'^books/(?P<pk>[0-9]+)/$', views.book_details),
	url(r'^add/$', views.book_add),
]

urlpaterns = format_suffix_patterns(urlpatterns)
