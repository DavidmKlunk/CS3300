from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StratForm(ModelForm):
    class Meta:
        model = BossStrat
        fields = '__all__'