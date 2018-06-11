# This page is not used anymore in the project.

from .forms import ContactForm
from .models import SmsInfo


def date_post(request, phone, content, time):

    if request.method == 'POST':
        SmsInfo.objects.create(phone_number=phone,
                               content=content,
                               time=time)


