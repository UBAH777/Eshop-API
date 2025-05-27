from django.urls import path

from . import views


urlpatterns = [
    path("item/", views.ItemListView.as_view())   ,
    path("item/<int:pk>/", views.ItemDetailView.as_view()), 
    path("review/", views.ReviewCreateView.as_view()),
    path("vendors/", views.VendorsListView.as_view()),
    path("vendors/<int:pk>/", views.VendorsDetailView.as_view()),
    path("category/", views.CategoriesListView.as_view()),
    path("category/<str:url>/", views.CategoriesDetailView.as_view()),
]
