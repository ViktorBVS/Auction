from email.policy import default
from tkinter import NONE
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

#--- 00 Активный пользователь ---------------------------------------------------------------#
class User(AbstractUser):
    pass

#--- 01 - Бренд производитель ---------------------------------------------------------------#
class Brend(models.Model):
    brend = models.CharField(max_length=32, db_index=True)
    
    class Meta:
        ordering = ('brend',)
        verbose_name = 'Бренд'
        verbose_name_plural = '01_Бренд'
    def __str__(self):
        return self.brend

#--- 02 - Тип механизма ---------------------------------------------------------------------#
class Type(models.Model):
    type = models.CharField(max_length=32, db_index=True)
    
    class Meta:
        ordering = ('type',)
        verbose_name = 'Механизм'
        verbose_name_plural = '02_Механизм'
    def __str__(self):
        return self.type

#--- 03 - Пол -------------------------------------------------------------------------------#
class Sex(models.Model):
    sex = models.CharField(max_length=8, db_index=True)
    
    class Meta:
        ordering = ('sex',)
        verbose_name = 'Пол'
        verbose_name_plural = '03_Пол'
    def __str__(self):
        return self.sex

#--- 04 - Материал корпуса ------------------------------------------------------------------#
class Case(models.Model):
    case = models.CharField(max_length=32, db_index=True)
    
    class Meta:
        ordering = ('case',)
        verbose_name = 'Материал корпуса'
        verbose_name_plural = '04_Материал корпуса'
    def __str__(self):
        return self.case

#--- 05 - Материал ремешка ------------------------------------------------------------------#
class Strap(models.Model):
    strap = models.CharField(max_length=32, db_index=True)
    
    class Meta:
        ordering = ('strap',)
        verbose_name = 'Материал ремешка'
        verbose_name_plural = '05_Материал ремешка'
    def __str__(self):
        return self.strap

#--- 06 - Водозащита ------------------------------------------------------------------------#
class Resist(models.Model):
    resist = models.CharField(max_length=8, db_index=True)
    
    class Meta:
        ordering = ('resist',)
        verbose_name = 'Водозащита'
        verbose_name_plural = '06_Водозащита'
    def __str__(self):
        return self.resist

#--- 07 - Страна производитель --------------------------------------------------------------#
class Country(models.Model):
    country = models.CharField(max_length=16, db_index=True)
    code = models.CharField(max_length=4, db_index=True)
    
    class Meta:
        ordering = ('country',)
        verbose_name = 'Страна производитель'
        verbose_name_plural = '07_Страна производитель'
    def __str__(self):
        return f"{self.country} ({self.code})"    

#--- 08 - Изображение товара ----------------------------------------------------------------#
class Image(models.Model):
    img_Name = models.CharField(max_length=32)
    img_Logo = models.ImageField(upload_to='images/')
    img_01 = models.ImageField(upload_to='images/')
    img_02 = models.ImageField(upload_to='images/')
    img_03 = models.ImageField(upload_to='images/')
       
    class Meta:
        ordering = ('img_Name',)
        verbose_name = 'Изображение товара'
        verbose_name_plural = '08_Изображение товара'
    def __str__(self):
        return f"{self.img_Name}"

#--- 09 - Описание товара -------------------------------------------------------------------#
class Product(models.Model):
    pr_Name = models.CharField(max_length=64, db_index=True)                                      # Название модели
    pr_Brend = models.ForeignKey(Brend, on_delete=models.CASCADE, related_name="pr_Brend")        # Бренд
    pr_Type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="pr_Type")           # Тип механизма
    pr_Sex = models.ForeignKey(Sex, on_delete=models.CASCADE, related_name="pr_Sex")              # Пол
    pr_Case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="pr_Case")           # Материал корпуса
    pr_Strap = models.ForeignKey(Strap, on_delete=models.CASCADE, related_name="pr_Strap")        # Материал ремешка
    pr_Resist = models.ForeignKey(Resist, on_delete=models.CASCADE, related_name="pr_Resist")     # Водозащита
    pr_Country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="pr_Country")  # Страна производитель
    pr_Img = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="pr_Img", default=1) # Картинки
    class Meta:
        ordering = ('pr_Name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'ТОВАРЫ'
    def __str__(self):
        return self.pr_Name

#--- 10 - Магазин ---------------------------------------------------------------------------#
class Shop(models.Model):
    sh_Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sh_Product")    # Название модели
    sh_Price = models.DecimalField(max_digits=10, decimal_places=2)                                 # Цена
    sh_Total = models.PositiveIntegerField(default=0)                                               # Всего едениц товара 
    sh_Sales = models.PositiveIntegerField(default=0)                                               # Количество проданого товара 
    sh_Left = models.PositiveIntegerField(default=0)                                                # Количество оставшегося товара
    sh_Sale = models.PositiveIntegerField(default=0)                                                # Скидка
    sh_Status = models.BooleanField(default=False)                                                  # Статус (в продаже/нет в наличии)
    sh_Desc = models.TextField(blank=True)                                                          # Описание
    sh_Date = models.DateTimeField(auto_now_add=True)                                               # Дата создания объявления
    
    class Meta:
        ordering = ('sh_Product',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'МАГАЗИН'

#--- 11 - Избранное -------------------------------------------------------------------------#
class Watchlist(models.Model):
    wl_User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    wl_Product_id = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    wl_Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=1)
    class Meta:
        ordering = ('wl_User',)
        verbose_name = 'Избранное'
        verbose_name_plural = '11_Избранное'
    def __str__(self):
        return f"{self.wl_User}:-> {self.wl_Product_id}, {self.wl_Shop}" 

#--- 12 - Коментарии ------------------------------------------------------------------------#
class Comment(models.Model):
    c_User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    c_Text = models.TextField(null=True, blank=True)
    c_Date = models.DateTimeField(auto_now=True)
    c_Product_id = models.IntegerField()
    
    class Meta:
        ordering = ('c_User',)
        verbose_name = 'Коментарии'
        verbose_name_plural = '12_Коментарии'
    def __str__(self):
        return f"{self.c_User} - {self.c_Product_id} ({self.c_Date}):-> {self.c_Text}" 

#--- 13 - Акции ---------------------------------------------------------------------------#
class Stock(models.Model):
    s_Title = models.CharField(max_length=512)
    s_Img = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ('s_Title',)
        verbose_name = 'Акции'
        verbose_name_plural = '13_Акции_Титул'
    def __str__(self):
        return f"{self.s_Title}" 
#--- 13 - Корзина ---------------------------------------------------------------------------#
#class ShoppingCart(models.Model):
#    sc_User = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#    sc_Product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
#    sc_Shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=1)
#    sc_Sum = models.IntegerField()
#    class Meta:
#        ordering = ('sc_User',)
#        verbose_name = 'Корзина'
#        verbose_name_plural = '13_Корзина'
#    def __str__(self):
#        return f"{self.sc_User}:-> {self.sc_Product}" 
