def get_data():
    first_name=input("Please enter the first name->")
    last_name=input("Please enter the last name->")
    return first_name,last_name
def output(first_name,last_name):
    print("Name:",first_name.lower(),"Surname:",last_name.lower())
    print(first_name.upper(),last_name.upper())
    print("-"*20)
    print(last_name.capitalize(),",",first_name.capitalize())


def main():
    first_name,last_name=get_data()
    output(first_name,last_name)
if __name__ == '__main__':
    main()
