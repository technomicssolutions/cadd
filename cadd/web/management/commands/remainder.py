from django.core.management.base import BaseCommand
from datetime import datetime
import time
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives, mail_admins
from django.conf import settings

from admission.models import Student, Enquiry, Installment
# from fees.models import Fees
text_content = 'This is an Important Message'

class Command(BaseCommand):
    help = "Create initial test user and pre-requisite data"

    def handle(self, *args, **options):

        date = datetime.now()
        current_date = date.date()
        # Reminder about the next follow up
        try:
            current_follow_ups = Enquiry.objects.filter(follow_up_date__year=current_date.year, follow_up_date__month=current_date.month, follow_up_date__day=current_date.day)
            subject = "Today's Follow Ups"
            from_email = settings.DEFAULT_FROM_EMAIL
            follow_up_list = []
            for enquiry in current_follow_ups:
                follow_up_list.append({
                    'name': enquiry.student_name,
                    'enquiry_no': enquiry.auto_generated_num,
                    'date': enquiry.saved_date.strftime('%d/%m/%Y'),
                })
            ctx = {
                'enquiries': follow_up_list,
            }
            html_content = render_to_string('email/follow_up_remainder.html', ctx)
            msg = EmailMultiAlternatives(subject, text_content, from_email, ['geethusureh@gmail.com'])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
        except Exception as ex:
            print str(ex)

        # Reminder about the Fees collection



