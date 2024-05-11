from django.db import models

# Create your models here.
class Volunteer(models.Model):
    volunteer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    regno = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    volunteer_attendance = models.CharField(max_length=45)
    performance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteer'

