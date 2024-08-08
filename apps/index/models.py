from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Ism")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Asal turi"
        verbose_name_plural = "Asal turlari"

    def get_absolute_url(self):
        return reverse("product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        "Category",
        related_name="products",
        on_delete=models.PROTECT,
        verbose_name="Kategoriya",
    )
    name = models.CharField(max_length=200, db_index=True, verbose_name="Ism")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(verbose_name="Rasmi", upload_to="products/", blank=True)
    description = models.TextField(blank=True, verbose_name="Tavsif")
    price = models.PositiveIntegerField(verbose_name="Narx")
    stock = models.PositiveIntegerField(verbose_name="Miqdori")
    available = models.BooleanField(default=True, verbose_name="Mavjud")
    weight = models.DecimalField(
        max_digits=10, decimal_places=1, verbose_name="Og'irligi"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name
