def solution(digits):
    digits = int(digits)
    if(digits < 100000):
        return 0 
    elif (digits >= 10000) and (digits < 100000): 
        return digits
    else:
        digits = str(digits)   
        
        _max = str(digits[0:5])
        for i in range(len(digits) - 4):
            newMax = str(digits[i:i + 5])
            newMax = int(newMax)
            _max = int(_max)
            if newMax > _max:
                    _max = newMax
                
        return _max
        _max = str(newNumber[0:5])
        for i in range(len(newNumber) - 5):
            newMax = str(newNumber[i:i + 5])
            newMax = int(newMax)
            _max = int(_max)
            if newMax > _max:
                _max = newMax
    return _max