from django.db import models
from django.urls import reverse


class Category(models.Model):
    """"""
    name = models.CharField("Категория", max_length=50)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Vendor(models.Model):
    """"""
    title = models.CharField("Производитель", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100)
    icon = models.ImageField("иконка", upload_to="vendor_icons/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("vendor_detail", kwargs={"slug": self.title})

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Item(models.Model):
    """"""
    title = models.CharField("Товар", max_length=100)
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Год выпуска", default=2000)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(
        Vendor, verbose_name="Производитель", related_name="vendor", on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField("остаток", default=0)
    price = models.DecimalField(verbose_name="Стоимость", max_digits=10, decimal_places=2)

    url = models.SlugField(max_length=100)
    image = models.ImageField("изображение", upload_to="item_images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"slug": self.url})
    
    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ItemShots(models.Model):
    """"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="item_shots/")
    item = models.ForeignKey(Item, verbose_name="Товар", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография товара"
        verbose_name_plural = "Фотографии товара"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="товар", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.item}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    item = models.ForeignKey(Item, verbose_name="товар", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.item}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
