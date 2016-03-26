from django.conf.urls import url
from apple import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'snippets/$', views.SnippetList.as_view()),
    url(r'snippets/(?P<pk>[0-9]+)/$', views.SnipettDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)