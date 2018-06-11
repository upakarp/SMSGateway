import datetime as dt
from datetime import timedelta

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.utils.timezone import now

from .forms import ContactForm
from .models import SmsInfo

from . import tasks


def dashboard(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404

    data_list = SmsInfo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(data_list, 3)

    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    return render(request, 'sms_api/dashboard.html', {'datas':datas})


def chart(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    return render(request, 'sms_api/chart.html', {
    })


def echart(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    return render(request, 'sms_api/bar-gradient.html', {
    })


def contact_page(request):

    contact_form = ContactForm(request.POST or None)

    context = {
        "title": "Message Dashboard",
        "page_title": "Send Message",
        "content": "Welcome to the Message Dashboard",
        "form": contact_form
    }

    if request.method == "POST":


        # SmsInfo.objects.create(phone_no=request.POST.get('phone_number'),
        #                        message=request.POST.get('content'),
        #                        sent_date=request.POST.get('time'))
        if contact_form.is_valid():
            form = contact_form.cleaned_data
            phone = form['phone_number']
            content = form['content']
            time = form['time']
            current_time = dt.datetime.now()

            # print(time)
            # print(time.timestamp())
            # print(current_time.timestamp())
            interval = time.timestamp() - current_time.timestamp()
            # interval > 10
            if interval > 20:
                print(12)
                #tasks.date_post_database.delay(phone, content, time)
                tasks.date_post_database.apply_async((phone, content, time), countdown=interval)
            else:
                SmsInfo.objects.create(phone_no=request.POST.get('phone_number'),
                                        message=request.POST.get('content'),
                                        sent_date=request.POST.get('time'))
            return redirect('http://localhost:8000/api/sms/')

    return render(request, "contact/view.html", context)
