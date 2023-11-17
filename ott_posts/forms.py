from django import forms
from .models import Ott
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class OttForm(forms.ModelForm):
    class Meta:
        model = Ott
        fields = ['type', 'people', 'bill', 'description_OTT']
        labels = {
            'type': _('OTT 종류'),
            'bill' : _('총 결제 금액'),
            'people' : _('모집 인원'),
            'description_OTT' : _('상세 정보'),
        }
        widgets = {
            'type': forms.RadioSelect(choices=Ott.TYPE_CHOICES),
        }
