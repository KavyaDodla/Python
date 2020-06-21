import sys
def copy(FH1,FH2):
    all_lines=FH1.readlines()
    count=0
    for lines in all_lines:
        count+=1
        if count%2==0:
            FH2.write(lines*2)
        if count%2!=0:
            FH2.write(lines)
    FH2.write("\n"+all_lines[0])

def new_file(file):
    a=file.split(".")
    print(a)
    file2="-new.".join(a)
    print(file2)
    return file2



def main():
    file=sys.argv[1]
    file2=new_file(file)
    FH1=open(file,"r+")
    FH2=open(file2,"w")
    copy(FH1,FH2)
    FH1.close()
    FH2.close()

if __name__=="__main__":
    main()


