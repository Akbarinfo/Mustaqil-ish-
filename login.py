import os
import platform
import stdiomask
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="123456789",
    database="user_info"
)

myreg = mydb.cursor()


class Register:
    def __init__(self):
        self.id = None
        self.ism = None
        self.login = None
        self.password = None
        self.age = None
        self.single = None
        ###Bosh menyu
        self.menyu()

    ### Bosh menyu
    def menyu(self):
        self.clear()
        print("""
        Assalom-u aleykum Mehmon

Ro'yhatdan o'tish      [1]
Tizimga kirish         [2]   
        """)

        menyu = input("Kirting [1]/[2]: ").strip()
        tmenyu = ["1", "2"]
        while menyu not in tmenyu:
            self.clear()
            print("Noto'g'ri belgi kirtingiz!")
            menyu = input("Kirting [1]/[2]: ").strip()
        if menyu == "1":
            self.reg()
        else:
            self.kirish()

    ### Ro'yhatdan o'tish
    def reg(self):
        self.clear()
        print("Ro'yhatdan o'tish")

        ###Ismingiz kiriting
        ism = input("Ismingiz: ").strip().title()
        while not ism.isalpha():
            self.clear()
            self.xato()
            ism = input("Ismingiz: ").strip().title()

        ### login kiriting
        login = input("Login: ").strip().title()
        while not login.isalnum():
            self.clear()
            self.xato()
            login = input("Login: ").strip().title()

        ### Parol kiriting
        parol = stdiomask.getpass(prompt="Parol: ", mask='*').strip()
        qparol = stdiomask.getpass(prompt="Parolni takrorlang: ", mask='*').strip()
        while parol != qparol:
            self.clear()
            self.xato()
            parol = stdiomask.getpass(prompt="Parol: ", mask='*').strip()
            qparol = stdiomask.getpass(prompt="Parolni takrorlang: ", mask='*').strip()

        ### yoshingizni kirting
        yosh = input("Yoshingiz: ").strip()
        while not yosh.isnumeric() or int(yosh) > 150:
            self.clear()
            self.xato()
            yosh = input("Yoshingiz: ").strip()

        ### Oilasimisiz
        oila = input("Oilaliymisiz [y/n]: ").strip().lower()
        toila = ["yes", "y", "no", "n"]
        while oila not in toila:
            self.clear()
            self.xato()
            oila = input("Oilaliymisiz [y/n]: ").strip().lower()
        if oila == "yes" or "y":
            oila = 0
        else:
            oila = 1

        ## Bazaga yozish
        myreg.execute("create table if not exists mustaqil(id int unsigned auto_increment primary key,"
                      "name varchar(30) not null,"
                      "login varchar(30) not null,"
                      "password varchar(30) not null,"
                      "age int(3) not null,"
                      "single bool default False)")
        myreg.execute(f"insert into mustaqil(name, login, password, age, single)"
                      f" values('{ism}', '{login}', '{parol}', {yosh}, {oila})")
        mydb.commit()
        #### Ro'yhatdan o'tilsa
        self.shaxsiy()

        ### Kirish

    def kirish(self):
        self.clear()
        print("\t Kirish")
        login = input("Login: ").strip().title()
        parol = stdiomask.getpass(prompt="Parol: ", mask='*').strip()
        while not self.chaqirish(login) or self.password != parol:
            self.clear()
            if self.login !=login:
                print("Bunaqa login yo'q")
            else:
                self.xato()
            login = input("Login: ").strip().title()
            parol = stdiomask.getpass(prompt="Parol: ", mask='*').strip()
        self.shaxsiy()

    ### shaxsiy bolim
    def shaxsiy(self):
        self.clear()
        print(f"""
            Assalom-u aleykum {self.ism}
    Shaxsiy bo'lim
Shaxsiy ma'lumotlar     [1]
Loginni o'zgartirish    [2]
Parolni o'zgartirish    [3]
Chiqish                 [4]
Accountni o'chirish     [5]
        """)
        tanla = input("Kirting [1]/[2]/[3]/[4]/[5]: ").strip()
        ttanla = ["1", "2", "3", "4", "5"]
        while tanla not in ttanla:
            self.clear()
            self.xato()
            tanla = input("Kirting [1]/[2]/[3]/[4]/[5]: ").strip()
        if tanla == "1":
            self.malumot()
        elif tanla == "2":
            self.ologin()
        elif tanla == "3":
            self.oparol()
        elif tanla == "4":
            self.logout()
        else:
            self.delete()


