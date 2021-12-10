from django.db import models

# Create your models here.


# class Shape(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class Dimensions(models.Model):
#     X = models.FloatField(max_length=5, verbose_name='X:')
#     Y = models.FloatField(max_length=5, verbose_name='Y:')
#     Z = models.FloatField(max_length=5, verbose_name='Z:')
#     R = models.FloatField(max_length=5, verbose_name='R:')
#     W = models.FloatField(max_length=5, verbose_name='W:')
#     H = models.FloatField(max_length=5, verbose_name='H:')
#     V = models.FloatField(max_length=5, verbose_name='V:')
#     T = models.FloatField(max_length=5, verbose_name='T:')
#     volume = models.FloatField(max_length=10, null=True, verbose_name='Objętość:')


class Concrete(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Beton:')
    description = models.CharField(max_length=256, verbose_name='Opis')

    def __str__(self):
        return self.name


class Use(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Zastosowanie')
    conc = models.ManyToManyField(Concrete, related_name='uses')

    def __str__(self):
        return self.name




class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Day(models.Model):
    DAYS = (
        (1, 'Poniedziałek'),
        (2, 'Wtorek'),
        (3, 'Środa'),
        (4, 'Czwartek'),
        (5, 'Piątek'),
        (6, 'Sobota'),
        (7, 'Niedziela'),
    )
    day = models.IntegerField(choices=DAYS)
    HOURS = (
        (1, '5-10'),
        (2, '10-15'),
        (3, '15-20'),
    )
    hour = models.IntegerField(choices=HOURS)
    persons = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='days')

    def __str__(self):
        return self.get_day_display() + ', godzina: ' + self.get_hour_display()


class List(models.Model):
    shape = models.CharField(max_length=50, verbose_name='Kształt')
    volume = models.FloatField(null=True, verbose_name='Objętość')
    concrete = models.CharField(max_length=50, verbose_name='Beton')
    use_of_concrete = models.CharField(max_length=100, verbose_name='Zastosowanie')
    legal_name = models.CharField(max_length=150, null=True, verbose_name='Imię i nazwisko')
    comment = models.TextField(null=True, verbose_name='Komentarz')
    created_date = models.DateTimeField(null=True, auto_now_add=True, verbose_name='Utworzono')
