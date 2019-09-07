from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from . import models

from django.shortcuts import render


# Create your views here.
def add_to_basket(request):
    product = get_object_or_404(models.Product, pk=request.GET.get("product_id"))
    basket = request.basket
    if not request.basket:
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        basket = models.Basket.objects.create(user=user)

        request.session["basket_id"] = basket.id
    basketline, created = models.BasketLine.objects.get_or_create(basket=basket, product=product)

    if not created:
        basketline.quantity += 1
        basketline.save()
    return HttpResponseRedirect(reverse("main:product", args=(product.slug,)))
