from django.contrib import admin

from .models import Person, Hobby, Meeting

admin.site.register(Person)
admin.site.register(Hobby)
admin.site.register(Meeting)

