from django.test import TestCase
from .models import Product, ShippingBox
from .recommendation import fits_inside, recommend_box


class BoxRecommendationTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Headphones",
            length=10,
            width=8,
            height=5,
            weight=0.5,
        )

        self.cheap_box = ShippingBox.objects.create(
            name="Small Box",
            length=12,
            width=10,
            height=7,
            max_weight=1,
            cost=20,
        )

        self.expensive_box = ShippingBox.objects.create(
            name="Large Box",
            length=20,
            width=15,
            height=10,
            max_weight=5,
            cost=50,
        )

    def test_product_fits_inside_box(self):
        self.assertTrue(fits_inside(
            self.product, self.cheap_box
        ))

    def test_selects_lowest_cost_suitable_box(self):
        result = recommend_box(
            self.product,
            ShippingBox.objects.all()
        )
        self.assertEqual(result, self.cheap_box)

    def test_rejects_box_with_insufficient_weight_capacity(self):
        self.cheap_box.max_weight = 0.2
        self.cheap_box.save()

        self.assertFalse(fits_inside(
            self.product, self.cheap_box
        ))

    def test_returns_none_when_no_box_fits(self):
        ShippingBox.objects.all().delete()

        result = recommend_box(
            self.product,
            ShippingBox.objects.all()
        )
        self.assertIsNone(result)

    def test_product_can_fit_after_rotation(self):
        self.product.length = 10
        self.product.width = 20
        self.product.height = 5
        self.product.save()

        rotated_box = ShippingBox.objects.create(
            name="Rotated Box",
            length=20,
            width=10,
            height=8,
            max_weight=2,
            cost=30,
        )

        self.assertTrue(fits_inside(
            self.product, rotated_box
        ))

    def test_exact_dimension_and_weight_limits(self):
        exact_box = ShippingBox.objects.create(
            name="Exact Fit",
            length=10,
            width=8,
            height=5,
            max_weight=0.5,
            cost=10,
        )

        self.assertTrue(fits_inside(
            self.product, exact_box
        ))