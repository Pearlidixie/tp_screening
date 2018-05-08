from django.test import TestCase
from edc_base.utils import get_utcnow
from copy import copy
from ..forms.subject_screening_form import SubjectScreeningForm
from ..constants import FEMALE, YES, NO, NOT_APPLICABLE


class TestSubjectScreeningForm(TestCase):

    def setUp(self):
        self.female_data = dict(
            report_datetime=get_utcnow(),
            gender=FEMALE,
            age_in_years=25,
            guardian_available=NOT_APPLICABLE,
            is_citizen=YES,
            is_married_citizen=NOT_APPLICABLE,
            marriage_proof=NOT_APPLICABLE,
            is_literate=YES,
            literate_witness_avail=NOT_APPLICABLE,
            consent_ability=YES)

    def test_default_ok(self):
        """test with default values that pass"""
        form = SubjectScreeningForm(data=self.female_data)
        form.is_valid()
        self.assertEqual(form.errors, {})
        self.assertTrue(form.save())

    def test_not_citizen_married_citizen_not_applicable(self):
        """test when a participant is not a citizen and
           is_married_citizen is not applicable"""
        data = copy(self.female_data)
        data.update(
            is_citizen=NO)
        form = SubjectScreeningForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'is_married_citizen': ['This field is applicable']})

    def test_not_citizen_married_citizen_no_documents(self):
        """test if non citizen not married to citizen and no documents"""
        data = copy(self.female_data)
        data.update(
            is_citizen=NO,
            is_married_citizen=YES)
        form = SubjectScreeningForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'marriage_proof': ['This field is applicable']})

    def test_not_married_citizen_no_documents(self):
        data = copy(self.female_data)
        data.update(
            is_citizen=NO,
            is_married_citizen=NO,
            marriage_proof=NO)
        form = SubjectScreeningForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'marriage_proof': ['This field is not applicable']})

    def test_not_literate_witness_not_applicable(self):
        data = copy(self.female_data)
        data.update(
            is_literate=NO)
        form = SubjectScreeningForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'literate_witness_avail': ['This field is'
                                                     ' applicable']})

    def test_is_minor_guardian_none(self):
        data = copy(self.female_data)
        data.update(
            age_in_years=12)
        form = SubjectScreeningForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'guardian_available': ['This field is applicable']})
