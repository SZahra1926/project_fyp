from django import forms
from .models import LipSyncTask

class LipSyncForm(forms.ModelForm):
    class Meta:
        model = LipSyncTask
        fields = ['video', 'audio']
