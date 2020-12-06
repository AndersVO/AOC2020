from typing import Dict, List
import re

with open('AVO\Day4\day4_input.txt') as f:
    raw = f.read()


TEST= '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

Passport = Dict[str, str]

def make_passport(raw: str) -> Passport:
    lines = raw.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    passport = {}

    for line in lines:
        for chunk in line.split(" "):
            key, value = chunk.split(":")
            passport[key] = value

    return passport

def make_passports(raw: str) -> List[Passport]:
    chunks = raw.split("\n\n")
    return [make_passport(chunk) for chunk in chunks if chunk.strip()]

PASSPORTS = make_passports(raw)

print(PASSPORTS)
DEFAULT_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def is_valid(passport: Passport, 
             required_fields: List[str] = DEFAULT_FIELDS) -> bool:
    return all(field in passport for field in required_fields)

print(sum(is_valid(passport) for passport in PASSPORTS))


def is_valid2(passport: Passport) -> bool:
    checks = [
        1920 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        is_valid_height(passport.get('hgt', '')),
        re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r"^[0-9]{9}$", passport.get('pid', ''))
    ]

    return all(checks)

def is_valid_height(hgt: str) -> bool:
    if hgt.endswith('cm'):
        hgt = hgt.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76 
        except:
            return False

    return False

print(sum(is_valid2(passport) for passport in PASSPORTS))