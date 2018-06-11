from datetime import date, timedelta
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication

from .forms import ContactForm
from .pagination import SmsInfoLimitOffSetPagination
from .models import SmsInfo
from . import serializers
from . import models
from . import tasks


class SmsInfoViewSet(viewsets.ModelViewSet):
    queryset = models.SmsInfo.objects.all()
    serializer_class = serializers.SmsInfoSerializer
    search_fields = ('phone_no', 'sent_date')
    authentication_classes = (BasicAuthentication, )
    pagination_class = SmsInfoLimitOffSetPagination


class ChartData(APIView):
    authentication_classes = (BasicAuthentication, )

    def get(self, request, format=None):
        data = tasks.get_chart_data()
        return Response(data)


class AddData(APIView):

    def get(self, request, format=None):

        response_dict = {
            "key1": "val1",
            "key2": "value2"
        }
        # print(tasks.add.delay(4, 4))
        try:
            print(tasks.add.delay(4, 4))
        except:
            print("Try fixing it.")
        return Response(response_dict)

class DatabaseData(APIView):

    def post(self, request, format=None):
        form = ContactForm

        if form.is_valid():
            phone = form.get('phone_number')
            content = form.get('content')
            time = form.get('time')

        try:
            a = tasks.date_post_database.delay(phone, content, time)
        except:
            print("Try fixing it")

        return Response(a.phone)




class StatsViewSet(APIView):

    def get(self, request, format=None):

        # count the number of entries since the given date -- in this case, yesterday to today
        today = date.today() - timedelta(1)
        ct_today = SmsInfo.objects.filter(sent_date__gte=date.today()).count()

        yesterday = date.today() - timedelta(1)
        day_before_yesterday = date.today() - timedelta(2)
        ct_yesterday = SmsInfo.objects.filter(sent_date__range=(yesterday, day_before_yesterday)).count()

        week = date.today() - timedelta(7)
        ct_week = SmsInfo.objects.filter(sent_date__gte=week).count()

        month = date.today() - timedelta(30)
        ct_month = SmsInfo.objects.filter(sent_date__gte=month).count()

        year = date.today() - timedelta(365)
        ct_year = SmsInfo.objects.filter(sent_date__gte=year).count()

        response_dict = {
            "Today": ct_today,
            "Yesterday": ct_yesterday,
            "This Week": ct_week,
            "This Month": ct_month,
            "This Year": ct_year
        }

        return Response(response_dict)
