from django.contrib import admin
import tp_screening


class SubjectScreeningAdmin(admin.ModelAdmin):

    radio_fields = {
        'gender': admin.VERTICAL,
        'is_citizen': admin.VERTICAL,
        'is_married_citizen': admin.VERTICAL,
        'marriage_proof': admin.VERTICAL,
        'is_literate': admin.VERTICAL,
        'literate_witness_avail': admin.VERTICAL,
        'is_minor': admin.VERTICAL,
        'guardian_available': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'gender',
                'is_citizen',
                'is_married_citizen',
                'marriage_proof',
                'is_literate',
                'literate_witness_avail',
                'is_minor',
                'guardian_available',)
        }),

    )


admin.site.register(tp_screening, SubjectScreeningAdmin)