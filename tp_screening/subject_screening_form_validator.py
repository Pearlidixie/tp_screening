from edc_form_validators import FormValidator
from .constants import NO, YES
from tp_screening.constants import NOT_APPLICABLE


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):

        condition = (
            self.cleaned_data.get('age_in_years') < 18)
        self.applicable_if_true(
            condition=condition, field_applicable='guardian_available')

        self.not_applicable(NOT_APPLICABLE, NO, field='is_married_citizen',
                            field_applicable='marriage_proof')

        self.not_applicable(YES, field='is_citizen',
                            field_applicable='is_married_citizen')

        self.not_applicable(NOT_APPLICABLE, NO, field='is_married_citizen',
                            field_applicable='marriage_proof')

        self.not_applicable(YES, field='is_literate',
                            field_applicable='literate_witness_avail')
