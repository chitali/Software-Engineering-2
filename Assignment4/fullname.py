def combName(fname, lname): 
    try:
        fname = str(fname)
        lname = str(lname)
    except ValueError:
         return "Error"
    if fname.isalpha() and lname.isalpha():
        return fname + " " + lname
    else:
        return "Error"