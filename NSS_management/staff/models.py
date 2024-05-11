from django.db import models

# Create your models here.
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contact = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'staff'