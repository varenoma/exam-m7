from django.urls import path

from .views import FAQCreateView, RequirementCreateView


urlpatterns = [
    path('create/faq', FAQCreateView.as_view(), name='create-FAQ'),
    path('create/requirement', RequirementCreateView.as_view(),
         name='create-Requirement')
]
