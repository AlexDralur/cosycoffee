from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Function to create the recipes form"""
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"] = "border border-dark rounded-0"