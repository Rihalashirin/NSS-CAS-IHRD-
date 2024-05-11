from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=45)
    time = models.TimeField()
    venue = models.CharField(max_length=45)
    date = models.DateField()
    e_nature = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'event'