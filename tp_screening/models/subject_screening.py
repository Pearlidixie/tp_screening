from django.db import models
from ..choices import GENDER, YES_NO, YES_NO_NA
from _datetime import datetime


class SubjectScreening(models.Model):
    
    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=datetime.now(),
        help_text='Date and time of report.')
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER)

    is_citizen = models.CharField(
        verbose_name="Are you a Botswana citizen?",
        max_length=10,
        choices=YES_NO)

    is_married_citizen = models.CharField(
        verbose_name="If not a citizen, are you legally married to a Botswana citizen?",
        max_length=10,
        choices=YES_NO_NA)

    marriage_proof = models.CharField(
        verbose_name="Has the participant produced the marriage certificate, as proof?",
        max_length=10,
        choices=YES_NO_NA)

    is_literate = models.CharField(
        verbose_name="Is the participant literate?",
        max_length=10,
        choices=YES_NO)

    literate_witness_avail = models.CharField(
        verbose_name="If illeterate, is there a literate witness available?",
        max_length=10,
        choices=YES_NO_NA)

    is_minor = models.CharField(
        max_length=10,
        choices=YES_NO)

    guardian_available = models.CharField(
        verbose_name="If minor, is there a guardian available?",
        max_length=10,
        choices=YES_NO_NA)
