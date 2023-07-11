from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from . import views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, ListView, DeleteView
from .models import Donor


# Create your views here.


def home(request):
    return render(request, 'home.html')


class DonorList(ListView):
    model = Donor
    context_object_name = 'donors'
    template_name = 'list.html'


def searchorgan(request):
    return render(request, 'organ_search.html')


class SearchView(ListView):
    model = Donor
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Donor.objects.filter(
            Q(blood_group=query) | Q(organ=query)
        )


class LoginSelection(ListView):
    model = Donor
    template_name = 'all_logins.html'
    context_object_name = 'key3'


def searchprofile(request):
    return render(request, 'profile_search.html')


class SearchProfileView(ListView):
    model = Donor
    template_name = 'search2.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Donor.objects.filter(
            Q(name=query)
        )


class AddDonor(CreateView):
    model = Donor
    fields = ['name', 'age', 'gender', 'blood_group', 'organ', 'phone_no', 'place', 'status']
    success_url = reverse_lazy('successmessage')
    template_name = 'add_donor_details.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddDonor, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Donor
    fields = ['name', 'age', 'gender', 'blood_group', 'organ', 'phone_no', 'place', 'status']
    success_url = reverse_lazy('successmessage')
    template_name = 'add_donor_details.html'

class ProfileDelete(DeleteView):
       model = Donor
       fields = ['name', 'age', 'gender', 'blood_group', 'organ', 'phone_no', 'place', 'status']
       success_url = reverse_lazy('deletemessage')
       template_name = 'profiledelete.html'

def successmessage(request):
        return render(request, 'successmessage.html')


def deletemessage(request):
        return render(request, 'deletemessage.html')

