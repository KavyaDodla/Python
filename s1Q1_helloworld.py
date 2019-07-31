"""
prompt for user’s name and then wish the user by saying Hello followed by his name
"""
def get_user_name():
    """
        Prompt the user to enter his name
        Input : None
        Output : Return the user input as a string
        """
    Name=str(input("Please enter your name"))
    return Name
def say_hello(user):
    """
    Say hello to the user
    Input: Name from function (get_user_name)=user
    Output:print hello to the user
    """
    print("Hello", user, "!!!")
def main():
    """
    Main function of the program
    """
    user=get_user_name()
    say_hello(user)
#main starts from here
main()
