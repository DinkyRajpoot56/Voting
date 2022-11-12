import sqlite3
con = sqlite3.connect("Election.db")
cur = con.cursor()
def Verify(Voter_id):
    print("Verifying.....")
    cur.execute("SELECT Voter_id,Nom_Voter_id from Voter,Nominee")
    rows = cur.fetchall()
    a=[]
    for x in  rows:
        a.append(rows[0])
        a.append(rows[1])
        if Voter_id in set[a]:
            return True
        else:
            return False
        ##Calculate Age:
from datetime import date
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
def addVoter():
    Voter_id =int(input("Enter voter_ID: "))
    if len(str(Voter_id))!=6:
        print("Invalid Please Enter valid Voter_Id:")
        return
    if Verify(Voter_id)==True:
        print("Data already present")
        return
    Voter_Name = input("Enter your Name:")
    Voter_Location=input("Enter Your Location:")
    DOB = input("Enter your DOB in YY-MM-DD format:")
    yyyy,mm,dd=map(int,DOB.split("-"))
    DOB=date(yyyy,mm,dd)
    if calculateAge(date(yyyy,mm,dd))<10:
        print("under age to Vote!")
        return
    cur.execute("INSERT INTO Voter Values(?,?,?,?)", (Voter_id,Voter_Name,Voter_Location,DOB))
    con.commit()
    print("Data Inserted in Voter-List")
    return
     
    
    def updateVoter():
        Voter_id =input("Enter your Voter_ID")
        if len(Voter_id)!=0:
            print("Invalid Please Enter 6-digit valid Voter_ID")
            return
        if Verify(Voter_id)==False:
            Voter_Name = input("Enter your New Voter_Name: ")
            Voter_Location=input("Enter your new location: ")
            cur.execute("UPDATE Voter SET Voter_Name=?, Voter_Location=?", (Voter_Name,Voter_Location,Voter_id)
            con.commit()
            print("Data updated successfully!")
            return
        else:
            print("Please Add Voter First")
            return
        
                        
        def addNominee():
            Nom_Voter_id =int(input("Enter Voter_ID: "))
            if len(str(Nom_Voter_id))!=6:
                        print("Invalid please enter valid Nom_Voter_ID")
                        return
            if Verify(Nom__id)==True:
                        print("Data already present")
                        return
            Nom_Name = input("Enter your Name: ")
            Nom_Location = input("Enter your location: ")
            DOB = input("Enter your DOB in YY-MM-DD format: ")
            yyyy,mm,dd=map(int,DOB.split("-"))
            DOB=date(yyyy,mm,dd)
            if calculateAge(date(yyyy,mm,dd))<20:
                        print("Under age to Nominate")
                        return
            cur.execute("INSERT INTO Nominee VALUES (?, ?, ?, ?)", (Nom_Voter_id,Nom_Name,Nom_Location,DOB))
            con.commit()
            Print("Data Inserted in Nominee-List")
            return
                        
                        
                        
        def updateNominee():
            Nom_Voter_id =input("Enter your Nom_Voter_ID: ") 
            if len(Nom_Voter_id)!=6:
                print("Invalid Please Enter6_digits valid Nom_Name: ")https://github.com/DinkyRajpoot56/CalorieTracker/tree/CalorieTrackeru
                return
            if verify(Nom_Voter_id)==False:
                Nom_Name = input("Enter your New Nom_Name: ")
                Nom_Location=input("Enter your new Location: ")
                cur.execute("UPDATE Nominee SET Nom_Name=?, Nom_Location=? WHERE Nom_Voter_id=?", (Nom_Name,Nom_Location,Nom_Voter_id))
                con.commit()
                print("Data updated successfully!")
                return
            else:
                print("Please Add nominee First!")
                return
                        
                        
                        
        def seeResult():
            cur.execute("SELECT * FROM Voter")
            rows = cur.fetchall()
            print("Total Vote Count is: ",len(rows))
            print("Nominee Name | Total Votes")
            Ll=[]
            for row in cur.execute("Select n.Nom_name,count(v.Nom_id) from Nominee n left join Voting_Details v on(n,Nom_Voter_id)")
                print(row[0]," | ",row[1])
                Ll(row[0]=row[1])
            v = list(Ll.values())
            k = list(Ll.keys())
            print("Winner: ",k[v.index(max(v))])
            return
                        
         
                        
        def ViewVoter_Details():
            cur.execute("select * from Voting_Details")
            rows = cur.fetchall()
            return rows
        def ViewVoter_():
            cur.execute("select * from Voter")
            rows = cur.fetchall()
            
            return rows
                        
                        
        def ViewNominee():
            cur.execute("select * from Nominee")
            rows = cur.fetchall()
            return rows
                        
                        
        def download():
            import cav
            h=['Voter_ID', 'Nominee_ID','Voting_Time']
            cur.execute("select * from Voting_Details")
            x = cur.fetchall()
            with open('Voting.cav','w') as f:
                w=cav.writer(f)
                w.writerow(h)
                for i in x:
                    w.writerow(i)
                print("Download! To see open C:/Drive/user & file name as Voting.cav ")
                return
        
                        
                        
        def validate(id):
            cur.execute('SELECT Voter_ID from Voter where Voter_ID=[]',format(id))
            x=cur.fetchall()
            for row in x:
                print(row)
                if id not in row:
                    print("User not voted")
                    return True
                elif id in row:
                    print("User already voted")
                    return False
            print("Enter valid Voter_ID")
            return False
                        
                        
  def welcome():
    print("-------------------")
    print("Welcome to E-voting System ")
    print("-------------------")
    flag = True
    while flag:
        flag = False
        print("1. voter \n2.Election Commission \n3.Exit")
        choice = int(input("Enter your response: "))
        if choice==0:
            print("==============")
            print("Thank you")
            print("==============")
            break
            
        elif choice==1:
            print("====================")
            print("Welcome to E-voting system!")
            print("====================")
            id = int(input("Enter your Voter_ID"))
            valid = False
            con = sqlite3.connect("Election.db")
            cur = con.cursor()
            cur.execute("select * from Voter")
            res = cur.fetchall()
            for row in res:
                if row[0]==id:
                    valid == True
                    user = row[1]
                if valid:
                    print("======================")
                    print("Welcome to Election-Commision Portal! :")
                    print("======================")
                    print("1.Add voter \n2.Update voter \n3.Add Nominee \n4.Update Nominee \n5.See result \n6. Download result")
                    r = int(input("Enter your response:"))
                    if r==1:
                        print("Add voter: ")
                        addVoter()
                    elif r==2:
                        print("Update Voter: ")
                        updateVoter()
                    elif r==3:
                        print("Add Nominee: ")
                        addNominee()
                    elif r==4:
                        print("Update Nominee: ")
                        updateNominee()
                    elif r==5:
                        print("See Result: ")
                        seeresult()
                    elif r==6:
                        print("Download result in csv form: ")
                        download()
                    else:
                        print("Invalid Response try again!")
                else:
                    print("Thank you!....exit")
                        
                        
                    
   db = sqlite3.connect("Election.db",timeout=20)

#voter table
import sqlite3
con = sqlite3.connect("Election.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS Voter(Voter_id INTEGER PRIMARY KEY,Voter_Name text,Voter_Location text,DoB text)")
con.commit()
con.close()

#Nominee table
import sqlite3
con = sqlite3.connect("Election.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS Nominee(Nom_Voter_id INTEGER PRIMARY KEY,Voter_Name text,Voter_Location text,DoB text)")
con.commit()
con.close()

#voting details table
import sqlite3
con = sqlite3.connect("Election.db")
cur = con.cursor()
cur.execute("CREATE TABLE  IF NOT EXISTS Voting_Details(Voter_id INTEGER PRIMARY KEY,Voter_Name text,Voter_Location text,DoB text)")
con.commit()
con.close()           
                        

                        
 
            
    
    
    
    
        