from django.db import models
from django.conf import settings
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import FormView
from django.forms import inlineformset_factory, formset_factory, BaseInlineFormSet, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset

from django.contrib.auth.models import User
from contacts import models
from contacts.models import Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()
# users = User.objects.all().select_related('profile')

from django.views import generic


class ContactsView(TemplateView):
    model = Contact
    paginate_by = 2
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        url = reverse('contacts')
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.all()[:5]
        return context

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 2
    def get_context_data(self, **kwargs):
    # Call the base implementation first to get the context
        context = super(ContactListView, self).get_context_data(**kwargs)
        # Need Paginator info
        context['object_list'] = Contact.objects.all().order_by('Last_Name')
        return context

class ContactDetailView(generic.DetailView):
    template_name = 'contact_detail.html'
    model = Contact
    context_object_name = "Contact"

    def contact_detail_view(request, pk):
        try:
            Contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404('Contact does not exist')

        return render(request, 'contact_detail.html', context={'Contact': Contact})

class DonorListView(generic.ListView):
    model = Contact
    def get_context_data(self, **kwargs):
        context = super(DonorListView, self).get_context_data(**kwargs)
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='donor')).order_by('Last_Name')
        return context

class VendorListView(generic.ListView):
    model = Contact
    def get_context_data(self, **kwargs):
        context = super(VendorListView, self).get_context_data(**kwargs)
        Owner = User
        context['object_list'] = Contact.objects.filter(Q(Contact_Category='vendor')).order_by('Company')
        return context

class generic_contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ('Owner',)
        # Address = forms.CharField(label='Address', max_length=100)

@login_required
def contacts_new(request):
    if request.method == "POST":
        form = generic_contact_form(request.POST)
        if form.is_valid():
                Contact = form.save(commit=False)
                def save_model(self, request, obj, form, change):
                    obj.Owner_id = request.user
                    super().save_model(request, obj, form, change)
                Contact.save()
                return redirect('contacts')
        else:
            return redirect('nope')
    else:
        form = generic_contact_form()
        return render(request, 'contacts/new_contact.html', {'form': form})

@login_required
def contacts_edit(request, pk):
    Contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = generic_contact_form(request.POST, instance=Contact)
        if form.is_valid():
            Contact = form.save(commit=False)
            Contact.Owner = User
            if not Company and not Last_Name:
                raise forms.ValidationError('Please include a contact name or company!')
            Contact.save()
            return redirect('contact-detail', pk=Contact.uuid)
    else:
        form = generic_contact_form(instance=Contact)
    return render(request, 'contacts/edit_contact.html', {'form': form})


# Views for forms
class contacts_new_view(FormView):
    template_name = 'new_contact.html'
    form_class = generic_contact_form
    success_url = '/contact-list/'

    def form_valid(self, form):
        def contacts_new():
            return super().form_valid(form)

class contacts_edit_view(FormView):
    template_name = 'edit_contact.html'
    form_class = generic_contact_form
    success_url = '/contact-list/'

    def form_valid(self, form):
        def contacts_edit():
            return super().form_valid(form)

# Not coded yet
class contacts_delete_view(FormView):
    template_name = 'delete_contact.html'
    form_class = generic_contact_form
    success_url = 'home'

    def form_valid(self, form):
        def contacts_edit():
            return super().form_valid(form)
