from django.core.management.base import BaseCommand, CommandError
from news.models import *



class Command(BaseCommand):
    help = 'Комманды для удаления всех постов из категории'
    requires_migrations_checks = True
    missing_args_message = 'Недостаточно аргументов'

    def add_arguments(self, parser):
        parser.add_argument('category_name', type=str)

    def handle(self, *args, **options):
        master_code = '7548'
        print(f'мастер код: {master_code}')
        answer = input('Введите мастер код: ')

        if answer != master_code:
            self.stdout.write(self.style.ERROR('В доступе отказано!'))
        else:
            try:
                category_name = options['category_name']
                Post.objects.filter(category_id__category_name=category_name).delete()
                self.stdout.write(self.style.SUCCESS(f'Успешно! Посты из категории {category_name}, удалены!'))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Could not find category'))


