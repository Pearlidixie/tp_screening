from django.db import models
from ..choices import GENDER, YES_NO, YES_NO_NA
from _datetime import datetime
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.sites.site_model_mixin import SiteModelMixin
from ..subject_screening_eligibility import SubjectScreeningEligibility
from tp_screening.identifiers import ScreeningIdentifier


class SubjectScreening(SiteModelMixin, BaseUuidModel):

    """SubjectScreeningEligibility is a class"""
    eligibility_cls = SubjectScreeningEligibility

    """ScreeningIdentifier is a class that creates a screening identifier"""
    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name='Screening ID',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=datetime.now(),
        help_text='Date and time of report.')

    gender = models.CharField(
        max_length=20,
        choices=GENDER)

    age_in_years = models.IntegerField(
        default=None
        )

    is_citizen = models.CharField(
        verbose_name="Are you a Botswana citizen?",
        max_length=20,
        choices=YES_NO)

    is_married_citizen = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana citizen?",
        max_length=20,
        choices=YES_NO,
        blank=True,
        null=True,
        help_text='Applies only to non citizens')

    marriage_proof = models.CharField(
        verbose_name="Has the participant produced the marriage certificate, as proof?",
        max_length=20,
        choices=YES_NO,
        blank=True,
        null=True,
        help_text='Applies only to non citizens')

    is_literate = models.CharField(
        verbose_name="Is the participant literate?",
        max_length=20,
        choices=YES_NO)

    literate_witness_avail = models.CharField(
        verbose_name="If illiterate, is there a literate witness available?",
        max_length=20,
        choices=YES_NO,
        blank=True,
        null=True,
        help_text='Applies only to participants that are not literate')

    guardian_available = models.CharField(
        verbose_name="If minor, is there a guardian available?",
        max_length=20,
        choices=YES_NO,
        blank=True,
        null=True,
        help_text='Applies only to minors')

    consent_ability = models.CharField(
        verbose_name='Participant or legal guardian/representative able and '
                     'willing to give informed consent.',
        max_length=5,
        default=None,
        choices=YES_NO,
        null=True)

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name='Reason not eligible',
        max_length=150,
        null=True,
        editable=False)

    consented = models.BooleanField(
        default=False,
        editable=False)

    """Customize how the model will be referenced. What will show up when 
       the save button is pressed instead of having modelObject as the
       name of the saved object"""
    def __str__(self):
        return (f'{self.screening_identifier} {self.gender} {self.age_in_years}')

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(model_obj=self, allow_none=True)
        self.eligible = eligibility_obj.eligible #either true or false
        if not self.eligible:
            reasons_ineligible = [
                v for v in eligibility_obj.reasons_ineligible.values() if v]
            reasons_ineligible.sort()
            self.reasons_ineligible = ','.join(reasons_ineligible)
        else:
            self.reasons_ineligible = None
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        return ['screening_identifier', 'subject_identifier', 'reference']
