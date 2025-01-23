class MarsStudent:
    def __init__(self, id, password, ism, familiya, yosh):
        self.id = id
        self.parol = password
        self.name = ism
        self.surname = familiya
        self.age = yosh
        self.coin = 0


    def add_coin(self, *son_kirit):
        """ Coin qushish"""
        obshiy = sum(son_kirit)
        self.coin += obshiy
        print(f""" 
Qushilgan coinlar: {self.coin}
""")
    def cut_coin(self, *minus_coin):
        """ Coin ayirish """
        minus_yigini = sum(minus_coin)
        self.coin -= minus_yigini
        print(f"""
Ayirilgan coin: {minus_yigini}
Qogan coin: {self.coin}
""")
    def get_coin(self):
        """ Coinlarni ko'rish """
        print(f"""
Barcha coinlaringiz: {self.coin} ta
""")


    def full_data(self):
        """ User bazasini kurish """
        while True:
            id = int(input('Idini kiriting: '))
            if id == self.id:
                password = int(input('Parolingizni kiriting: '))
                if password == self.parol:
                        print(f""" 
                    Ism: {self.name}
                    Familiya: {self.surname}
                    Yosh: {self.age}
                    """)
                else:
                    print('Parolingizni xato kiritdingiz')
                    continue
            else:
                print('Idini xato kiritdingiz!')
                continue

student1 = MarsStudent(12345, 2010, 'yashnar', 'xamzayev', 14)
student1.add_coin(12,12,121,1)
student1.add_coin(12,12,12)
student1.get_coin()
student1.cut_coin(12, 12,12)
student1.full_data()