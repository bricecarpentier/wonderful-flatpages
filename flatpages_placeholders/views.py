from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView

from .models import Placeholder


class PlaceholderUpdateView(UpdateView):
    model = Placeholder
    fields = ['content']
    success_url = '/first/'

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(PlaceholderUpdateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            d = {}
            d[self.request.POST.get('name')] = self.request.POST.get('value', '')
            kwargs.update({
                'data': d,
                'files': self.request.FILES,
            })

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})

        return kwargs

    def get_success_url(self):
        if hasattr(self, 'object') and self.object is not None and self.object.page is not None:
            return self.object.page.url
        else:
            return '/'
