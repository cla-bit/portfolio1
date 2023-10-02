from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .forms import ContactForm
from .models import Project, Category, Portfolio
from .utils import send_contact_email


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = get_object_or_404(Portfolio, pk=1)
        context['resume'] = portfolio.resume
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = get_object_or_404(Portfolio, pk=1)
        context['professional_summary'] = portfolio.professional_summary
        context['skills'] = portfolio.skills.all()
        return context


class ProjectView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    paginate_by = 1

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        queryset = super().get_queryset().filter(done=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home:contact')

    def form_valid(self, form):
        contact = form.save()
        send_contact_email(contact)
        messages.success(self.request, 'Your message has been sent. Thank you!')
        return super().form_valid(form)
