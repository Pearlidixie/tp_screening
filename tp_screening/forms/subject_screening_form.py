from ..models import SubjectScreening
from django import forms


class SubjectScreeningForm(forms.ModelForm):
    class Meta:
        model = SubjectScreening
        fields = '__all__'
