import inspect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import *
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import redirect

# @receiver(post_save, sender=Post)
# def sub_mail(sender, instance, created, **kwargs):
#     if created:
#         subject = f'{instance.title} {instance.data.strftime("%d %m %Y")}'
#     else:
#         subject = f'Изменено  {instance.previewName} {instance.data.strftime("%d %m %Y")}'
#
#     send_mail(
#         subject=subject,
#         message=instance.text,
#         from_email='testemops@yandex.ru',
#         recipient_list=['testemops@yandex.ru']
#     )
