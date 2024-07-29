from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('add_product',views.add_product,name='add_product'),
   path('show_product',views.show_product,name='show_product'),
   path('updatepage/<int:pk>',views.updatepage,name='updatepage'),
   path('update_product/<int:pk>',views.update_product,name='update_product'),
   path('deletepage/<int:pk>',views.deletepage,name='deletepage')


]