from django.test import TestCase
from tp_screening.subject_screening_eligibility import SubjectScreeningEligibility
from ..models import SubjectScreening
from ..constants import YES, NO, NOT_APPLICABLE


class TestSubjectScreeningEligibility(TestCase):
    def setUp(self):
        self.subject_screening = SubjectScreening(
            age_in_years=23,
            guardian_available=NOT_APPLICABLE,
            is_citizen=YES,
            is_married_citizen=NOT_APPLICABLE,
            marriage_proof=NOT_APPLICABLE,
            is_literate=YES,
            literate_witness_avail=NOT_APPLICABLE,
            consent_ability=YES)

    def test_subject_screening_eligibility_cls_correct(self):
        """"""
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertTrue(subject_eligibility.eligible)

    def test_minor_no_guardian(self):
        """participant is a minor but no guardian"""
        self.subject_screening.age_in_years = 12
        self.subject_screening.guardian_available = NO
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_minor_guardian_not_applicable(self):
        """participant is a minor but guardian available is N/A"""
        self.subject_screening.age_in_years = 12
        self.subject_screening.guardian_available = NOT_APPLICABLE
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_not_married_proof_not_applicable(self):
        """participant is not a citizen and not married to a motswana"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = NO
        self.subject_screening.marriage_proof = NOT_APPLICABLE
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_not_married_proof_no(self):
        """participant is not a citizen and not married to a motswana"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = NO
        self.subject_screening.marriage_proof = NO
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_not_married_proof_avail(self):
        """participant is not a citizen, not married to a motswana but
           marriage documents provided"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = NO
        self.subject_screening.marriage_proof = YES
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_married_citizen_no_proof(self):
        """participant is not a citizen, married to a citizen but no proof"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = YES
        self.subject_screening.marriage_proof = NO
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_married_proof_not_applicable(self):
        """participant is not a citizen, married to a citizen but proof
           is not applicable"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = YES
        self.subject_screening.marriage_proof = NOT_APPLICABLE
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_citizen_married_citizen_proof_avail(self):
        """participant is not a citizen but married to a citizen"""
        self.subject_screening.is_citizen = NO
        self.subject_screening.is_married_citizen = YES
        self.subject_screening.marriage_proof = YES
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertTrue(subject_eligibility.eligible)

    def test_not_literate_no_literate_guardian(self):
        """Participant is not literate and does not have a literate guardian"""
        self.subject_screening.is_literate = NO
        self.subject_screening.literate_witness_avail = NO
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)

    def test_not_literate_literate_guardian_not_applicable(self):
        """Participant is not literate and does not have a literate guardian"""
        self.subject_screening.is_literate = NO
        self.subject_screening.literate_witness_avail = NOT_APPLICABLE
        subject_eligibility = SubjectScreeningEligibility(
            self.subject_screening)
        self.assertFalse(subject_eligibility.eligible)
