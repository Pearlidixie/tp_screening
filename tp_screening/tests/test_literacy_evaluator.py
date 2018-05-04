from django.test import TestCase

from tp_screening.literacy_evaluator import LiteracyEvaluator
from edc_constants.constants import YES, NO


class TestLiteracyEvaluator(TestCase):

    def test_literacy_evaluator_literate(self):
        """Participant is literate"""
        literacy_eval = LiteracyEvaluator(is_literate=YES)
        self.assertTrue(literacy_eval.eligible)

    def test_not_literate_no_literate_witness(self):
        """participant not literate and no literate witness available"""
        literacy_eval = LiteracyEvaluator(is_literate=NO,
                                          literate_witness_avail=NO)
        self.assertFalse(literacy_eval.eligible)

    def test_not_literate_literate_witness_none(self):
        """Participant not literate and literate witness is None"""
        literacy_eval = LiteracyEvaluator(is_literate=NO,
                                          literate_witness_avail=None)
        self.assertFalse(literacy_eval.eligible)

    def test_not_literate_witness_available(self):
        """Participant is not literate but literate witness available"""
        literacy_eval = LiteracyEvaluator(is_literate=NO,
                                          literate_witness_avail=YES)
        self.assertTrue(literacy_eval.eligible)
