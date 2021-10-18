from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProImag, ProductReview, Home_images, Category
from django.core.paginator import Paginator
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from cart.forms import CartAddProductForm
from django.db.models import Q
from django.conf import settings
from .models import Product


def all_prodcut(request, category_slug=None):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

    
        
    # categories = Category.objects.all()
    # category = request.GET.get('category')
    # if category == None:
    #     all_prodcut = Product.objects.all()
        
    # else:
    #     all_prodcut = Product.objects.filter(category__name=category)
    category = None
    categories = Category.objects.all()
    # products = Product.objects.filter(available=True)
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, slug=category_slug)
        all_prodcut = Product.objects.filter(category__name=category)
    else:
        all_prodcut = Product.objects.all()
    # products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    imagess = Home_images.objects.all()
    
    paginator = Paginator(all_prodcut, 8)
    page_number = request.GET.get('page')
    all_prodcut = paginator.get_page(page_number)
    
   
    con = {'all_prodcut': all_prodcut,
           'categories': categories,
        #    'products': products,
           'imagess': imagess,
           
           'cart_product_form': cart_product_form,
           }
    return render(request, 'all_product.html', con)


def one_prodcut(request, slug):

    product = get_object_or_404(Product, slug=slug)
    one_prodcut = Product.objects.get(slug=slug)
    cart_product_form = CartAddProductForm()
    images = ProImag.objects.filter(product=product)

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(
            product=product, user=request.user, stars=stars, content=content)

        return redirect(".", slug=slug)

    con = {'one_prodcut': one_prodcut,
           'cart_product_form': cart_product_form,
           'product': product,
           'images': images,

           }
    return render(request, 'one_product.html', con)


def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        #return HttpResponse(lang)
        return HttpResponseRedirect("/"+lang)


def about_us(request):
    return render(request, 'about.html')


def search(request):
    # second is default parameter which is empty
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(Book_name__icontains=query) | Q(descrip__icontains=query))

    return render(request, 'products.html', {'products': products, 'query': query})


def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)
