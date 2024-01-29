from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('staff/',views.staff,name="staff"),
    path('staff_detail/(?P<pk>)\w+',views.staff_detail,name="staff-detail"),
    path('product/',views.product,name="d-product"),
    path('product_update/(?P<pk>)\w+',views.product_delete,name="product-delete"),
    path('product_delete/(?P<pk>)\w+',views.product_update,name="product-update"),
    path('order/',views.order,name="order"),
    

]
