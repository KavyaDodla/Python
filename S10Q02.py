import sys
def count_character(FH,search_term):
    all_lines=FH.readlines()
    count=0
    x=0
    for i in all_lines:
        count=count+1
        occurences=i.count(search_term)
        if occurences>x:
            x=occurences
            print("The sentences that has maximum occurences of",search_term,"is->",all_lines[(count-1)])

def main():
    filename=sys.argv[1]
    search_term=sys.argv[2]
    with open(filename,'r') as FH:
        count_character(FH,search_term)

if __name__=="__main__":
    main()



