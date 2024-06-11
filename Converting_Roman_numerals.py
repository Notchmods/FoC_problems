def romanToInt(s):
        Roman_numerals={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        current_number=0
        previous_number=0
        total_numbers=0
        for numerals in s[::-1]:
            current_number=Roman_numerals[numerals]
            if current_number>=previous_number:
                total_numbers+=current_number
            else:
                total_numbers-=current_number
            previous_number=Roman_numerals[numerals]
        return total_numbers
