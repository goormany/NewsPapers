from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import *
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
import datetime
from django.conf import settings

# @receiver(pre_save, sender=Post)
# def pre_save_handler(sender, instance, *args, **kwargs):
#     start_date = datetime.datetime.today().date()
#     end_date = start_date+datetime.timedelta(days=1)
#     print(instance.PostAuthor)
#     posts_quantity = Post.objects.filter(PostAuthor=instance.PostAuthor, data__range=(start_date, end_date))
#     print(len(posts_quantity))
#     if len(posts_quantity) > 3:
#         raise Exception('Больше 3-х')


# @receiver(post_save, sender=Post)
# def sub_mail(sender, instance, created, **kwargs):
#     sub_list = []
#     for sub in instance.category_id.subscribers.all():
#         sub_list.append(sub.email)
#     if created:
#         subject = f'{instance.title}'# {instance.data.strftime("%d %m %Y")}'
#     else:
#         # subject = f'Изменено  {instance.title} {instance.data.strftime("%d %m %Y")}'
#         pass
#
#     send_mail(
#         subject=subject,
#         message=instance.text,
#         from_email='testemops@yandex.ru',
#         recipient_list=sub_list
#     )

# @receiver(post_save, sender=Post)
# def sub_mail_v2(sender, instance, **kwargs):
#     post = instance
#     sub_list = []
#     for sub in instance.category_id.subscribers.all():
#         sub_list.append(sub.email)
#     html_content = render_to_string(
#         'send_notify_post_create.html',
#         {
#             'username': sub,
#             'post': post,
#             'site': settings.BASE_URL,
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject=post.title,
#         body='text',
#         from_email='testemops@yandex.ru',
#         to=sub_list
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()