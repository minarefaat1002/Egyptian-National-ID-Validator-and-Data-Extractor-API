from .schemas import NationalIDResposne
from fastapi import  HTTPException
from typing import Union

# Information regarding validation and extraction of the Egyptian National ID are extracted from the following sources
#  1. https://en.wikipedia.org/wiki/Egyptian_National_Identity_Card
#  2. https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL/2dae541f02f4c5119629e8b84e907d14/9e0c551836a54a12b42bb77e183525ef.html


# ===============================
# ✅ VALIDATION AND EXTRACTION✅
# ===============================

class EgyptianNationalIDUtility:

    # =======================
    # PROVINCE CODE MAPPING#
    # =======================

    province_map = {
                '01': 'Cairo',
                '02': 'Alexandria',
                '03': 'Port Said',
                '04': 'Suez',
                '11': 'Damietta',
                '12': 'Dakahlia',
                '13': 'Ash Sharqia',
                '14': 'Kaliobeya',
                '15': 'Kafr El - Sheikh',
                '16': 'Gharbia',
                '17': 'Monoufia',
                '18': 'El Beheira',
                '19': 'Ismailia',
                '21': 'Giza',
                '22': 'Beni Suef',
                '23': 'Fayoum',
                '24': 'El Menia',
                '25': 'Assiut',
                '26': 'Sohag',
                '27': 'Qena',
                '28': 'Aswan',
                '29': 'Luxor',
                '31': 'Red Sea',
                '32': 'New Valley',
                '33': 'Matrouh',
                '34': 'North Sinai',
                '35': 'South Sinai',
                '88': 'Foreign'}

    @classmethod
    def get_governorate_name(cls, province_code: str) -> Union[str, None]:
        """
        Maps a province code to its corresponding name.

        Args:
            province_code (str): A 2-digit province code.
        
        Returns:
            str: The name of the province.
        """

        if province_code not in cls.province_map:
            raise HTTPException(status_code=400, detail="The provicded province_code is wrong.")
        return cls.province_map[province_code]

    
    @staticmethod
    def get_gender(gender_digit: str) -> str:
        """Returns gender based on the 13th digit:
        Odd for male, even for female."""

        gender_digit = int(gender_digit)
        return "Male" if gender_digit % 2 != 0 else "Female"
    
    
    @classmethod
    def get_birth_date(cls, birth_date: str) -> Union[str, None]:

        # (1-6) digits: Represent the date of birth (YYMMDD).
        birth_date_part = birth_date[1:]

        # First Digit: Denotes the century of birth, representing a span of one
        #  hundred years. Starting from 1900 to 1999 = C = 2 Starting from 2000 to 2099 = c = 3
        century_digit = int(birth_date[0])

        # determine the century  20 or 21 
        if century_digit == 2:
            birth_year = 1900 + int(birth_date_part[0:2])
        elif century_digit == 3:
            birth_year = 2000 + int(birth_date_part[0:2])
        else:
            raise HTTPException(status_code=400, detail="The provicded century digit is wrong.")

        
        birth_month = int(birth_date_part[2:4])
        birth_day = int(birth_date_part[4:6])
        return f"{birth_day}-{birth_month}-{birth_year}"
    
    
    @classmethod
    def validate(cls, national_id: str) -> Union[str, None]:
        """
        Validates and extracts information from an Egyptian National ID.

        Args:
            national_id (str): A 14-digit national ID number.

        Returns:
            dict: A dictionary containing extracted information or an error message.
        """

        # Check if the id is a 14-digit number.
        if len(national_id) != 14 or not national_id.isdigit():
            raise HTTPException(status_code=400, detail="Invalid Egyptian National ID format. It must be 14 digits.")
        
        gender = cls.get_gender(national_id[12])
        governorate = cls.get_governorate_name(national_id[7:9])
        birth_date = cls.get_birth_date(national_id[:7])

        # (9-12) digits: A number assigned by the system that is
        #  distinct for births occurring on the same day within the same province. 
        serial_number = national_id[9:13]

        # last digit: Represent a check digit or checksum. It's used
        # to validate the authenticity of the enire ID number.
        check_digit = national_id[13]

        return NationalIDResposne(
            national_id=national_id,
            birth_date=birth_date,
            gender=gender,
            governorate=governorate,
            serial_number=serial_number,
            check_digit=check_digit
        )
