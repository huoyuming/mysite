from django.conf.urls import patterns, url

from views import ZufangItems

urlpatterns = patterns('',
    url(r'^zufang-items/$', ZufangItems.as_view()),
)