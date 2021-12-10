from django.core.management.base import BaseCommand, CommandError
from calc.models import Day, Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        p1 = Person.objects.create()
        p1.first_name = 'Zdzisław'
        p1.last_name = 'Kowalski'
        p1.description = 'Specjalista ds. Obsługi Klienta'
        p1.save()

        p2 = Person.objects.create()
        p2.first_name = 'Janina'
        p2.last_name = 'Nowak'
        p2.description = 'Młodszy Specjalista ds. Obsługi Klienta'
        p2.save()

        p3 = Person.objects.create()
        p3.first_name = 'Andrzej'
        p3.last_name = 'Leszczyński'
        p3.description = 'Starszy Specjalista ds. Obsługi Klienta'
        p3.save()

        p4 = Person.objects.create()
        p4.first_name = 'Magdalena'
        p4.last_name = 'Łaminoga'
        p4.description = 'Specjalista ds. Obsługi Klienta'
        p4.save()

        p5 = Person.objects.create()
        p5.first_name = 'Renata'
        p5.last_name = 'Skowrońska'
        p5.description = 'Starszy Specjalista ds. Obsługi Klienta'
        p5.save()

        p6 = Person.objects.create()
        p6.first_name = 'Krzysztof'
        p6.last_name = 'Dobija'
        p6.description = 'Młodszy Specjalista ds. Obsługi Klienta'
        p6.save()

        # p1 = Person.objects.get(id=6)
        # p1.delete()


