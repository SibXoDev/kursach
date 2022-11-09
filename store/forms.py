from django import forms
from .models import Game, SystemRequirements

class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        exclude = ("tags", "media", "date")

class SysReqCreationForm(forms.ModelForm):
    class Meta:
        model = SystemRequirements
        fields = '__all__'