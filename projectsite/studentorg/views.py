from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from studentorg.models import Organization
from studentorg.forms import OrganizationForm 
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm  # Corrected from 'from class'
    template_name = 'org_edit.html'  # Corrected from 'template name'
    success_url = reverse_lazy('organization-list') 

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_delete_confirm.html'  # More standard naming
    success_url = reverse_lazy('organization-list') 