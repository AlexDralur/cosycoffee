from django import forms
from .models import Producer


class ProducerForm(forms.ModelForm):
    """Function to create the producers form"""
    class Meta:
        model = Producer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                "class"] = "border border-dark rounded-0"