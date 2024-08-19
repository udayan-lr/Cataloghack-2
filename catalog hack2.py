import random
data={"Andhra Pradesh": "Amaravati", "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur", "Bihar": "Patna",
    "Chhattisgarh": "Raipur", "Goa": "Panaji",
    "Gujarat": "Gandhinagar", "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla", "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru", "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal", "Maharashtra": "Mumbai",
    "Manipur": "Imphal", "Meghalaya": "Shillong",
    "Mizoram": "Aizawl", "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar", "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur", "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai", "Telangana": "Hyderabad",
    "Tripura": "Agartala", "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun", "West Bengal": "Kolkata" }

print("Welcome to GITAM School's States and Capitals Quiz competition")
print("To exit the quiz at any time enter '0'.")
points=0
for i in range(0,10):
    s,c=random.choice(list(data.items()))
    type=random.choice([0,1])
    if type==0:
        ans=input(f"\nWhat is the Capital of {s}?\nEnter your answer: ")
        if ans.strip()=='0':
            print("Thank you for playing")
            break
        elif ans.strip().lower()==c.lower():
            print("Correct answer: +1 point")
            points+=1
        else:
            print("Wrong answer: +0 points")
    else:
        ans=input(f"\n{c} is the Capital of which State?\nEnter your answer: ")
        if ans.strip()=='0':
            print("Thank you for playing")
            break
        elif ans.strip().lower()==s.lower():
            print("Correct answer: +1 point")
            points+=1
        else:
            print("Wrong answer: +0 points")
    del data[s]
print("\nYour final score:",points,"/ 10")
print("Thank you for your participation")