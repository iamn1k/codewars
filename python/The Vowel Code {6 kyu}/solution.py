def encode(s):
    for i in range(len(s)):
        if s[i] == 'a':
            s= s.replace('a','1')
        elif s[i] == 'e':
            s = s.replace('e','2')
        elif s[i] == 'i':
            s = s.replace('i','3')
        elif s[i] == 'o':
            s = s.replace('o','4')
        elif s[i] == 'u':
            s = s.replace('u','5')
    return str(s)
        
    
def decode(s):
    for i in range(len(s)):
        if s[i] == '1':
            s= s.replace('1','a')
        elif s[i] == '2':
            s = s.replace('2','e')
        elif s[i] == '3':
            s = s.replace('3','i')
        elif s[i] == '4':
            s = s.replace('4','o')
        elif s[i] == '5':
            s = s.replace('5','u')
    return str(s)