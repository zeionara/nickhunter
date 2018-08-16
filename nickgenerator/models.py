from django.db import models

class Nick(models.Model):
    title = models.CharField(max_length = 64)
    date = models.DateTimeField('date generated')
    rating = models.IntegerField(default = 0)

    def __str__(self):
        return '%s created %s' % (self.title, str(self.date))

class Like(models.Model):
    ip_address = models.CharField(max_length = 20)
    nick_title = models.CharField(max_length = 64)
    
    def __str__(self):
        return '%s liked %s' % (self.ip_address, self.nick_title)
