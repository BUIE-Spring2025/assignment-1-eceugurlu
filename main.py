def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    roman_num = [(1,"I"),(4,"IV"),(5,"V"),(9,"IX"),
                 (10,"X"),(40,"XL"),(50,"L"),(90,"XC"),(100,"C"),(400,"CD"),
                 (500,"D"),(900, "CM",(1000,"M"))]
    roman_terminal = ""
    
    for i,j  in roman_num:
        while num >= i:
            roman_terminal += j 
            num -= i
    return roman_terminal 