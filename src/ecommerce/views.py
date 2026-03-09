from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import  HttpResponseRedirect
from .models import ProductModel
from django.shortcuts import get_object_or_404
from .forms import ProductModelForm
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView

#Views class
class ProtectedListView(LoginRequiredMixin, ListView):
    model = ProductModel
    template_name = "ecommerce/products/my_products.html"
    context_object_name = "products"

    def get_queryset(self):
        return ProductModel.objects.filter(seller=self.request.user)


class MyProductsRedirectView(RedirectView):
    pattern_name = "my-products"

# Create your views here.
#DELETE
def product_model_delete_view(request, product_id=None):
    instance=get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Producto eliminado")
        return redirect("list")
    context={
        "product":instance
    }
    template="ecommerce/delete-view.html"
    return render(request, template, context)

#UPDATE
def product_model_update_view(request, product_id=None):
    instance=get_object_or_404(ProductModel, id=product_id)
    form=ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        messages.success(request, "Producto actualizado con éxito")
        return redirect("detail", product_id=instance.id)
    context={
        "form":form
    }
    template="ecommerce/update-view.html"
    return render(request, template, context)

#CREATE
def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.seller = request.user
        instance.save()

        messages.success(request, "Producto creado con éxito")
        return redirect("detail", product_id=instance.id)

    return render(request, "ecommerce/create-view.html", {"form": form})

#DETAIL
def product_model_detail_view(request, product_id):
    instance =get_object_or_404(ProductModel, id=product_id)
    context={
        "product":instance
    }
    template="ecommerce/detail-view.html"
    return render (request, template, context)

def login_required_view(request):
    queryset=  ProductModel.objects.all()
    #print(queryset)
    template="ecommerce/list_view.html"
    context={
        "products":queryset
    }
    if request.user.is_authenticated:
        template="ecommerce/list_view.html"
    else:
        template="ecommerce/list_view_public.html"
    return render(request, template, context)

#@login_required(login_url="/login")
#LIST
def product_model_list_view(request):
    queryset=  ProductModel.objects.all()
    query=request.GET.get("q", None)
    if query is not None:
        queryset=queryset.filter(
            Q(title__icontains=query)|
            Q(price__icontains =query)
            )
    template="ecommerce/list_view.html"
    context={
        "products":queryset
    }
    #if request.user.is_authenticated:
    template="ecommerce/list_view.html"
    #else:
    #    template="ecommerce/list_view_public.html"

    return render(request, template, context)
