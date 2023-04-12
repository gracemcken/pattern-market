from django.views.generic import CreateView
from .models import Pattern

# Create your views here.


class AddPattern(CreateView):
    """Add pattern view"""
    template_name = 'patterns/add_pattern.html'
    model = Pattern
    success_url = '/patterns/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPattern, self).form_valid(form)
