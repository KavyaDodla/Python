"""
print first 12 even fibonacci numbers starting with 1,1
"""

def logic():
    a = 1
    b = 1
    list = []
    length=0
    while length<12:
        res=a+b
        a = b
        b = res
        if b%2==0:
            list.append(b)
            length=0
            for i in list:
                length+=1
    else:
        print(list)

logic()






