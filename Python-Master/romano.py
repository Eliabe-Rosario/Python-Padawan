def roman_to_int(s, total=0, prev_value=0):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not s:
        return total

    value = roman_dict[s[-1]]
    if value < prev_value:
        total -= value
    else:
        total += value
    
    return roman_to_int(s[:-1], total, value)


print(roman_to_int("III"))    
print(roman_to_int("LVIII"))  
print("São os números inseridos")