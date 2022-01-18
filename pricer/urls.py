"""pricer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import excel.views
import login.views
import account.views
from django.conf.urls.static import static
from django.conf import settings
#from pricer import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/login')),
    path('admin/', admin.site.urls),
    path('excel/', excel.views.index),
    path('login/', login.views.login, name="login"),
    path('logout/', login.views.user_logout, name="logout"),

    #Profile
    path('profile/', account.views.brands),
    path('profile/products/', account.views.index),

    path('profile/brands/', account.views.brands),
    path('profile/brand/delete/<int:pk>/', account.views.brand_delete),
    path('profile/rules/<int:loader_id>', account.views.rules),
    path('profile/brands/add/', account.views.addbrand),
    path('profile/brands/show/<int:id>/', account.views.showBrand),
    path('profile/loader/show/<int:id>/<int:sheet_id>/', account.views.show_loader, name="loader_show_sheet"),
    path('profile/loader/show/<int:id>/', account.views.show_loader, name="loader_show"),
    path('profile/loader/matching/<int:id>/', account.views.save_matching),
    path('profile/loader/add/', account.views.add_loader),
    path('profile/load-file/<int:id>/<int:sheet_id>/', account.views.run_file),
    path('profile/run/<int:rule_id>', account.views.run_file_new),
    # Attributes
    path('profile/attributes/replacement/', account.views.show_attributes_page),
    path('profile/attributes/replacement/all/', account.views.get_all_replacemtns),
    path('profile/attributes/replacement/delete/', account.views.delete_replacemtns),


    path('profile/add-rule/<int:brand_id>/<int:loader_id>/<slug:type>/', account.views.add_rule),

    path('profile/rule/save/', account.views.save_rule),

    path('profile/products/remove/<int:id>/', account.views.rem_one_product),

    # Edit product
    path('profile/product/edit-ajax/', account.views.edit_product_ajax),
    path('profile/replacement/edit-ajax/', account.views.edit_replacement_ajax),
    path('profile/product/edit/<int:id>/', account.views.edit_product),


    path('profile/remove/<int:id>/', account.views.rem_products),

    path('profile/remove/', account.views.rem_products),
    path('profile/products/remove-by-brand/<str:name>/', account.views.rem_products),
    path('profile/loader/remove/<int:id>/<int:brand_id>', account.views.rem_loader),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
