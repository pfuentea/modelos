from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('second/<name>', views.second),
    path('wizards/', views.wizards ),
    path('wizard-create/', views.wizardsnew),
    path('wizard-update/<int:p_id>', views.wizardsedit),
    path('wizard-delete/<int:p_id>', views.wizardsdelete ),   
    
]
