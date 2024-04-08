'''f = open("report.txt", "w")
while True:
    content = input("Enter content for the file: ")
    f.write(content)
    f.write("\n")
    ch = input("Enter 's' to continue: ")
    if ch != "s":
        break

f.close()
f1 = open("test.txt", "w")
f2 = open("report.txt", "r")
r = f2.readlines()
for line in r:
    if line[0] in "EeTt":
        f1.write(line)

f1.close()
f2.close()
def todo():
    f1 = open("swet.txt", "w")
    while True:
        content = input("Enter content for the file: ")
        f1.write(content)
        f1.write("\n")
        ch = input("Enter 's' to continue: ")
        if ch != "s":
            break
    f1.close()

    f2 = open("swet.txt", "r")
    r = f2.readlines()
    for i in r:
        i.split()
        if "to" in i and "do" in i:
            print(i)
    f2.close()

todo()

def day_of_year():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Get the first day of the year from the user
    first_day = input("Enter the first day of the year: ")

    # Validate the input
    if first_day not in days_of_week:
        print("Invalid input for the first day of the year.")
        return

    # Get the day number from the user
    day_number = int(input("Enter a day number in the range 2 to 365: "))

    # Validate the day number
    if day_number < 2 or day_number > 365:
        print("Invalid input for the day number.")
        return

    # Calculate the day of the input day number
    index = (days_of_week.index(first_day) + day_number - 1) % 7
    result_day = days_of_week[index]

    print(f"The day of day number {day_number} is {result_day}.")

day_of_year()'''

#to create a csv file movie.csv which consists of movie no
#,name rating .write routines to the files an dprint all the movie names whose ratings
# are a and b+,modify the details of the file for the entererd movie no

'''import csv

def create_csv():
    with open('movies.csv', 'w', newline='') as f:
        heading = ['Movie No', 'Name', 'Rating']
        w = csv.writer(f)
        w.writerow(heading)
        while True:
            no=input("enter movie no")
            name=input("enter name")
            rating=input("enter rating")
            w.writerow([no,name,rating])
            
            ch=input("enter s to continue")
            if ch!="s":
                break
            
create_csv()
def printing():
    with open('movies.csv', 'r', newline='') as f1:
        r=csv.reader(f1)
        for i in r:
            if i[-1]in ['a','b']:
                print(i)
printing()
import csv

def modify():
    with open('movie.csv', 'r', newline='') as f1:
        rows = list(csv.reader(f1))
        while True:
            movie_no = input("Enter movie no to be modified: ")
            name = input("Enter new name: ")
            rating = input("Enter new rating: ")
            for i in rows:
                if i[0] == movie_no:
                    i[1] = name
                    i[2] = rating

            ch = input("Enter 's' to continue o ")
            if ch.lower() != "s":
                break
        return rows

def summa():
    modified_data = modify()
    
    with open('movie.csv', 'w', newline='') as f2:
        w = csv.writer(f2)
        w.writerows(modified_data)

summa()
f=open("test.txt","r")
f1=open("swe.txt","w")
r=f.read()
print(r)
f1.write(r)
f.close()
f1.close()'''



       
         
        
        
        
    

