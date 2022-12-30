# Python-NHI

A function to check strings against the New Zealand Ministry of Health NHI
Validation Routine.

## Install

```
pip install python-nhi
```

## Usage

```python
from nhi import check_nhi

print(check_nhi("WLD9413"))  # True
print(check_nhi("ZZZ00AA"))  # False
```

Checks are case-insensitive

## Note

In previous revisions of HISO 10046 and the NHI validation routine there
have been inconsistencies regarding whether a checksum of 0 is invalid
in the new format. This issue has been resolved in later revisions
and a checksum of 0 in the new format is *NOT* considered invalid.

## See Also

- https://www.health.govt.nz/publication/hiso-100462022-consumer-health-identity-standard
- https://www.health.govt.nz/our-work/health-identity/national-health-index/information-health-it-vendors-and-developers/nhi-interfaces