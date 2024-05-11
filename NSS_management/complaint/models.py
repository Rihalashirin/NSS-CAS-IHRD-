from django.db import models
from volunteer.models import Volunteer


# Create your models here.
class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
   # volunteer_id = models.IntegerField()
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'complaint'

