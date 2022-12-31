# Python-NHI

A function to check strings against the New Zealand Ministry of Health NHI
Validation Routine.
Supports the old and new NHI number formats specified in
[HISO 10046:2022](https://www.health.govt.nz/publication/hiso-100462022-consumer-health-identity-standard).

## Install

```
pip install python-nhi
```

## Usage

```python
from nhi import is_nhi

print(is_nhi("WLD9413"))  # True
print(is_nhi("aDh48zj"))  # True
print(is_nhi("zzZ0044"))  # False
print(is_nhi("ZZZ00AA"))  # False
```

Checks are case-insensitive.

***Note:*** This does not check that the NHI number has been _assigned_ to
a person, it merely checks the NHI is consistent with the HISO 10046:2022
standard.

### Excluding Testcases

NHI numbers that begin with `Z` are reserved for testing.
If you wish to exclude these values, you will need to manually check for a `Z`
prefix:

```python
from nhi import is_nhi

value = "zBc42dq"

print(is_nhi(value))  # True
print(not value.upper().startswith("Z") and is_nhi(value))  # False
```

***Note:*** This does not mean that the NHI number has been _assigned_ to
a person, it just means that the NHI value is not reserved for testing.

## See Also

- https://www.health.govt.nz/publication/hiso-100462022-consumer-health-identity-standard
- https://www.health.govt.nz/our-work/health-identity/national-health-index/information-health-it-vendors-and-developers/nhi-interfaces'
