import sys
def text_match(FH,search_term):
    all_lines=FH.readlines()
    for i in all_lines:
        occurences=i.count(search_term)
        if occurences>0:
            print("The line that has",search_term,"is->",i)
def main():
    filename=sys.argv[1]
    search_term=sys.argv[2]
    with open(filename,'r') as FH:
        text_match(FH,search_term)

if __name__=="__main__":
    main()

