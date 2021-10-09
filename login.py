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
        self.menyu()

    ### Bosh menyu
    def menyu(self):
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
        pass

    ### shaxsiy bolim
    def shaxsiy(self):
        pass

    ### Login o'zgartirish
    def ologin(self):
        pass

    ### Parolni o'zgartirish
    def oparol(self):
        pass

    ### Tizimdan chiqish
    def logout(self):
        pass

    ### Accountni o'chirish
    def delete(self):
        pass

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
