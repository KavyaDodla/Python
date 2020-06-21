import sys
def get_data():
    find=input("Which word should I find for->")
    replace=input("which word should I use to replace->")
    return find,replace

def find_replace(FH,find,replace):
        line=FH.readlines()
        list=[]
        #this will find match and replace each line in lists
        for i in line:
            if find in i:
                new_line=i.replace(find,replace)
                list.append(new_line)
            else:
                list.append(i)
        # this will write the entire file with new data
        FH.seek(0,0)
        for i in list:
            FH.write(i)
            FH.truncate()


def main():
    file=sys.argv[1]
    find,replace=get_data()
    FH=open(file,"r+")
    find_replace(FH,find,replace)
    FH.close()
if __name__=="__main__":
    main()

