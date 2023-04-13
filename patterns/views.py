from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pattern
from .forms import PatternForm

# Create your views here.


class AddPattern(LoginRequiredMixin, CreateView):
    """Add pattern view"""
    template_name = 'patterns/add_pattern.html'
    model = Pattern
    form_class = PatternForm
    success_url = '/patterns/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPattern, self).form_valid(form)
