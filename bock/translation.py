from modeltranslation.translator import register, TranslationOptions
from .models import Product, Category


@register(Product)
class NewsTranslationOptions(TranslationOptions):
    fields = ('Book_name', 'descrip', 'product_info',)


@register(Category)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', )
