from edc_constants.constants import YES, NO


class LiteracyEvaluator:
    """Eligible if gender is valid and female not pregnant.
    """

    def __init__(
            self, is_literate=None, literate_witness_avail=None, **kwargs):
        self.eligible = False
        self.reasons_ineligible = None
        if is_literate == NO and literate_witness_avail == YES:
            self.eligible = True
        elif is_literate == YES:
            self.eligible = True
        if not self.eligible:
            self.reasons_ineligible = []
            if is_literate == NO and literate_witness_avail == NO:
                self.reasons_ineligible.append(
                    'not literate and no literate witness')
            if is_literate == NO and literate_witness_avail is None:
                self.reasons_ineligible.append(
                    'not literate and literate witness'
                    'should be provided')
