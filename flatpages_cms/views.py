from django.views.generic.edit import CreateView

from .models import Image


class CreateImageView(CreateView):
    model = Image
