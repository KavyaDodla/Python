"""
Collect the runs scored for each ball faced by the batsman.
              A dot ball is represented by a dot in input.
              An empty line represents a wicket.

          - Find the total runs scored by the batsman
          - Find the strike rate of the batsman [ runs scored/balls faced ]
          - Find the number of balls wasted by the batsman
          - How many boundaries and sixes did he score ?"""
def data():
    runs_list=[]
    while True:
        run=(input("Please enter the runs scored by Dhoni for each ball. If it is no run enter dot. If batsman is out just click enter"))
        if run:
            runs_list.append(run)
        else:
            runs_list.append(0)
            break
    return(runs_list)

def result():
    runs_list=data()
    #calculate total runs scored
    total_runs=0
    for i in runs_list:
        if i==".":
            continue
        else:
            i=int(i)
            total_runs=total_runs+i
    print("Total runs scored by Dhoni are",total_runs)
    #Number of balls faced
    balls_faced=0
    for i in runs_list:
        if i == ".":
            balls_faced+=1
            continue
        else:
            i=int(i)
            balls_faced+=1
    print("Total balls faced by Dhoni:", balls_faced)

    #Strike rate
    strike_rate=total_runs/balls_faced
    print("The strike rate of Dhoni for this match is:",strike_rate)

    #number of  balls wasted
    dots = 0
    for i in runs_list:
        if i=="." or i=="0"
            dots+=1
    print("The number of balls wasted by Dhoni are",dots)

    #Boundaries
    fours=0
    sixes=0
    for i in runs_list:
        if i == ".":
                continue
        else:
            i=int(i)
            if i==4:
                fours+=1
            if i==6:
                sixes+=1
    print("Dhoni scored",fours,"fours and",sixes,"sixes")
    Boundaries=fours+sixes
    print("Dhoni scored",Boundaries,"boundaries in this match")
#main starts here
result()
