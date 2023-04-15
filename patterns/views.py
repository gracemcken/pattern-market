from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

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
    
class EditPattern(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """User can edit a pattern they own"""
    template_name = 'patterns/edit_pattern.html'
    model = Pattern
    form_class = PatternForm
    success_url = '/patterns/'
    
    """Code to implement test"""
    def test_func(self):
        return self.request.user == self.get_object().user
    
    
class DeletePattern(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """User can delete a pattern they own"""
    model = Pattern
    success_url = '/patterns/'
    
    """Code to implement test mixin"""
    def test_func(self):
        return self.request.user == self.get_object().user
