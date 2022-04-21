from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from cr_note.models import Crn
from django.urls import reverse_lazy

from django.template.response import TemplateResponse
from django.utils import timezone

from django.views import generic
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from cr_note.forms import CrnForm
from django.contrib.auth.mixins import LoginRequiredMixin


from cr_note.models import Crn
from datetime import datetime
from .filters import CRNFilter
from django_filters import DateFromToRangeFilter
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class CrnListView(LoginRequiredMixin,generic.ListView):

    model = Crn

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CRNFilter(self.request.GET, queryset=Crn.objects.order_by('-created_at')[:100])
        return context

    


@method_decorator(login_required, name='dispatch')
class CrnDetailView(LoginRequiredMixin,generic.DetailView):
    model = Crn

@method_decorator(login_required, name='dispatch')
class CreateCrnView(LoginRequiredMixin,generic.CreateView):
    login_url = '/login'
    redirect_field_name = 'cr_note/crn_detail.html'
    form_class = CrnForm
    model = Crn

@method_decorator(login_required, name='dispatch')
class CrnUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/login'
    redirect_field_name = 'cr_note/crn_detail.html'
    form_class = CrnForm
    model = Crn

@method_decorator(login_required, name='dispatch')
class CrnDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Crn
    success_url = reverse_lazy('crn_list')


@login_required
def allcrn(request):
    queryset_list = Crn.objects.order_by('-created_at')[:1000]

    context = {
        
        'crns': queryset_list ,
        
    }

    return render(request, 'cr_note/allcrn.html' ,context)
