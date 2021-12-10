from django.contrib import admin
from .models import Concrete, Use, Person, Day

# Register your models here.

admin.site.register(Concrete)
admin.site.register(Use)
admin.site.register(Person)
admin.site.register(Day)