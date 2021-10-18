from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name=("category"))
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ost:product_list_by_category', args=[self.slug])
# class Category(models.Model):

# 	name = models.CharField(max_length=200, db_index=True,
# 	                        verbose_name=("category"))
# 	slug = models.SlugField(max_length=200, db_index=True, unique=True)

# 	class Meta:
# 		ordering = ('name',)
# 		verbose_name = "Category"
# 		verbose_name_plural = "Categorys"

# 	def __str__(self):
# 		return self.name
    
#     def get_absolute_url(self):
#         return reverse('products:product_list_by_category', args=[self.slug])


class Product(models.Model):
   
    Book_name = models.CharField(
        max_length=100, verbose_name=("أسم المنتج "), db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,
                            unique=True, blank=True, null=True)
    category = models.ForeignKey(
     	Category, related_name='product', on_delete=models.CASCADE, default=False, null=True)
    descrip = RichTextUploadingField(
        verbose_name=("وصف المنتج"), blank=True, null=True)
    product_info = RichTextUploadingField(verbose_name=(
        "معلومات المنتج"), default="", blank=True, null=True)
    Book_image = models.ImageField(
        upload_to='Produkten/', verbose_name=("صور"), blank=True, null=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=0, verbose_name=("سعر المنتج"))
    Discountprice = models.DecimalField(
        max_digits=7, decimal_places=0, default="0", verbose_name=("سعر عند وجود خصم"))
    Frakt = models.DecimalField(
        max_digits=7, decimal_places=0, verbose_name=("Frakt"))
    created = models.DateTimeField(verbose_name=("تاريخ الاضافة"))
    updated = models.DateTimeField(
        auto_now=True, verbose_name=("تاريخ الاضافة"))

    

    class meta:
        index_together = (('id', 'slug'),)
        verbos_name = ('Product')
        verbos_name_plural = ('Products')

    def __str__(self):
        return self.Book_name

    def get_absolute_url(self):
        # [self.id,self.slug]) #args
        return reverse('ost:one_prodcut', kwargs={'slug': self.slug})

    def __str__(self):
        return self.Book_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Book_name)
        super(Product, self).save(*args, **kwargs)

             

              


class ProImag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=("produktnamn"))
    image = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("produktbild"))

    def __str__(self):
        return str(self.product)


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


class Home_images(models.Model):

    image_1 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الاولى"))
    image_2 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الثانيه"))
    image_3 = models.ImageField(
        upload_to='Produkten/', default="0", blank=True, verbose_name=("الصورة الرئيسية الثالثة"))

    def __str__(self):
        return str(self.image_1)



