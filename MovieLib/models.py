from django.db import models

# Create your models here.
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Movie(models.Model):
    title = models.CharField(max_length=128)
    releaseDate = models.DateField()
    price = IntegerRangeField(min_value=0, max_value=100)

class todo(models.Model):
    What = models.CharField(max_length=128)
    Deadline = models.DateField()
    Done = IntegerRangeField(min_value=0, max_value=100)