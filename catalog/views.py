from django.shortcuts import render
from .models import Product, Category, Tag

def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')
    tag_ids = request.GET.getlist('tags')

    products = Product.objects.all()

    if query:
        products = products.filter(description__icontains=query)
    if category_id:
        products = products.filter(category_id=category_id)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'tags': tags,
        'selected_category': category_id,
        'selected_tags': list(map(int, tag_ids)),
    })