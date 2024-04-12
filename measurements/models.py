from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)  # Define value con un valor predeterminado de 0
    unit = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
