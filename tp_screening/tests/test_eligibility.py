from copy import copy
from django.test import TestCase, tag
from edc_constants.constants import FEMALE, YES, NO, NOT_APPLICABLE

from ..eligibility import Eligibility, EligibilityError


class TestEligibility(TestCase):

    def setUp(self):
        self.evaluator_criteria = dict(
            age=18,
            gender=FEMALE,
            is_citizen=YES,
            is_married_citizen=NO,
            marriage_proof=NOT_APPLICABLE,
            is_literate=YES,
            literate_witness_avail=NOT_APPLICABLE,
            is_minor=NO,
            guardian_available=NOT_APPLICABLE,
            allow_none=True)

        self.criteria = dict(
            consent_ability=True)

#     def test_eligibility_ok(self):
#         obj = Eligibility(**self.evaluator_criteria, **self.criteria)
#         self.assertTrue(obj.eligible)
#         self.assertIsNone(obj.reasons_ineligible)
# 
#     def test_eligibility_not_ok_by_age_only(self):
#         self.evaluator_criteria.update(age=10)
#         obj = Eligibility(**self.evaluator_criteria, **self.criteria)
#         self.assertFalse(obj.eligible)
#         self.assertEqual(obj.reasons_ineligible, {'age': 'age<18.'})
