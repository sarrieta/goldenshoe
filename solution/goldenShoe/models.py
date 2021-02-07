from django.db import models
import uuid

from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

# Create your models here.




class Product(models.Model):

    type_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    color_choices = (
        ('Yellow', 'Yellow'),
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Pink', 'Pink'),
        ('Brown', 'Brown'),
        ('Green', 'Green'),
        ('Fucsia', 'Fucsia'),
        ('Orange', 'Orange'),
        ('Grey', 'Grey'),
        ('Peach', 'Peach'),
        ('Amber', 'Amber'),
        ('White', 'White'),
    )
    size_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    category = (
        ('Sport', 'Sport'),
        ('Smart', 'Smart'),
        ('Slipper', 'Slipper'),
        ('Heel', 'Heel'),

    )
    name = models.CharField(max_length=30)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    color = models.CharField(max_length=10, choices=color_choices)
    size = models.CharField(max_length=10, choices=size_choices, default=9)
    type = models.CharField(max_length=10, choices=type_choices)
    image = models.ImageField(max_length=100,upload_to="media", default='')
    quantity = models.IntegerField(default=10)
    description = models.CharField(max_length=100, default="tesst")
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=10, choices=category, default="Smart")


    def __str__(self):
       return 'Policy: ' + self.name


class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))
    order_trans_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.SET_NULL,null= True, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null= True, related_name='requests_created')
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)
