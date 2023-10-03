from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        cat_list = [
            {'name': 'Телевизор', 'description': 'для ТВ'},
            {'name': 'Телефон', 'description': 'для звонков'},
            {'name': 'Ноутбук', 'description': 'для досуга'},
            {'name': 'Монитор', 'description': 'для ПК'}
        ]
        cat_for_create = []
        for cat_item in cat_list:
            cat_for_create.append(
                Category(**cat_item)
            )

        Category.objects.bulk_create(cat_for_create)