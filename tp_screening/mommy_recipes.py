from edc_base.utils import get_utcnow
from .constants import NOT_APPLICABLE, YES, NO, MALE
from faker import Faker
from model_mommy.recipe import Recipe

from .models import SubjectScreening

fake = Faker()

subjectscreening = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow(),
    gender=MALE,
    age_in_years=40,
    guardian_available=NOT_APPLICABLE,
    is_citizen=YES,
    is_married_citizen=NOT_APPLICABLE,
    marriage_proof=NOT_APPLICABLE,
    is_literate=YES,
    literate_witness_avail=NOT_APPLICABLE,
    consent_ability=YES)
