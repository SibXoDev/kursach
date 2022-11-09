from django import forms
from .models import Game, SystemRequirements, Categories

class GameCreationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        exclude = ("media", "date")

class SysReqCreationForm(forms.ModelForm):
    class Meta:
        model = SystemRequirements
        fields = '__all__'

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'