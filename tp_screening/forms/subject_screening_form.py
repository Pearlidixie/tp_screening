from ..models import SubjectScreening
from django import forms
from tp_subject_form_validators.form_validators.subject_screening import SubjectScreeningFormValidator
from edc_form_validators import FormValidatorMixin


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
