"""
calculate percentages of marks as per user input and give the classes accordingly
"""
def prompt():
    """
    prompt user for marks scored in english,science and mathematics
    :return:
    """
    english1=int(input("what are the marks scored by you in english"))
    science1_theory=int(input("what are the marks scored by you in science theory"))
    science1_practical = int(input("what are the marks scored by you in science practical"))
    science1=science1_theory+science1_practical
    mathematics1=int(input("what are the marks scored by you in mathematics"))
    return english1, science1_theory,science1_practical,science1,mathematics1

def calculate_percentages():
    """
    input= return of function prompt
    out put= over all percenatage scored by student across all 3 subjects
    return the percentage
    """
    english1,science1_theory,science1_practical,science1,mathematics1=prompt()
    totalmarks=(english1+science1_theory+science1_practical+mathematics1)
    english=75
    s_theory=75
    s_practical=25
    science=100
    mathematics=100
    maximum=(english+s_theory+s_practical+mathematics)
    percentage = ((totalmarks)*100)/(maximum)
    return percentage,english1,science1_theory,science1_practical,science1,mathematics1

def rank():
    student_percentage,english1,science1_theory,science1_practical,science1,mathematics1=calculate_percentages()
    english_pass=25
    theory_pass=25
    practical_pass=25
    mathes_pass=35
    if english1>=english_pass and science1_theory>=theory_pass and science1_practical>=practical_pass and mathematics1>=mathes_pass:
        if student_percentage>90:
            print("Grade A")
        elif student_percentage>75 and student_percentage<=90:
            print ("Grade B")
        else:
            print("Average")
    else:
        print("Fail")
# main starts from here
rank()




