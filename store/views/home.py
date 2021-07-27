from django.shortcuts import render
from django.views import View
from store.models.category import Catagory
from store.models.product import Product

# Create your views here.
class Index(View):
    def get(self, request):
        products = None
        categories = Catagory.get_all_categories();
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        # return render(request, 'orders/order.html')
        # print(prds)
        return render(request, 'index.html', data)
