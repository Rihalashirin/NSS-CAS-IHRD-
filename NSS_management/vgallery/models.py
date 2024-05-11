from django.db import models
from volunteer.models import Volunteer
from event.models import Event

# Create your models here.
class Vgallery(models.Model):
    vgallery_id = models.AutoField(primary_key=True)
    #volunteer_id = models.IntegerField()
    volunteer=models.ForeignKey(Volunteer,on_delete=models.CASCADE)
    #event_id = models.IntegerField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    classes = models.CharField(max_length=45)
    date = models.DateField()
    images = models.CharField(max_length=545)
    videos = models.CharField(max_length=545, blank=True, null=True)
    images2 = models.CharField(max_length=545, blank=True, null=True)
    images3 = models.CharField(max_length=545, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vgallery'


