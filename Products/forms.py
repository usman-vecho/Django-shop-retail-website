from django import forms
from .models import Cart,Products
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name','volume','selling_price','purchase_price','benifit','total','total_quantity']
        labels = {'product_name':'اسم المنتج',
                    'volume':'الوزن (كغم)',
                    'selling_price':'سعر البيع',
                    'purchase_price':'سعر الشراء',
                    'benifit':'فائدة',
                    'total':'المجموع',
                    'total_quantity':'الإجمالي'      
            }

