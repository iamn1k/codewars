def encrypt_this(text):
    words = text.split(" ")
    res = []
    for i in words:
        new = ""
        temp = ""
        for j in range(len(i)):
          if j == 0:
            new += str(ord(i[j]))
          elif j == 1:
            temp = i[j]
            new += i[-1]
          elif j == len(i) - 1:
            new += temp
          else:
            new += i[j]  
        res.append(new)
    return " ".join(list(filter(None, res))) 