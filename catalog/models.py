from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(
        upload_to="images/category/",
        verbose_name="Изображение категории",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание категории",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]


class SubCategory(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название подкатегории",
        help_text="Введите название подкатегории",
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="images/subcategories/",
        verbose_name="Изображение подкатегории",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание категории",
    )
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Субкатегория"
        verbose_name_plural = "Субкатегории"
        ordering = ["title"]


class Product(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание продукта",
    )
    image_small = models.ImageField(
        upload_to="images/products/small/",
        verbose_name="Изображение маленькое",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    image_medium = models.ImageField(
        upload_to="images/products/medium/",
        verbose_name="Изображение среднее",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    image_large = models.ImageField(
        upload_to="images/products/large/",
        verbose_name="Изображение большое",
        blank=True,
        null=True,
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену продукта")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")
    slug = models.SlugField(unique=True, blank=True, null=True)
    subcategory = models.ForeignKey(
        SubCategory, related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["title"]
