from django.shortcuts import render,redirect

def home(req):
    return render(req,'home.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import Item, Rack
from .forms import ItemForm

# View to add an item
class AddItemView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'add_item.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list page
        return render(request, 'add_item.html', {'form': form, 'error': 'Form submission failed'})

# View to list all items
class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'item_list.html', {'items': items})

# View to search an item
class SearchItemView(View):
    def get(self, request):
        query = request.GET.get('query', '').strip()
        items = Item.objects.filter(name__icontains=query)

        if items.exists():
            results = [
                {'name': item.name, 'rack': item.rack.name, 'quantity': item.quantity, 'stock': item.stock}
                for item in items
            ]
        else:
            results = []

        return JsonResponse({'items': results})
