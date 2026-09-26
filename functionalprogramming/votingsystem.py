print("***********************")
print("----VOTING PROGRAM----")
print("***********************")
candidate_1 = input("Enter the first candidate name:- ")
candidate_2 = input("Enter the second candidate name:- ")
print("Sucessfully added!Voting started!")
print("----------------------------------")
print("")
ids =[]
points_1 = 0
points_2 = 0
condition = True
n =1
while condition:
    print(f"The candidates are {candidate_1} and {candidate_2}!")
    id = input(f"Enter your 3 digit id (person {n}):-")
    if len(id) >3 or len(id) <3:
        print("Id is incorrect!Try again")
    elif id in ids:
        print("Same person Can't vote twice!(same id)!")
    else:
        ids.append(id)
        candidate =input("Whom you want to cast the vote?Enter the name:-")
        if candidate == candidate_1:
            points_1+=1
        elif candidate == candidate_2:
            points_2 +=1
        else:
            print("The name you entered is not a candidate!")
        n+=1
    if n >=11:
        condition=False
    print("")

print(f"{n-1} Candidates have entered the votes!")
print("The results are compiling!")

if points_1 == points_2:
    print("It's a tie..")
elif (points_1 > points_2):
    print("{} has won! by {} points".format(candidate_1, (points_1-points_2)))
else:
    print("{} has won! by {} points".format(candidate_2, (points_2-points_1)))

