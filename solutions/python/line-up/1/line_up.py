def line_up(name, number):
    ordinal_num = "th"
    num_list = list(str(number))
    
    if num_list[-1] == "1":
        ordinal_num = "th" if len(num_list) > 1 and num_list[-2] == "1" else "st"
    if num_list[-1] == "2":
        ordinal_num = "th" if len(num_list) > 1 and num_list[-2] == "1" else "nd"
    if num_list[-1] == "3":
        ordinal_num = "th" if len(num_list) > 1 and num_list[-2] == "1" else "rd"
        
    return f"{name}, you are the {number}{ordinal_num} customer we serve today. Thank you!"
