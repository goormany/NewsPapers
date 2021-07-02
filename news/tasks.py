from datetime import timedelta, timezone, datetime
from celery import shared_task
import time
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
from django.utils.timezone import localtime
from django.contrib.sites.shortcuts import get_current_site


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def week_email_sending():
    print(f'Start at {localtime()}')
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    for user in User.objects.all():
        if len(user.category_set.all()) > 0:
            posts = Post.objects.filter(data__range=(start_date, end_date), text=user.first_name)
            html_content = render_to_string(
                'weekly_mailing.html',
                {
                    'site': settings.BASE_URL,
                    'news': posts,
                    'username': user.first_name,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Здравствуйте {user.first_name}. Мы подготовили дайджест статей за неделю с нашего портала',
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=user.email
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

# @shared_task
# def day7_mail():
#     for category in Category.objects.all():
#         subject = f'Последние статьи за 7 дней в категории {category}'
#         end_date = timezone.now()
#         start_date = end_date - timedelta(days=7)
#         posts = Post.objects.filter(postCategory=category, data__range=(start_date, end_date))
#         if posts.exists():
#             for sub in category.subscibers.all():
#                 html_content = render_to_string(
#                     'weekly_mailing.html',
#                     {
#                         'username': sub,
#                         'posts': posts,
#                         'category': category,
#                         'site': settings.BASE_URL,
#                     }
#                 )
#                 msg = EmailMultiAlternatives(
#                     subject=subject,
#                     from_email=settings.DEFAULT_FROM_EMAIL,
#                     to=sub.email
#                 )
#                 msg.attach_alternative(html_content, 'text/html')
#                 msg.send()