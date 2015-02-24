from django.conf.urls import patterns,url
from main import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name ='index'),
                       url(r'^tags/$',view.tags,name = 'tags'),
                       url(r'^tags/(?P<tag_name>\w+)/$',view.tag,name ='tag'),
                       url(r'^add_link/$',view.add_link,name='add_link'),
                       )