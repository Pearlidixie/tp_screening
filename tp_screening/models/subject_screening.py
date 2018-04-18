from django.db import models
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA


class EnrollmentChecklist():

    gender = models.CharField(
        max_length=10,
        choices=GENDER)

    is_citizen = models.CharField(
        verbose_name="Are you a Botswana citizen?",
        choices=YES_NO)

    is_married_citizen = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana citizen?",
        choices=YES_NO_NA)

    marriage_proof = models.CharField(
        verbose_name="Has the participant produced the marriage certificate, as proof?",
        choices=YES_NO_NA)

    is_literate = models.CharField(
        verbose_name="Is the participant literate?",
        choices=YES_NO)

    literate_witness_avail = models.CharField(
        verbose_name="If illeterate, is there a literate witness available?",
        choices=YES_NO_NA)

    is_minor = models.CharField(
        choices=YES_NO)

    guardian_available = models.CharField(
        verbose_name="If minor, is there a guardian available?",
        choices=YES_NO_NA)