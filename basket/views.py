from django.shortcuts import render, redirect, reverse, get_object_or_404
from parts.models import Parts


def basket(request):
    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return render(request, "basket/basket.html")


def update_basket(request, item_id):
    part = get_object_or_404(Parts, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity

    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_basket(request, item_id):
    basket = request.session.get('basket', {})
    basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))
