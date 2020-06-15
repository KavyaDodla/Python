def get_data():
    sentence=input("Please enter the text->")
    search=input("Which word should I search for->")
    new=input("which word should I use to replace->")
    return sentence,search,new
def search():
    sentence,search,new=get_data()
    if search in sentence:
        sentence2=sentence.replace(search,new)
    print (sentence2)
search()





