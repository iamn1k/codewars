def make_readable(sec):
    import math
    h = math.floor(sec / 3600)
    m = math.floor((sec - (h*3600)) / 60)
    s = sec - ((math.floor(h*3600) + (math.floor(m*60))))
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    if s < 10:
        s = '0' + str(s)
    return str(h) + ':' + str(m) + ':' + str(s)