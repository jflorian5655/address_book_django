from django.db import models

from .managers import MeetingManager

from model_utils.models import TimeStampedModel


class Hobby(TimeStampedModel):
    """
    Nodelo que representa la tabla Hobby
    """
    hobby = models.CharField('Pasa tiempo', max_length=50)

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.hobby


class Person(TimeStampedModel):
    """
    Modelo que representa la tabla person
    """

    full_name = models.CharField('Nombres', max_length=50)
    job = models.CharField('Trabajo', max_length=100, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField('teléfono', max_length=15, blank=True)
    hobbies = models.ManyToManyField(Hobby)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.full_name


class Meeting(TimeStampedModel):
    """
    Modelo que representa la tabbla meeting
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_meet = models.DateField()
    time = models.TimeField()
    subject = models.CharField('Asunto', max_length=100)

    objects = MeetingManager()

    class Meta:
        verbose_name = "Reunión"
        verbose_name_plural = "Reuniones"

    def __str__(self):
        return self.subject





