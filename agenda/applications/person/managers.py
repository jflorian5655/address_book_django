from django.db import models
from django.db.models import Count


class MeetingManager(models.Manager):
    """
    Manager para el modelo meeting
    """

    def number_of_meetings_by_job(self):
        result = self.values('person__job').annotate(quantity=Count('id'))

        return result




