def calcVol(l, w, h):
    try:
        l = float(l)
        w = float(w)
        h = float(h)
    except ValueError:
         return "Error"
    if l >= 0 and w >= 0 and h >= 0:
        return  l * w * h
    else:
        return "Error"

        