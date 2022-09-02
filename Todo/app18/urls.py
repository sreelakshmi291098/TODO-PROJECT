from django.urls import path
from app18 import views
urlpatterns=[
    path('',views.index,name='index'),
    path('update',views.update,name='update'),
    # path('form',views.form,name='form'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('<int:id>/formupdate',views.formupdate,name='formupdate'),
    path('delete/<int:id>',views.delete,name='delete'),
]

