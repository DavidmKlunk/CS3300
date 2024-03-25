from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField



# Create your models here.

class BossStrat(models.Model):
    video = EmbedVideoField()