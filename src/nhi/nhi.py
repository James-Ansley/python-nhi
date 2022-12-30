import re
from operator import mul

_OLD_NHI_FORMAT_REGEX = re.compile(r"^[A-HJ-NP-Z]{3}\d{4}$")
_NEW_NHI_FORMAT_REGEX = re.compile(r"^[A-HJ-NP-Z]{3}\d{2}[A-HJ-NP-Z]{2}$")


def check_nhi(nhi: str) -> bool:
    """
    Checks a string against the New Zealand Ministry of Health NHI specification
    defined by HISO 10046:2022 and the May 2022 V4 NHI validation routine
    .. note::
        In previous revisions of HISO 10046 and the NHI validation routine there
        have been inconsistencies regarding whether a checksum of 0 is invalid
        in the new format. This issue has been resolved in later revisions
        and a checksum of 0 in the new format is *NOT* considered invalid.
    .. seealso::
        - https://www.health.govt.nz/publication/hiso-100462022-consumer-health-identity-standard
        - https://www.health.govt.nz/our-work/health-identity/national-health-index/information-health-it-vendors-and-developers/nhi-interfaces
    :param nhi: A potential NHI string
    :return: True if the given string satisfies the New Zealand NHI Validation
        Routine and False otherwise
    """
    nhi = nhi.upper()
    matches_old = _OLD_NHI_FORMAT_REGEX.match(nhi)
    matches_new = _NEW_NHI_FORMAT_REGEX.match(nhi)

    if matches_new:
        nhi_values = [_char_code(c) for c in nhi]
        checksum = sum(map(mul, nhi_values, range(7, 1, -1))) % 24
        check_digit = 24 - checksum
        return check_digit == nhi_values[-1]
    elif matches_old:
        nhi_values = [_char_code(c) for c in nhi]
        checksum = sum(map(mul, nhi_values, range(7, 1, -1))) % 11
        check_digit = (11 - checksum) % 10
        return checksum != 0 and check_digit == nhi_values[-1]
    return False


def _char_code(c):
    if c.isdigit():
        return int(c)
    else:
        return ord(c) - ord('@') - ('I' < c) - ('O' < c)
