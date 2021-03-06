from django.contrib import admin
from tp_screening.models.subject_screening import SubjectScreening
from tp_screening.forms.subject_screening_form import SubjectScreeningForm


class SubjectScreeningAdmin(admin.ModelAdmin):
    form = SubjectScreeningForm

    radio_fields = {
        'gender': admin.VERTICAL,
        'is_citizen': admin.VERTICAL,
        'is_married_citizen': admin.VERTICAL,
        'marriage_proof': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'literate_witness_avail': admin.VERTICAL,
        'guardian_available': admin.VERTICAL,
        'consent_ability': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'gender',
                'age_in_years',
                'guardian_available',
                'is_citizen',
                'is_married_citizen',
                'marriage_proof',
                'is_literate',
                'literate_witness_avail',
                'consent_ability')
        }),

    )
    list_display = ['screening_identifier', 'gender', 'age_in_years',
                    'eligible', 'reasons_ineligible']


admin.site.register(SubjectScreening, SubjectScreeningAdmin)
