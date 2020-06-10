def get_data():
    first_name=input("Please enter the first name->")
    last_name=input("Please enter the last name->")
    return first_name,last_name
def initials(first_name,last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    x=len(first_name)
    y=len(last_name)
    if x>y:
        z=y-1
    if x<y:
        z=x-1
    if x==y:
        z=y-1
    name=[]
    n=first_name[:-z]
    name.append(n)
    n=last_name[:-z]
    name.append(n)
    print(" ".join(name)) # join will merge two trings as a single string

def main():
    first_name,last_name=get_data()
    initials(first_name,last_name)
main()

