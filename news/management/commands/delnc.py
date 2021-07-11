from django.core.management.base import BaseCommand, CommandError
from news.models import *


class Command(BaseCommand):
    help = 'Комманды для удаления всех постов из категории'
    requires_migrations_checks = True
    missing_args_message = 'Недостаточно аргументов'

    def add_arguments(self, parser):
        parser.add_argument('category_name', type=str)

    def handle(self, *args, **options):
        print('Мастер код: 7548')
        answer = input('Введите Мастер код для удаления: ')

        if answer == '7548':
            try:
                category = str(options['category_name'])
                print(category)
                postdel = Post.objects.filter(postCategory=category).delete()
                print(postdel)
                self.stdout.write(self.style.SUCCESS(f'Успешно. Все новости категории {category} удалены!'))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR('Нет такой категории! Отказано!'))
        else:
            self.stdout.write(self.style.ERROR('В доступе отказано!'))
