import math

def log_table1():
    for i in range(1,10):
        if i<9:
            log_value=math.log(i,10)
            print(i,"--","%.4f"%log_value)
        if i==9:
            i=i+1
            log_value=math.log(i,10)
            print(i,"--","%.4f"%log_value)

def log_table2():
    for i in range(1,100,10):
        i=i+10
        i=i-1
        log_value2=math.log(i,10)
        print(i,"--","%.4f"%log_value2)

    # number=list(range(110))
    # number2=number[10::10]
    # print(number2)

log_table1()
log_table2()
