"""
calculate percentages of marks as per user input and give the classes accordingly
"""
def prompt():
    """
    import sys and use system argument variables rather than using input
    """
    english1, science1, mathematics=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    return english1,science1,mathematics

def calculate_percentages():
    """
    input= return english1,science1,mathematics from def prompt
           total marks of english,science and mathematics
    out put= over all percenatage scored by student across all 3 subjects
    return the percentage
    """
    english=80
    science=90
    mathematics=100
    marks_english,marks_science,marks_mathematics=prompt()
    percentage = ((marks_english+marks_science+marks_mathematics)*100)/(english+science+mathematics)
    return percentage

def rank():
     """
     input is percentage form calculate_percentage function
     seggrate the rank as per the instructions
     out put:print statement specifying the class student ranked into
     """
     student_percentage=calculate_percentages()
     if student_percentage>=90:
         print("Your rank is first class")
     elif student_percentage>=75 and student_percentage<90:
         print ("Your rank is second class")
     elif student_percentage<75 and student_percentage>35:
         print("Your rank is average ")
     else:
         print("You failed for this test")
# main starts from here
rank()




