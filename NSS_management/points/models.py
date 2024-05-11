from django.db import models
from volunteer.models import Volunteer
from attendance.models import Attendance

# Create your models here.
class Points(models.Model):
    points_id = models.AutoField(primary_key=True)
   # volunteer_id = models.IntegerField()
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    attendance_id = models.IntegerField()
    # attendance=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    points = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'points'
