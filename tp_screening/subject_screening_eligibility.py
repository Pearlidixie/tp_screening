from edc_constants.constants import NORMAL, YES, NO

from .eligibility import Eligibility


def if_yes(value):
    return value == YES


def if_no(value):
    return value == NO


def if_none(value):
    return value == NO


def if_normal(value):
    return value == NORMAL


class SubjectScreeningEligibility:
    eligibility_cls = Eligibility

    def __init__(self, model_obj=None, allow_none=None):
        eligibility_obj = self.eligibility_cls(
            age_in_years=model_obj.age_in_years,
            guardian_available=model_obj.guardian_available,
            is_citizen=model_obj.is_citizen,
            is_married_citizen=model_obj.is_married_citizen,
            marriage_proof=model_obj.marriage_proof,
            is_literate=model_obj.is_literate,
            literate_witness_avail=model_obj.literate_witness_avail,
            consent_ability=model_obj.consent_ability
        )

        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