### Shaxsiy Ma'lumotlar
    def malumot(self):
        self.clear()
        print(f"""
        Shaxsiy Ma'lumotlar
id {self.id}
Loginingiz {self.login}
Ismingiz {self.ism}
Yoshingiz {self.age}
Oilaliymi {self.single}
        """)
        self.nazad()

### Login o'zgartirish
    def ologin(self):
        self.clear()
        print("Loginni O'zgartirish")
        joriy = input("Joriy Loginngiz: ").strip().title()
        while self.login != joriy:
            self.clear()
            print("Joriy loginni xato kirtingiz:")
            joriy = input("Joriy Loginngiz: ").strip().title()
        login = input("Yangi Login kirting: ").strip().title()
        while not login.isalnum():
            self.clear()
            self.xato()
            login = input("Yangi Login kirting: ").strip().title()
        myreg.execute(f"update mustaqil set login='{login}' where id={self.id}")
        mydb.commit()
        self.clear()
        print("Muvafaqiyatli o'zgartildi\n")
        self.nazad()

    ### Parolni o'zgartirish
    def oparol(self):
        self.clear()
        print("Parol o'zgartirish")
        joriy = stdiomask.getpass(prompt="Joriy parol: ", mask='*').strip()
        while joriy != self.password:
            self.clear()
            print("Joriy parolni xato kirtingiz")
            joriy = stdiomask.getpass(prompt="Joriy parol: ", mask='*').strip()
        parol = stdiomask.getpass(prompt="Yangi parol: ", mask='*').strip()
        yparol = stdiomask.getpass(prompt="Yangi parolni takrorlang: ", mask='*').strip()
        while parol != yparol or not parol.isalnum():
            self.clear()
            if parol !=yparol:
                print("Takroran parolni xato kirtingiz!")
            else:
                self.xato()
            parol = stdiomask.getpass(prompt="Yangi parol: ", mask='*').strip()
            yparol = stdiomask.getpass(prompt="Yangi parolni takrorlang: ", mask='*').strip()
        myreg.execute(f"update mustaqil set password='{parol}' where id={self.id}")
        mydb.commit()

        self.kirish()

    ### Tizimdan chiqish
    def logout(self):
        self.clear()
        print("Rostan bizni tark etyabsizmi?")
        log = input("Kirting [y/n]: ").strip().lower()
        tlog = ["yes", "y", "no", "n"]
        while log not in tlog:
            self.clear()
            self.xato()
            log = input("Kirting [y/n]: ").strip().lower()
        if log == "yes" or log == "y":
            self.menyu()
        else:
            self.shaxsiy()

    ### Accountni o'chirish
    def delete(self):
        self.clear()
        print("parol")
        self.nazad()

### Bazadan malumotlarni olish
    def chaqirish(self, login):
        myreg.execute(f"select *from mustaqil where login='{login}'")
        natija = myreg.fetchall()
        for id, name, login, parol, age, single in natija:
            self.id = id
            self.ism = name
            self.login = login
            self.password = parol
            self.age = age
            if single == 1:
                self.single = "Oilaliy"
            else:
                self.single = "Endi to'y"

        if self.login == login:
            return True
        else:
            return False

### Orqaga qaytish
    def nazad(self):
        nazad = input("Bosh sahifa [yes/y]: ").strip().lower()
        tnazad = ["yes", "y"]
        while nazad not in  tnazad:
            self.clear()
            self.xato()
            nazad = input("Bosh sahifa [yes/y]: ").strip().lower()
        self.shaxsiy()

    ### Error
    def xato(self):
        print("Noto'g'ri belgi kirtingiz!")

    ### Oynani tozalash
    def clear(self):
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            print("Balki sizda MacOs,dir")


window = Register()
