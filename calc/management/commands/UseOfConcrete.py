from django.core.management.base import BaseCommand, CommandError
from calc.models import Use


class Command(BaseCommand):
    def handle(self, *args, **options):
        c1 = Use.objects.create()
        c1.name = 'Podkład, wylewka'
        c1.save()

        c2 = Use.objects.create()
        c2.name = 'Schody'
        c2.save()

        c3 = Use.objects.create()
        c3.name = 'Chudy beton'
        c3.save()

        c4 = Use.objects.create()
        c4.name = 'Fundamenty'
        c4.save()

        c5 = Use.objects.create()
        c5.name = 'Stropy/wieńce'
        c5.save()

        c6 = Use.objects.create()
        c6.name = 'Ściany/słupy'
        c6.save()

        c7 = Use.objects.create()
        c7.name = 'Płyty chodnikowe/krawężniki - podsypka'
        c7.save()

        c8 = Use.objects.create()
        c8.name = 'Inne zastosowanie'
        c8.save()