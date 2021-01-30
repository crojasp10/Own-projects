import pymysql

#Here is a class called Vehicle with three variables in the constructor
class vehicle():
    def __init__(self,passengers,speed, brand):
        self.brand = brand
        self.speed = speed
        self.passengers=passengers

#This class has three methods the first one is to connect and create(if it does not exist) a new table(to keep the trucks objects) on a MySql server.
#The second one connects to the database and create(if doesn't exist)a table (to keep the motorcycles objects)on the same MySql local server
#The third one is just to connect the database and create a cursor like the other ones as well
class connection():

    def connectionA(self):   
        conex= pymysql.connect(db="practica",
        user="root",
        password="----",
        host="Localhost",
        port=3306) 
        cur= conex.cursor()
        try:
            cur.execute('''CREATE TABLE TRUCKS(
            ID INTEGER PRIMARY KEY AUTO_INCREMENT,
            Brand VARCHAR(50),
            Passengers INTEGER,
            Speed INTEGER,
            Shipment INTEGER)''')
        except:
            print("La base de datos ya existe")
        
        datss= [(self.brand,self.passengers,self.speed,self.shipment)]
        cur.executemany("INSERT INTO TRUCKS VALUES(NULL, %s,%s,%s,%s)",datss)
        conex.commit()
    
    def connectionB(self):   
        conex= pymysql.connect(db="practica",
        user="root",
        password="----",
        host="Localhost",
        port=3306) 
        cur= conex.cursor()
        try:
            cur.execute('''CREATE TABLE MOTORCYCLES(
                ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                Brand VARCHAR(50),
                Passengers INTEGER,
                Speed INTEGER,
                Color VARCHAR(50))''')
        except:
            print("La base de datos ya existe")
        
        datss= [(self.brand,self.passengers,self.speed,self.color)]
        cur.executemany("INSERT INTO MOTORCYCLES VALUES(NULL, %s,%s,%s,%s)",datss)
        conex.commit()

    def Connected(self):   
        conex= pymysql.connect(db="practica",
        user="root",
        password="----",
        host="Localhost",
        port=3306) 
        cur= conex.cursor()

#This Truck class inherit from vehicle class,connection class and use a new variable.    
class truck(vehicle,connection):
    def __init__(self,passengers,speed,brand,shipment):
        self.shipment=shipment
        super().__init__(passengers,speed, brand)

#This moto class inherit from vehicle class, connection class and use a new variable.   
class moto(vehicle,connection):
    def __init__(self,passengers,speed,brand,color):
        self.color = color
        super().__init__(passengers,speed,brand)

#Here we can find the creation of a connection object called Comands, them there's a Do-while constructed loop, we can find three options.
#1.It's to create a truck object(option 1) or moto object (option 2) and save it on the respective tables on the database thanks to the connectionA and connectionB methods inherited from connection class.
#2.It's to show the data saved on the tables option 1 to show trucks data and option 2 to show motorcycles data. In this option we use the method connected from the connection object
#3.Here the Flag variable is False and the program is over. 
Comands=connection()
Flag=True
while Flag:
    print("1.Register a vehicle\n2.Watch the data\n3.Close")
    Selection=input()
    if Selection=="1":
        print("Choose a kind of vehicle(1=Truck or 2=motorcycle): ")
        Select=input()
        if Select=="1":
            passenger=2
            bran=input("which brand?: ")
            spee=input("How fast?: ")
            ship=input("How much shipment?: ")
            camion=truck(passenger,spee,bran,ship)
            camion.connectionA()

        if Select=="2":
            print("Enter the data(passengers,speed,brand and color separeted by comma(,)")
            dat=input()
            data=dat.split(",")
            pas=data[0]
            spe=data[1]
            bra=data[2]
            col=data[3]
            Motor=moto(pas,spe,bra,col)
            Motor.connectionB()
    
    if Selection=="2":
        print("Do you want to watch the Trucks(1) or the Motorcycles(2)")
        order=input()
        if order=="1":
            Comands.Connected()
            cur.execute("SELECT ID, Brand,Passengers,Speed,Shipment FROM TRUCKS")
            List=cur.fetchall()
            for i in List:
                print("Id:",i[0],"\nBrand:",i[1],"\nPassengers:",i[2],"\nSpeed:",i[3],"\nColor:",i[4],"\n")
            conex.commit()
        if order=="2":
            Comands.connected()
            cur.execute("SELECT ID, Brand,Passengers,Speed,Color FROM MOTORCYCLES")
            Listt=cur.fetchall()
            for i in Listt:
                print("Id:",i[0],"\nBrand:",i[1],"\nPassengers:",i[2],"\nSpeed:",i[3],"\nColor:",i[4],"\n")
            conex.commit()
            
    if Selection=="3":
        Flag=False
        print("The program is over")


    
