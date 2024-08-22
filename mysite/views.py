from django.shortcuts import render, get_object_or_404
from .models import Discount, Order
from .forms import DiscountForm


def apply_discount(request, pk=1):
    orders = get_object_or_404(Order, pk)
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            percent = Discount.objects.get(code=form.cleaned_data['code']).percentage
            orders.discount = orders.original_price - (percent / 100) * orders.original_price
            orders.save()
            return render(request, 'main.html', {'dis': orders.discount})
    return render(request, 'main.html', {'form': DiscountForm})
