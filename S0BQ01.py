def get_data():
    status=input("Please enter Yes if you want to continue ->")
    if status.lower()=="yes":
        print("continue")
        return True

if __name__=="__main__":
    #print("It worked")
    get_data()
