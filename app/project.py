from flask import Flask

app = Flask(__name__)


@app.route('/')

class Team :
    def __init__(self , name , sec , department ):
        self.name = name
        self.sec = sec
        self.department= department
        
        
def members ():
    member1 = Team("Ahmed Abd El-Maksoud Ahmed " , 4 , "CS")
    member2 = Team("Hazem Ahmad Ahmad Rady" , 2 , "CS") 
    member3 = Team("Mostafa Eid Abd El-Khalek " , 4 , "CS")
    member4 = Team("Hadeer Kandeel Abd El-Ghaffar " , 4 , "CS")
    member5 = Team("Yasmin Muhammad Abdullah" , 4 , "CS")
    print("")

    
    print("Team members ")
    
    print("1 ")
    print(member1.name , "    sec : " , member1.sec , "  " , member1.department)
    
    print("2 ")
    print(member2.name , "         sec : " , member2.sec , "  " , member3.department)

    print("3 ")
    print(member3.name , "     sec : " , member3.sec , "  " , member3.department)

    print("4 ")
    print(member4.name , "  sec : " , member4.sec , "  " , member4.department)

    print("5 ")
    print(member5.name , "        sec : " , member5.sec , "  " , member5.department)

print("")
members()
app.run(host='0.0.0.0', port=5000)
