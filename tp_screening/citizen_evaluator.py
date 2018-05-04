from edc_constants.constants import YES, NO


class CitizenEvaluator:
    """Evaluates eligibility based on citizenship
    """

    def __init__(
            self, is_citizen=None,
            is_married_citizen=None, marriage_proof=None, **kwargs):
        self.eligible = False
        self.reasons_ineligible = None
        if is_citizen == YES:
            self.eligible = True
        elif is_citizen == NO and is_married_citizen == YES:
            if marriage_proof == YES:
                self.eligible = True
        if not self.eligible:
            self.reasons_ineligible = []
            if(is_citizen == NO and is_married_citizen == NO
               and marriage_proof == NO):
                self.reasons_ineligible.append(
                    'participant must be a citizen or '
                    'married to a citizen and have proof of marriage')
            if(is_citizen == NO and is_married_citizen == NO
               and marriage_proof == YES):
                self.reasons_ineligible.append(
                    'participant must be a citizen or '
                    'married to a citizen and have proof of marriage'
                    ' to a motswana citizen')
