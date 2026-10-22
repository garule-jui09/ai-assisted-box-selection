def fits_inside(product, box):
    product_dimensions = sorted([
        product.length,
        product.width,
        product.height,
    ])

    box_dimensions = sorted([
        box.length,
        box.width,
        box.height,
    ])

    dimensions_fit = all(
        p <= b
        for p, b in zip(product_dimensions, box_dimensions)
    )

    weight_fits = product.weight <= box.max_weight

    return dimensions_fit and weight_fits


def recommend_box(product, boxes):
    suitable_boxes = [
        box for box in boxes
        if fits_inside(product, box)
    ]

    if not suitable_boxes:
        return None

    return min(
        suitable_boxes,
        key=lambda box: (box.cost, box.pk or 0)
    )