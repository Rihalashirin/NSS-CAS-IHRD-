from django.db import models
from event.models import Event
# Create your models here.
class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    report = models.CharField(max_length=45)
    # event_id = models.IntegerField()
    event=models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'report'