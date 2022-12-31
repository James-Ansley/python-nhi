import unittest
from nhi import is_nhi


class TestCheckNHI(unittest.TestCase):
    def test_valid_old_format_NHI_number(self):
        self.assertTrue(is_nhi("JBX3656"))
        self.assertTrue(is_nhi("ZZZ0016"))
        self.assertTrue(is_nhi("ZZZ0024"))
        self.assertTrue(is_nhi("ZAA0067"))
        self.assertTrue(is_nhi("ZAA0075"))
        self.assertTrue(is_nhi("ZAA0083"))
        self.assertTrue(is_nhi("ZAA0091"))
        self.assertTrue(is_nhi("ZAA0105"))
        self.assertTrue(is_nhi("ZAA0113"))
        self.assertTrue(is_nhi("ZAA0121"))
        self.assertTrue(is_nhi("ZAA0130"))
        self.assertTrue(is_nhi("ZAA0148"))
        self.assertTrue(is_nhi("ZAA0156"))
        self.assertTrue(is_nhi("ZAC5361"))

    def test_valid_new_format_NHI_number(self):
        self.assertTrue(is_nhi("ZVU27KZ"))
        self.assertTrue(is_nhi("ALU18KZ"))
        self.assertTrue(is_nhi("AUL78CF"))
        self.assertTrue(is_nhi("ARM79XB"))
        self.assertTrue(is_nhi("ATD33RD"))
        self.assertTrue(is_nhi("ADH48ZJ"))
        self.assertTrue(is_nhi("ZBC42DQ"))
        self.assertTrue(is_nhi("ZZZ00AX"))
        self.assertTrue(is_nhi("ZGT56KB"))
        self.assertTrue(is_nhi("ZHS91BR"))
        self.assertTrue(is_nhi("ZHW58CN"))
        self.assertTrue(is_nhi("ZLV86AX"))

    def test_no_digit_can_be_added_to_an_old_format_NHI_with_a_checksum_of_0_to_make_it_valid(self):
        for i in range(10):
            with self.subTest(i=i):
                self.assertFalse(is_nhi(f"ZZZ004{i}"))

    def test_invalid_old_format_NHI_numbers(self):
        self.assertFalse(is_nhi("ZZZ0044"))
        self.assertFalse(is_nhi("ZZZ0017"))
        self.assertFalse(is_nhi("DAB8233"))

        # Needs a checkdigit of 6
        self.assertFalse(is_nhi("JBX3650"))
        self.assertFalse(is_nhi("JBX3651"))
        self.assertFalse(is_nhi("JBX3652"))
        self.assertFalse(is_nhi("JBX3653"))
        self.assertFalse(is_nhi("JBX3654"))
        self.assertFalse(is_nhi("JBX3655"))
        self.assertFalse(is_nhi("JBX3657"))
        self.assertFalse(is_nhi("JBX3658"))
        self.assertFalse(is_nhi("JBX3659"))

    def test_invalid_new_format_NHI_numbers(self):
        self.assertFalse(is_nhi("ZZZ00AA"))
        self.assertFalse(is_nhi("ZZZ00AY"))
        self.assertFalse(is_nhi("ZVU27KY"))
        self.assertFalse(is_nhi("ZVU27KA"))
        self.assertFalse(is_nhi("ZHW58CZ"))

    def test_random_strings_are_invalid(self):
        self.assertFalse(is_nhi("not an NHI"))
        self.assertFalse(is_nhi("!@#$%&*"))
        self.assertFalse(is_nhi("AAANNNC"))
        self.assertFalse(is_nhi("AAANNAC"))
        self.assertFalse(is_nhi("ZVU27K"))
        self.assertFalse(is_nhi("JBX365"))

    def test_is_nhi_is_case_insensitive(self):
        # Valid Cases
        self.assertTrue(is_nhi("jBx3656"))
        self.assertTrue(is_nhi("zZz0016"))
        self.assertTrue(is_nhi("zZz0024"))
        self.assertTrue(is_nhi("zAa0067"))
        self.assertTrue(is_nhi("zAa0075"))
        self.assertTrue(is_nhi("zAa0083"))
        self.assertTrue(is_nhi("zAa0091"))
        self.assertTrue(is_nhi("zAa0105"))
        self.assertTrue(is_nhi("zAa0113"))
        self.assertTrue(is_nhi("zAa0121"))
        self.assertTrue(is_nhi("zAa0130"))
        self.assertTrue(is_nhi("zAa0148"))
        self.assertTrue(is_nhi("zAa0156"))
        self.assertTrue(is_nhi("zAc5361"))
        self.assertTrue(is_nhi("zVu27kz"))
        self.assertTrue(is_nhi("aLu18kz"))
        self.assertTrue(is_nhi("aUl78cf"))
        self.assertTrue(is_nhi("aRm79xb"))
        self.assertTrue(is_nhi("aTd33rd"))
        self.assertTrue(is_nhi("aDh48zj"))
        self.assertTrue(is_nhi("zBc42dq"))
        self.assertTrue(is_nhi("zZz00ax"))
        self.assertTrue(is_nhi("zGt56kb"))
        self.assertTrue(is_nhi("zHs91br"))
        self.assertTrue(is_nhi("zHw58cn"))
        self.assertTrue(is_nhi("zLv86ax"))

        # Invalid cases
        self.assertFalse(is_nhi("zzZ0044"))
        self.assertFalse(is_nhi("zzZ0017"))
        self.assertFalse(is_nhi("daB8233"))
        self.assertFalse(is_nhi("jbX3650"))
        self.assertFalse(is_nhi("jbX3651"))
        self.assertFalse(is_nhi("jbX3652"))
        self.assertFalse(is_nhi("jbX3653"))
        self.assertFalse(is_nhi("jbX3654"))
        self.assertFalse(is_nhi("jbX3655"))
        self.assertFalse(is_nhi("jbX3657"))
        self.assertFalse(is_nhi("jbX3658"))
        self.assertFalse(is_nhi("jbX3659"))
        self.assertFalse(is_nhi("zzZ00aa"))
        self.assertFalse(is_nhi("zzZ00ay"))
        self.assertFalse(is_nhi("zvU27ky"))
        self.assertFalse(is_nhi("zvU27ka"))
        self.assertFalse(is_nhi("zhW58cz"))


if __name__ == '__main__':
    unittest.main()
