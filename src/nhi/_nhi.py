import re
from operator import mul

_OLD_NHI_FORMAT_REGEX = re.compile(r"^[A-HJ-NP-Z]{3}\d{4}$")
_NEW_NHI_FORMAT_REGEX = re.compile(r"^[A-HJ-NP-Z]{3}\d{2}[A-HJ-NP-Z]{2}$")


def is_nhi(nhi: str) -> bool:
    """
    Checks a string against the New Zealand Ministry of Health NHI specification
    defined by HISO 10046:2023 and the NHI validation routine

    .. seealso::
        - https://www.tewhatuora.govt.nz/publications/hiso-100462023-consumer-health-identity-standard/

    :param nhi: A potential NHI string
    :return: True if the given string satisfies the New Zealand NHI Validation
        Routine and False otherwise
    """
    nhi = nhi.upper()
    if _NEW_NHI_FORMAT_REGEX.match(nhi):
        nhi_values = [_char_code(c) for c in nhi]
        checksum = sum(map(mul, nhi_values, range(7, 1, -1))) % 23
        check_digit = 23 - checksum
        return check_digit == nhi_values[-1]
    elif _OLD_NHI_FORMAT_REGEX.match(nhi):
        nhi_values = [_char_code(c) for c in nhi]
        checksum = sum(map(mul, nhi_values, range(7, 1, -1))) % 11
        check_digit = (11 - checksum) % 10
        return checksum != 0 and check_digit == nhi_values[-1]
    return False


def _char_code(c: str) -> int:
    if c.isdigit():
        return int(c)
    else:
        return ord(c) - ord('@') - ('I' < c) - ('O' < c)
