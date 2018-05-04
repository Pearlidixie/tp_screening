from tp_screening.literacy_evaluator import LiteracyEvaluator
from tp_screening.minor_evaluator import MinorEvaluator
from tp_screening.citizen_evaluator import CitizenEvaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.

    Any key in `additional_criteria` has value True if eligible.
    """

    literacy_evaluator_cls = LiteracyEvaluator
    minor_evaluator_cls = MinorEvaluator
    citizen_evaluator_cls = CitizenEvaluator

    def __init__(self, age_in_years=None, guardian_available=None,
                 is_citizen=None, is_married_citizen=None,
                 marriage_proof=None, is_literate=None,
                 literate_witness_avail=None, **additional_criteria):

        self.criteria = dict(**additional_criteria)

        if len(self.criteria) == 0:
            raise EligibilityError('No criteria provided.')

        self.literacy_evaluator = self.literacy_evaluator_cls(
            is_literate=is_literate,
            literate_witness_avail=literate_witness_avail)

        self.minor_evaluator = self.minor_evaluator_cls(
            age_in_years=age_in_years, guardian_available=guardian_available)

        self.citizen_evaluator = self.citizen_evaluator_cls(
            is_citizen=is_citizen, is_married_citizen=is_married_citizen,
            marriage_proof=marriage_proof)

        self.criteria.update(is_literate=self.literacy_evaluator.eligible)
        self.criteria.update(is_minor=self.minor_evaluator.eligible)
        self.criteria.update(is_citizen=self.citizen_evaluator.eligible)

#       eligible if all criteria are True
        self.eligible = all([v for v in self.criteria.values()])
        if self.eligible:
            self.reasons_ineligible = None
        else:
            self.reasons_ineligible = {
                k: v for k, v in self.criteria.items() if not v}
            for k, v in self.criteria.items():
                if not v:
                    if k in self.custom_reasons_dict:
                        self.reasons_ineligible.update(
                            {k: self.custom_reasons_dict.get(k)})
                    elif k not in ['is_literate', 'is_citizen', 'is_minor']:
                        self.reasons_ineligible.update({k: k})
            if not self.literacy_evaluator.eligible:
                self.reasons_ineligible.update(
                    is_literate=f"{' and '.join(self.literacy_evaluator.reasons_ineligible)}.")
            if not self.citizen_evaluator.eligible:
                self.reasons_ineligible.update(
                    is_citizen=f"{' and '.join(self.citizen_evaluator.reasons_ineligible)}.")
            if not self.minor_evaluator.eligible:
                self.reasons_ineligible.update(
                    is_minor=f"{' and '.join(self.minor_evaluator.reasons_ineligible)}.")

    def __str__(self):
        return self.eligible

    @property
    def custom_reasons_dict(self):
        """Returns a dictionary of custom reasons for named criteria.
        """
        custom_reasons_dict = dict(
            consent_ability='Not able or unwilling to give ICF.',
            is_literate='Participant should be literate'
                        ' or have literate guardian')
        for k in custom_reasons_dict:
            if k in custom_reasons_dict and k not in self.criteria:
                raise EligibilityError(
                    f'Custom reasons refer to'
                    ' invalid named criteria, Got \'{k}\'. '
                    f'Expected one of {list(self.criteria)}. '
                    f'See {repr(self)}.')
        return custom_reasons_dict
