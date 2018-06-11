from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
from .viewsets import SmsInfoViewSet, ChartData, AddData, StatsViewSet, DatabaseData
from .views import contact_page

router = DefaultRouter()
router.register(r'sms', SmsInfoViewSet)

urlpatterns = [
    url(r'dashboard/$', views.dashboard, name='api-dashboard'),
    url(r'chart/$', views.chart, name='api-chart'),
    url(r'echartdata/$', views.echart, name='api-echart'),
    url(r'chart-data/$', ChartData.as_view(), name='api-chart-data'),
    url(r'send_message/$', contact_page, name='api-chart-data'),
    url(r'add_data/$', AddData.as_view(), name='add-data'),
    url(r'data_base/$', DatabaseData.as_view(), name='database-data')

]

urlpatterns += router.urls
