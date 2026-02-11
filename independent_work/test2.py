class User:
    def __init__(self,name):
        self.name = name

class UserRepository:
    def save_to_file(self, user):
        self.user = user
        with open('my_homework/independent_work/user.txt','a', encoding='utf-8') as f:
            f.write(f'{user.name}\n')
        print(f"[Файл]: Користувача {user.name} збережено у user.txt") 

class EmailService:
    def send_email(self, user):
        print(f"[Email]: Привіт, {user.name}! Раді бачити тебе в нашій команді!")

my_arhive=UserRepository()
my_postman = EmailService()

user1 = User('Іван')
my_arhive.save_to_file(user1)
my_postman.send_email(user1)

user2 = User('Коля')
my_arhive.save_to_file(user2)
my_postman.send_email(user2)
        



    