import re

raw_data = open('04_input').read()


def text_line_to_dict(in_line):
    key_val_txts = in_line.split(" ")
    out_dict = {}
    for kv in key_val_txts:
        k, v = kv.split(":")
        out_dict[k] = v
    return out_dict


passports_lines = map(lambda pp: pp.replace("\n", " "), raw_data.split("\n\n"))
passport_dicts = list(map(lambda pp: text_line_to_dict(pp), passports_lines))


def valid_passport_p1(pp_dict):
    return all([
        'byr' in pp_dict,
        'iyr' in pp_dict,
        'eyr' in pp_dict,
        'hgt' in pp_dict,
        'hcl' in pp_dict,
        'ecl' in pp_dict,
        'pid' in pp_dict
    ])


def valid_byr(pp_dict):
    if 'byr' in pp_dict:
        if re.match(r"^\d{4}$", pp_dict['byr']):
            if 1920 <= int(pp_dict['byr']) <= 2002:
                return True
    return False


def valid_iyr(pp_dict):
    if 'iyr' in pp_dict:
        if re.match(r"^\d{4}$", pp_dict['iyr']):
            if 2010 <= int(pp_dict['iyr']) <= 2020:
                return True
    return False


def valid_eyr(pp_dict):
    if 'eyr' in pp_dict:
        if re.match(r"^\d{4}$", pp_dict['eyr']):
            if 2020 <= int(pp_dict['eyr']) <= 2030:
                return True
    return False


def valid_hgt(pp_dict):
    if 'hgt' in pp_dict:
        if re.match(r"^\d+(cm|in)$", pp_dict['hgt']):
            if pp_dict['hgt'][-2:] == 'in':
                if 59 <= int(pp_dict['hgt'][0:-2]) <= 76:
                    return True
            elif pp_dict['hgt'][-2:] == 'cm':
                if 150 <= int(pp_dict['hgt'][0:-2]) <= 193:
                    return True
    return False


def valid_hcl(pp_dict):
    if 'hcl' in pp_dict:
        if re.match(r"^#[0-9a-f]{6}$", pp_dict['hcl']):
            return True
    return False


def valid_ecl(pp_dict):
    if 'ecl' in pp_dict:
        if pp_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    return False


def valid_pid(pp_dict):
    if 'pid' in pp_dict:
        if re.match(r"^\d{9}$", pp_dict['pid']):
            return True
    return False


def valid_passport_p2(pp_dict):
    if valid_passport_p1(pp_dict):
        return all([
            valid_byr(pp_dict),
            valid_iyr(pp_dict),
            valid_eyr(pp_dict),
            valid_hgt(pp_dict),
            valid_hcl(pp_dict),
            valid_ecl(pp_dict),
            valid_pid(pp_dict),
        ])
    else:
        return False


print("Part 1: ", len(list(filter(lambda pp: valid_passport_p1(pp), passport_dicts))))
print("Part 2: ", len(list(filter(lambda pp: valid_passport_p2(pp), passport_dicts))))
