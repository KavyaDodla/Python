import sys
def text(FH1,FH2):
    text1=FH1.readlines()
    list=[]
    print(text1)
    for i in text1:
        line=i.split(".")
        #print(line)
        for i in line:
            if i!="\n":
                list.append("\n"+i+".")
    return list
def override(list,FH2):
    for i in list:
        FH2.write(i)


def main():
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    FH1=open(filename1,'r')
    FH2=open(filename2,'a')
    list=text(FH1,FH2)
    override(list,FH2)
    FH1.close()
    FH2.close()

if __name__=="__main__":
    main()



