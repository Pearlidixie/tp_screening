from ..models import SubjectScreening
from ..subject_screening_form_validator import SubjectScreeningFormValidator
from django import forms
from edc_form_validators import FormValidatorMixin


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
