from django.db import models
from django.contrib.auth.models import User

class LipSyncTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    audio = models.FileField(upload_to='audios/')
    output_video = models.FileField(upload_to='output_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
