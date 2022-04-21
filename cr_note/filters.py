import django_filters
from . models import Crn
from datetime import datetime
from django_filters import DateFromToRangeFilter
from django_filters import FilterSet, filters
from django import forms
from django_filters.widgets import RangeWidget, SuffixedMultiWidget




class CRNFilter(FilterSet):


    created_at = filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD', 'type': 'date'}),label='CRN Date Between')

    class Meta:
        model = Crn

        fields = ('cr_station', 'created_at')


