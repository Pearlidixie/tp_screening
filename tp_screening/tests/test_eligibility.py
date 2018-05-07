from django.test import TestCase
from ..constants import FEMALE, YES, NO, NOT_APPLICABLE

from ..eligibility import Eligibility


class TestEligibility(TestCase):

    def setUp(self):
        self.evaluator_criteria = dict(
            gender=FEMALE,
            age_in_years=18,
            guardian_available=NOT_APPLICABLE,
            is_citizen=YES,
            is_married_citizen=NOT_APPLICABLE,
            marriage_proof=NOT_APPLICABLE,
            is_literate=YES,
            literate_witness_avail=NOT_APPLICABLE,
            is_minor=NO)

        self.criteria = dict(
            consent_ability=True)

    def test_eligibility_ok(self):
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertTrue(obj.eligible)
        self.assertIsNone(obj.reasons_ineligible)

    def test_eligibility_not_ok_by_age_only(self):
        self.evaluator_criteria.update(age_in_years=10,
                                       guardian_available=NO)
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertFalse(obj.eligible)
        self.assertEqual(obj.reasons_ineligible, {
            'is_minor': 'participant is a minor and no'
                        ' guardian is available'})

    def test_eligibility_not_ok_by_literacy(self):
        self.evaluator_criteria.update(is_literate=NO,
                                       literate_witness_avail=NO)
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertFalse(obj.eligible)
        self.assertEqual(obj.reasons_ineligible, {
            'is_literate': 'not literate and no literate witness'})

    def test_eligibility_not_ok_by_consent_ability(self):
        self.criteria.update(consent_ability=False)
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertFalse(obj.eligible)
        self.assertEqual(obj.reasons_ineligible, {
            'consent_ability': 'Not able or unwilling to give ICF'})

    def test_eligibility_not_ok_not_citizen(self):
        self.evaluator_criteria.update(is_citizen=NO,
                                       is_married_citizen=NO)
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertFalse(obj.eligible)
        self.assertEqual(obj.reasons_ineligible, {
            'is_citizen': 'participant not a citizen and no married'
                          ' to a citizen'})
