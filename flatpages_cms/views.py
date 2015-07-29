from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Image


class CreateImageView(CreateView):
    model = Image
    fields = ('name', 'description', 'file', 'alternative_text')

    def form_valid(self, form):
        super(CreateImageView, self).form_valid(form)
        return HttpResponse(self.object.pk)
