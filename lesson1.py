class Product:
    # створили: имя категорію цціну та к-сть
    def __init__(self, name, category, price , quantity, ):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
# показує інформацію яку ми впишем в зміну класу 
    def information (self):
        print(f'Продукт {self.name} категорія: {self.category} ціна {self.price} кількість {self.quantity} ')        
#можна вписати нову ціну за продукту
    def change_price(self, new_price):
        self.price = new_price
        print(f'Ціна на {self.name} змінена на {self.price}')
# можна вписати нову к-сть продукту 
    def update_quantity(self,amount):
        self.quantity = amount
        print(f'Нова кількість продукту {self.name}: {self.quantity}')
# юзер блок 
class Customer:
    def __init__(self, name, email ,):
        self.name = name
        self.email = email
        self.orders = []
#коли клієнт робе заказ додаємо до пустого списку self.orders = [] пишем іім'я та суму
    def add_order(self, order):
        self.orders.append(order)
        print(f"Клієнт {self.name} оформив замовлення. До сплати: {order.total_sum}")
# сторюємо список покупок і зазначаємо що на даний момент ця сума 0      
products_list=[]
class Order:
    def __init__(self):
        self.products = []
        self.total_sum = 0
# добавляємо продукт який ми спишем в ... .add_product(якийсь продукт): , і додаємо до загальной суми
    def add_product(self,product):
        self.products.append(product)
        self.total_sum = self.total_sum + product.price
        print(f"До замовлення додано: {product.name}. Сума: {self.total_sum}")

# читаємо тхт файл де будуть декілька товарів
with open(r'product.txt', 'r', encoding='utf-8') as file:
    for i in file:
        data = i.strip().split(',') #розділяємо інформацію через кому 
        new_product = Product(data[0],data[1],float(data[2]),float(data[3]))#кажемо що буде 4 різних даних name, category, price , quantity
        products_list.append(new_product)#додаємо в список який раніше стврорили 

# відображення інфи
my_toy =Product('Свинка ','іграшка', 500, 10)
my_toy.change_price(600) #змінено ціну
my_toy.update_quantity(21) #змінено к-сть
my_toy.information()

# звертаємось до списку покупок 
my_order = Order()
first_toy = products_list[0] #робимо першу покупку зазначаємо що купляємо товар ведмедик який в тхт файлі під номером 0
my_order.add_product(first_toy)#через ад продук додаємо перший продукт щоб сума додалась до 0 
second_toy = products_list[1]
my_order.add_product(second_toy)

client = Customer("Владислав", "vlad@email.com")
client.add_order(my_order)


