from django.db import models
from volunteer.models import Volunteer
from event.models import Event
# Create your models here.
class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    # volunteer_id = models.IntegerField()
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    attendance = models.CharField(max_length=45)
    #event_id = models.IntegerField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    performance = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'attendance'

