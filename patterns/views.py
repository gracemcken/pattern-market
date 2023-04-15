from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pattern
from .forms import PatternForm

# Create your views here.


class Patterns(ListView):
    """View all patterns"""

    template_name = "patterns/patterns.html"
    model = Pattern
    context_object_name = "patterns"


class PatternDetail(DetailView):
    """View pattern details"""

    template_name = "patterns/pattern_detail.html"
    model = Pattern
    context_object_name = "pattern"


class AddPattern(LoginRequiredMixin, CreateView):
    """Add pattern view"""

    template_name = "patterns/add_pattern.html"
    model = Pattern
    form_class = PatternForm
    success_url = "/patterns/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPattern, self).form_valid(form)
