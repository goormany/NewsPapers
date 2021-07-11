from django.core.management.base import BaseCommand, CommandError
from news.models import *


class Command(BaseCommand):
    help = 'УДАЛЕНИЕ ВСЕХ ПОСТОВ С САЙТА'

    def handle(self, *args, **options):
        master_code = '7548'
        answer = input('Введите мастер код: ')

        if answer == master_code:
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Успешно! Все посты удалены!'))
        else:
            self.stdout.write(self.style.ERROR('В доступе отказано!'))