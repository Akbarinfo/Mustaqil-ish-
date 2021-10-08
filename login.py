import os
import platform


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
        pass

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

### Oynani tozalash
    def clear(self):
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            print("Balki sizda MacOs,dir")

window = Register()
