import logging
from datetime import datetime, timedelta

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives, send_mail
from news.models import User, Post, Category
from django.utils import timezone


logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
# def day7_mail():
#     for category in Category.objects.all():
#         subject = f'Последние статьи за 7 дней в категории {category}'
#         end_date = timezone.now()
#         start_date = end_date - timedelta(minutes=3)
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




# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        # scheduler.add_job(
        #     day7_mail,
        #     trigger=CronTrigger(minute="*/3"),
        #     # То же, что и интервал, но задача тригера таким образом более понятна django
        #     id="day7_mail",  # уникальный айди
        #     max_instances=1,
        #     replace_existing=True,
        # )
        # logger.info("Added job 'day7_mail'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")