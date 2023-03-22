from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ism', null=True)
    tg_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Telegram id')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Raqam', null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return str(self.tg_id)

    class Meta:
        verbose_name = "Foydalanuvchilar"
        verbose_name_plural = "Foydalanuvchilar"


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Kategroiya nomi')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mashinalar"
        verbose_name_plural = "Mashinalar"


class Product(models.Model):
    photo = models.ImageField(verbose_name='Tovar surati')
    price = models.PositiveBigIntegerField(verbose_name='Tovar narxi')
    quan = models.PositiveIntegerField(verbose_name='Soni')
    descr = models.TextField(verbose_name='Tavsifi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    def __str__(self):
        return f'{self.category.name}, {self.price} so\'m'

    class Meta:
        verbose_name = "Chexollar"
        verbose_name_plural = "Chexollar"


class Video(models.Model):
    product = models.ForeignKey(Product, related_name='video', on_delete=models.CASCADE)
    video = models.FileField(verbose_name='Video')

    def __str__(self):
        return str(self.product.price)

    class Meta:
        verbose_name = "Tovar videolari"
        verbose_name_plural = "Tovar videolari"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Foydalanuvchi')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Chexol')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Sana')

    class Meta:
        verbose_name = "Buyurmalar"
        verbose_name_plural = "Buyurtmalar"
