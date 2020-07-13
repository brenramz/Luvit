from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(
        'name', min_length=3, max_length=55)
    value = models.DecimalField(
        'value', decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.9)])
    discount_value = models.DecimalField(
        'discount value', decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(99999.9)])
    stock = models.IntegerField(
        'stock', validators=[MinValueValidator(-1)])

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
