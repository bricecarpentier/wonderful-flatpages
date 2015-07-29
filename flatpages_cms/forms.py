from django.forms.models import modelform_factory
from .models import Image


ImageForm = modelform_factory(Image,
    fields=('file', 'alternative_text'))
