def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.lstrip('#')
    answer = tuple(int(hex_string[i:i + 2], 16) for i in (0,2,4))
    return {'r' : answer[0],'g': answer[1],'b' : answer[2]}