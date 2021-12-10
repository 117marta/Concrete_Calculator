from django.core.management.base import BaseCommand, CommandError
from calc.models import Day, Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        JK = Person.objects.get(id=12)
        JN = Person.objects.get(id=13)
        AL = Person.objects.get(id=14)
        ML = Person.objects.get(id=15)
        RS = Person.objects.get(id=16)
        KD = Person.objects.get(id=17)

        Day.objects.create(day=1, hour=1, persons=JK)
        Day.objects.create(day=1, hour=2, persons=JN)
        Day.objects.create(day=1, hour=3, persons=AL)
        Day.objects.create(day=2, hour=1, persons=ML)
        Day.objects.create(day=2, hour=2, persons=RS)
        Day.objects.create(day=2, hour=3, persons=KD)
        Day.objects.create(day=3, hour=1, persons=AL)
        Day.objects.create(day=3, hour=2, persons=JK)
        Day.objects.create(day=3, hour=3, persons=JN)
        Day.objects.create(day=4, hour=1, persons=RS)
        Day.objects.create(day=4, hour=2, persons=KD)
        Day.objects.create(day=4, hour=3, persons=ML)
        Day.objects.create(day=5, hour=1, persons=JN)
        Day.objects.create(day=5, hour=2, persons=AL)
        Day.objects.create(day=5, hour=3, persons=JK)
        Day.objects.create(day=6, hour=1, persons=KD)
        Day.objects.create(day=6, hour=2, persons=ML)
        Day.objects.create(day=6, hour=3, persons=RS)





