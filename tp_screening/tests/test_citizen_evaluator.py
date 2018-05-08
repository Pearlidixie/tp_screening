from django.test import TestCase

from tp_screening.citizen_evaluator import CitizenEvaluator
from ..constants import YES, NO


class TestCitizenEvaluator(TestCase):

    def test_citizen_evaluator_citizen(self):
        """Participant is a citizen"""
        citizen_eval = CitizenEvaluator(is_citizen=YES)
        self.assertTrue(citizen_eval.eligible)

    def test_citizen_evaluator_not_citizen(self):
        """participant not a citizen"""
        citizen_eval = CitizenEvaluator(
            is_citizen=NO,
            is_married_citizen=NO,
            marriage_proof=NO)
        self.assertFalse(citizen_eval.eligible)
        citizen_eval = CitizenEvaluator(is_citizen=NO,
                                        is_married_citizen=NO,
                                        marriage_proof=YES)
        self.assertFalse(citizen_eval.eligible)
        citizen_eval = CitizenEvaluator(is_citizen=NO,
                                        is_married_citizen=YES,
                                        marriage_proof=NO)
        self.assertFalse(citizen_eval.eligible)
        citizen_eval = CitizenEvaluator(is_citizen=NO,
                                        is_married_citizen=YES,
                                        marriage_proof=YES)
        self.assertTrue(citizen_eval.eligible)
