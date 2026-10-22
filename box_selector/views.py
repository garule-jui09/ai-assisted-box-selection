
from django.shortcuts import render
from .models import Product, ShippingBox
from .recommendation import recommend_box


def home(request):
    products = Product.objects.all().order_by("name")
    selected_product = None
    recommended_box = None
    checked = False
    error = None

    if request.method == "POST":
        checked = True
        product_id = request.POST.get("product_id")

        try:
            selected_product = Product.objects.get(pk=product_id)

            recommended_box = recommend_box(
                selected_product,
                ShippingBox.objects.all()
            )

            if recommended_box is None:
                error = "No suitable box is available for this product."

        except (Product.DoesNotExist, ValueError, TypeError):
            error = "Please select a valid product."

    return render(
        request,
        "box_selector/home.html",
        {
            "products": products,
            "selected_product": selected_product,
            "recommended_box": recommended_box,
            "checked": checked,
            "error": error,
        },
    )
