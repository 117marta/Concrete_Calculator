from django.core.management.base import BaseCommand, CommandError
from calc.models import Concrete


class Command(BaseCommand):
    def handle(self, *args, **options):
        c1 = Concrete.objects.create()
        c1.name = 'C8/10'
        c1.description = 'Dawniej B10'
        c1.save()

        c2 = Concrete.objects.create()
        c2.name = 'C12/15'
        c2.description = 'Dawniej B15'
        c2.save()

        c3 = Concrete.objects.create()
        c3.name = 'C16/20'
        c3.description = 'Dawniej B20'
        c3.save()

        c4 = Concrete.objects.create()
        c4.name = 'C20/25'
        c4.description = 'Dawniej B25'
        c4.save()

        c5 = Concrete.objects.create()
        c5.name = 'C25/30'
        c5.description = 'Dawniej B30'
        c5.save()

        c6 = Concrete.objects.create()
        c6.name = 'C30/37'
        c6.description = 'Dawniej B37. Także B35, B40 według "PN-S-10042:1991" - norma mostowa'
        c6.save()

        c7 = Concrete.objects.create()
        c7.name = 'C35/45'
        c7.description = 'Dawniej B45'
        c7.save()

        c8 = Concrete.objects.create()
        c8.name = 'C40/50'
        c8.description = 'Dawniej B50'
        c8.save()

        c9 = Concrete.objects.create()
        c9.name = 'C45/55'
        c9.description = 'Dawniej B55'
        c9.save()

        c10 = Concrete.objects.create()
        c10.name = 'C50/60'
        c10.description = 'Dawniej B60'
        c10.save()

        c11 = Concrete.objects.create()
        c11.name = 'C55/67'
        c11.save()

        c12 = Concrete.objects.create()
        c12.name = 'C60/75'
        c12.save()

        c13 = Concrete.objects.create()
        c13.name = 'C70/85'
        c13.save()

        c14 = Concrete.objects.create()
        c14.name = 'C80/95'
        c14.save()

        c15 = Concrete.objects.create()
        c15.name = 'C90/105'
        c15.save()

        c16 = Concrete.objects.create()
        c16.name = 'C100/115'
        c16.save()