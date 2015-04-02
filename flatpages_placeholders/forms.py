from django import forms

from .models import Placeholder


class ContentOnlyPlaceholderForm(forms.ModelForm):
    class Meta:
        model = Placeholder
        fields = ['content', ]
