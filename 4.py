from util import readfile

import re

DAY = 4

FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def solve_1(lines):
    buffer = set()
    n = 0
    for line in lines:
        line = line.replace("\n", "")
        if line == "":
            diff = FIELDS - buffer
            if diff == {"cid"} or diff == set():
                n += 1
            buffer = set()
        pairs = line.split(" ")
        for pair in pairs:
            key = pair.split(":")[0]
            if key:
                buffer.add(key)
    n += int((FIELDS - buffer) in ({"cid"}, set()))
    return n


HEIGHT_REGEX = re.compile(r"(([0-9]){2}in)|([0-9]{3}cm)")


def height_validator(v):
    if not v:
        return False

    if HEIGHT_REGEX.match(v):
        h, unit = v[:-2], v[-2:]
        h = int(h)
        if unit == "cm":
            return h >= 150 and h <= 193
        elif unit == "in":
            return h >= 59 and h <= 76
    return False


HCL_REGEX = re.compile(r"#[abcdef0-9]{6}")
VALID_EYE_COLORS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
PID_REGEX = re.compile(r"[0-9]{9}")

VALIDATORS = {
    "byr": lambda v: v and (len(v) == 4 and int(v) >= 1920 and int(v) <= 2002),
    "iyr": lambda v: v and (len(v) == 4 and int(v) >= 2010 and int(v) <= 2020),
    "eyr": lambda v: v and (len(v) == 4 and int(v) >= 2020 and int(v) <= 2030),
    "hgt": height_validator,
    "hcl": lambda v: v and len(v) == 7 and HCL_REGEX.match(v) is not None,
    "ecl": lambda v: v in VALID_EYE_COLORS,
    "pid": lambda v: v and len(v) == 9 and PID_REGEX.match(v) is not None,
    "cid": lambda v: True,
}


def validate_passport(passport):
    for k, validate in VALIDATORS.items():
        if not validate(passport.get(k)):
            print(f"{k} validator failed for {k} = {passport.get(k)}")
            return False
    return True


def solve_2(lines):
    data, n = {}, 0
    for line in lines:
        line = line.replace("\n", "")
        if line == "":
            n += int(validate_passport(data))
            data = {}
            continue
        pairs = line.split(" ")
        for pair in pairs:
            k, v = pair.split(":")
            data[k] = v
    n += int(validate_passport(data))
    return n


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        lines = f.readlines()
        print(solve_1(lines))
        print(solve_2(lines))
