from django.db import models

class Nick(models.Model):
    title = models.CharField(max_length = 64)
    date = models.DateTimeField('date generated')

    def __str__(self):
        return '%s created %s' % (self.title, str(self.date))
