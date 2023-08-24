import string
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
        self.assertTrue(is_nhi("ZBN77VL"))
        self.assertTrue(is_nhi("ZZZ00AC"))
        self.assertTrue(is_nhi("ZDR69YX"))
        self.assertTrue(is_nhi("ZSC21TN"))
        self.assertTrue(is_nhi("ZZB30NH"))
        self.assertTrue(is_nhi("ZYZ81ZV"))
        self.assertTrue(is_nhi("ZVB97XQ"))
        self.assertTrue(is_nhi("ZRA29VA"))
        self.assertTrue(is_nhi("ZYX61YS"))

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

        # Needs a check character of V
        for c in string.ascii_uppercase:
            if c != "V":
                with self.subTest(c=c):
                    self.assertFalse(is_nhi(f"ZHW58C{c}"))

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
        self.assertTrue(is_nhi("zZz00aC"))
        self.assertTrue(is_nhi("zDr69yX"))
        self.assertTrue(is_nhi("zSc21tN"))
        self.assertTrue(is_nhi("zZb30nH"))
        self.assertTrue(is_nhi("zYz81Zv"))
        self.assertTrue(is_nhi("zVb97Xq"))
        self.assertTrue(is_nhi("zRa29Va"))
        self.assertTrue(is_nhi("zYx61Ys"))

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
