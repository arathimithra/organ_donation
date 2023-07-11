from os import path

from django import views
from django.urls import path
from .views import DonorList, AddDonor, LoginSelection, SearchView, SearchProfileView, ProfileUpdate, ProfileDelete
from . import views





urlpatterns = [


path('',views.home,name='home'),
path('logselect', LoginSelection.as_view(), name='all_logins'),
path('list/', DonorList.as_view(), name='list'),
path('search_organ/',views.searchorgan,name='search_organ'),
 path('search/',SearchView.as_view(),name='search-result'),
path('add_donor_details/', AddDonor.as_view(), name='add_donor_details'),
path('search_profile/',views.searchprofile,name='search_profile'),
 path('search2/',SearchProfileView.as_view(),name='search-profile-result'),
path('profileupdate<int:pk>/', ProfileUpdate.as_view(), name='profileupdate'),
path('profiledelete<int:pk>/', ProfileDelete.as_view(), name='profiledelete'),
path('successmessage',views.successmessage,name='successmessage'),
path('deletemessage',views.deletemessage,name='deletemessage'),



    ]