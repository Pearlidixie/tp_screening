from edc_constants.constants import YES, NO


class MinorEvaluator:
    """Eligible if gender is valid and female not pregnant.
    """

    def __init__(
            self, age_in_years, guardian_available, **kwargs):
        self.eligible = False
        self.reasons_ineligible = None
        if age_in_years < 18 and guardian_available == YES:
            self.eligible = True
        elif age_in_years >= 18:
            self.eligible = True
        if not self.eligible:
            self.reasons_ineligible = []
            if age_in_years < 18 and guardian_available == NO:
                self.reasons_ineligible.append(
                    'participant is a minor and no guardian is available')
            if age_in_years < 18 and guardian_available is None:
                self.reasons_ineligible.append(
                    'participant is a minor and no guardian is available')
