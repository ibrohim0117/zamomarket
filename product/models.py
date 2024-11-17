import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from user.models import BaseCreatedModel


class Category(BaseCreatedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += '-' + str(uuid.uuid4()).split()[-1]
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class SubCategory(BaseCreatedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while SubCategory.objects.filter(slug=self.slug).exists():
            self.slug += '-' + str(uuid.uuid4()).split()[-1]
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(BaseCreatedModel):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', db_index=True)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    count = models.IntegerField(validators=[MinValueValidator(1)])
    is_active = models.BooleanField(default=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while Product.objects.filter(slug=self.slug).exists():
            self.slug += '-' + str(uuid.uuid4()).split()[-1]
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    def __str__(self):
        return self.name


class ProductImage(BaseCreatedModel):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Comment(BaseCreatedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=25, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.user:
            self.username = self.user.username
        else:
            self.username = 'AnonymousUser'
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)


class Cart(BaseCreatedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    now_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.product:
            self.now_price = self.product.price
        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,
                     update_fields=update_fields)

    @property
    def total_price(self):
        return self.quantity * self.now_price









