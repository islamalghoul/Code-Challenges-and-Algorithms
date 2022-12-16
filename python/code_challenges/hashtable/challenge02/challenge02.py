# Write here the code challenge solution
string="ASAC is a department at LTUC. ASAC teaches programming in LTUC"
def repeated_word(str):
    if not str :
        return "empty string"
    str=str.split()
    obj={}
    for i in str:
        if i in obj:
            return i
        else:
            obj[i]=i
    return "no repeated word"
print(repeated_word(string))


