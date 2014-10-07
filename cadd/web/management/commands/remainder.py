from django.core.management.base import BaseCommand
from datetime import timedelta
import time
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives, mail_admins

from admission.models import Student
# from fees.models import Fees

