from django.test import TestCase

from tp_screening.minor_evaluator import MinorEvaluator
from edc_constants.constants import YES, NO


class TestMinorEvaluator(TestCase):

    def test_not_minor(self):
        """Participant is not a minor"""
        minor_eval = MinorEvaluator(age_in_years=18,
                                    guardian_available=None)
        self.assertTrue(minor_eval.eligible)

    def test_minor_no_guardian(self):
        """Participant is Minor but no guardian"""
        minor_eval = MinorEvaluator(age_in_years=17,
                                    guardian_available=NO)
        self.assertFalse(minor_eval.eligible)

    def test_minor_guardian_none(self):
        """Participant is Minor but no guardian"""
        minor_eval = MinorEvaluator(age_in_years=17,
                                    guardian_available=None)
        self.assertFalse(minor_eval.eligible)

    def test_minor_guardian_avail(self):
        """Participant is Minor guardian available"""
        minor_eval = MinorEvaluator(age_in_years=17,
                                    guardian_available=YES)
        self.assertTrue(minor_eval.eligible)



