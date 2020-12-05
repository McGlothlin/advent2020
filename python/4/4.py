import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from common import readString, inclusiveRange


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
    passport_id: str
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

    def validate_inputs(self):
        self.validate_range(self.birth_year, 1920, 2002)
        self.validate_range(self.issue_year, 2010, 2020)
        self.validate_range(self.expiration_year, 2020, 2030)
        self.validate_height(self.height)
        self.validate_pattern(self.hair_color, re.compile(r'#[0-9a-f]{6}'))
        self.validate_eyes(self.eye_color)
        self.validate_pattern(self.passport_id, re.compile(r'^[0-9]{9}$'))

    @staticmethod
    def validate_range(number, start, end):
        try:
            if int(number) not in inclusiveRange(start, end):
                raise TypeError(f'Invalid number "{number}". Must be between {start} and {end}.')
        except ValueError:
            raise TypeError(f'Invalid number. {number} is not an integer.')

    @staticmethod
    def validate_pattern(input_str, pattern):
        """ Validates a generic pattern """
        if not pattern.match(input_str):
            raise TypeError(f'Invalid passport. {input_str} must match: {pattern}.')

    def validate_height(self, height):
        """ Height range based on units selected. """
        valid_units = ['cm', 'in']
        parsed_height = re.split(r'(\d{2}\d?)(\w{2})', height)
        try:
            assert len(parsed_height) == 4
        except AssertionError:
            raise TypeError(f'Invalid height. Expecting a number and a unit of measurement.')
        distance_value = parsed_height[1]
        distance_unit  = parsed_height[2]

        if distance_unit not in valid_units:
            raise TypeError(f'Invalid height. Must measure in cm or in.')

        if distance_unit == 'in':
            self.validate_range(distance_value, 59, 76)
        if distance_unit == 'cm':
            self.validate_range(distance_value, 150, 193)

    @staticmethod
    def validate_eyes(eye_color):
        valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if eye_color not in valid_eye_colors:
            raise TypeError(f'Invalid eye color {eye_color}. Must be one of {", ".join(valid_eye_colors)}')


class PassportParser:
    def __init__(self, validate=True):
        """ separator indicates a break between passport entries """
        self.valid_passports: List[Passport] = []
        self.invalid_passports: List[dict] = []
        self.expected_fields = 7
        self.validate = validate

    def parse_file(self, file_path):
        passport_separator = re.compile('\n{2}')  # Separates distinct passports
        field_separator = re.compile(' |\n')  # Separates fields within a single passport
        key_val_separator = re.compile(':')  # Separates the key/value pairs of a given field

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
                passport = PassportAdapter(**passport_dict)
                if self.validate:  # Part 2
                    passport.validate_inputs()
                self.valid_passports.append(passport)
            except TypeError as e:
                # This try/catch should be used with care. Could easily swallow a legitimate exception, making the
                # validation harder to debug.
                self.invalid_passports.append(passport_dict)
                # print(e)

    def get_passports(self):
        return self.valid_passports


def main():
    parser1 = PassportParser(validate=False)
    parser1.parse_file('input.txt')

    parser2 = PassportParser(validate=True)
    parser2.parse_file('input.txt')

    part1 = len(parser1.get_passports())
    part2 = len(parser2.get_passports())

    print(f'Answer 1: {part1}')
    print(f'Answer 2: {part2}')


if __name__ == '__main__':
    main()
