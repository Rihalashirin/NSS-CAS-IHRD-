from django.db import models
from event.models import Event
# Create your models here.
class Gallery(models.Model):
    gallery_id = models.AutoField(primary_key=True)
    # event_id = models.IntegerField()
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    images = models.CharField(max_length=45)
    videos = models.CharField(max_length=45)
    images2 = models.CharField(max_length=45, blank=True, null=True)
    images3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gallery'