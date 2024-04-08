from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Expansion(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("expansion-detail", args=[str(self.id)])
    
    def get_raid(self):
        return Raid.objects.select_related('expansion').all().filter(expansion=self.id)
    
class Raid(models.Model):
    name = models.CharField(max_length=200)
    expansion = models.ForeignKey(Expansion, null=True, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("raid-detail", args=[str(self.id)])
    
    def get_bosses(self):
        return Boss.objects.select_related('raid').all().filter(raid=self.id)
    
# Create your models here.
class Boss(models.Model):
    name = models.CharField(max_length = 200)
    raid = models.ForeignKey(Raid, null=True, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("boss-detail", args=[str(self.id)])

class BossStrat(models.Model):
    title = models.CharField(max_length = 200, default='Boss Name Here')
    description = models.CharField(max_length=1000,default='Boss Description Here')
    is_active = models.BooleanField(default=True,)
    roster = models.TextField(blank=True)
    ertNote = models.TextField(blank=True)
    weakaura = models.CharField(max_length=200,blank=True)
    video = EmbedVideoField(blank=True)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("strat-detail", args=[str(self.id)])
    





