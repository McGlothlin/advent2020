import re
from dataclasses import dataclass
from typing import Optional, List, Dict
from common import readString


@dataclass
class Passport:
    """ Represents a passport.

        Input for this problem contains unfriendly field names which have been mapped as an alias.
    """
    birth_year: int
    issue_year: int
    expiration_year: int
    height: str
    hair_color: str
    eye_color: str
    passport_id: int
    country_id: Optional[int]


@dataclass
class PassportAdapter(Passport):
    """ Our text file has some strange names for common fields.

        Populate our passport values using an alias.
    """

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.birth_year = byr
        self.issue_year = iyr
        self.expiration_year = eyr
        self.height = hgt
        self.hair_color = hcl
        self.eye_color = ecl
        self.passport_id = pid
        self.country_id = cid

    # def __init__(self):
    #     try:
    #         super().__init__(**kwargs)
    #     except TypeError as e:
    #         if

    # aliases = {
    #     'byr': 'birth_year',
    #     'iyr': 'issue_year',
    #     'eyr': 'expiration_year',
    #     'hgt': 'height',
    #     'hcl': 'hair_color',
    #     'ecl': 'eye_color',
    #     'pid': 'passport_id',
    #     'cid': 'country_id'
    # }
    #
    #
    # def __getattr__(self, attr):
    #     if attr in self.aliases:
    #         getattr(self, self.aliases.get(attr))
    #
    #
    # def __setattr__(self, key, value):
    #     try:
    #         super().__setattr__(key, value)
    #     except AttributeError:
    #         setattr(self, self.aliases[key], value)


class PassportParser:
    def __init__(self):
        """ separator indicates a break between passport entries """
        self.valid_passports: List[Passport] = []
        self.invalid_passports: List[dict] = []


    def parse_file(self, file_path):
        passport_separator = re.compile('\n{2}')
        field_separator = re.compile(' |\n')
        key_val_separator = re.compile(':')

        input_string = readString(file_path)
        input_list = re.split(passport_separator, input_string)

        for passport_string in input_list:
            field_list = re.split(field_separator, passport_string)
            passport_dict = {}
            for field in field_list:
                if not field:
                    # bug in parsing causes empty string
                    continue
                key, value = re.split(key_val_separator, field)
                passport_dict[key] = value
            try:
                self.valid_passports.append(PassportAdapter(**passport_dict))
            except TypeError:
                # print(f'Invalid passport spec: {passport_dict}')
                self.invalid_passports.append(passport_dict)


    def get_passports(self):
        return self.valid_passports


def main():
    parser = PassportParser()
    parser.parse_file('input.txt')

    part1 = len(parser.get_passports())
    # part2 = treesHit(1, 1) * treesHit(3, 1) * treesHit(5, 1) * treesHit(7, 1) * treesHit(1, 2)

    print(f'Answer 1: {part1}')
    # print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
