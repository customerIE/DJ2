# —оздайте три модели Django: клиент, товар и заказ.
#
#  лиент может иметь несколько заказов. «аказ может содержать несколько товаров. “овар может входить в несколько заказов.
#
# ѕол€ модели Ђ лиентї:
# Ч им€ клиента
# Ч электронна€ почта клиента
# Ч номер телефона клиента
# Ч адрес клиента
# Ч дата регистрации клиента
#
# ѕол€ модели Ђ“оварї:
# Ч название товара
# Ч описание товара
# Ч цена товара
# Ч количество товара
# Ч дата добавлени€ товара
#
# ѕол€ модели Ђ«аказї:
# Ч св€зь с моделью Ђ лиентї, указывает на клиента, сделавшего заказ
# Ч св€зь с моделью Ђ“оварї, указывает на товары, вход€щие в заказ
# Ч обща€ сумма заказа
# Ч дата оформлени€ заказа
#
# ƒопишите несколько функций CRUD дл€ работы с модел€ми по желанию.


from django.db import models
from datetime import date

class Client(models.Model):     # наследуемс€ от класса model
    name = models.CharField(max_length=100)        # —оздаем столбцы таблицы, id в django проставитс€ автоматически
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_registration = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User name: {self.name}, email:{self.email}, phone: {self.phone}, address: {self.address}, ' \
               f'date_registration: {self.date_of_registration}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2) # максимум чисел 8 и мест после зап€той 2
    description = models.TextField()                            # какой то очень большой текст
    quantity_of_goods = models.IntegerField(default=0)
    product_update_date = models.DateTimeField(date)


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE) # заказчик, ссылка на пользовател€ и при удалении пользовател€, мы удалим все его заказы
    products = models.ManyToManyField(Product)                   # много заказов могут содержать данный продукт и много продуктов могут быть в заказе
    date_ordered = models.DateTimeField(auto_now_add=True)       # при заказе автоматически ставитс€ дата и врем€
    total_price = models.DecimalField(max_digits=8, decimal_places=2)