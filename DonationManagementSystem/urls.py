"""
URL configuration for DonationManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.Home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path

from DonationManagementSystem import views
from django.urls import path
from DonationManagementSystem.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('logins/', all_logins, name='all_logins'),
path('donor_login', donor_login, name='donor_login'),
path('volunteer_login', volunteer_login, name='volunteer_login'),
path('admin_login', admin_login, name='admin_login'),
path('admin_home', admin_home, name='admin_home'),
path('donor_registration', donor_registration, name='donor_registration'),
path('volunteer_registration', volunteer_registration, name='volunteer_registration'),
path('donor_home', donor_home, name='donor_home'),
path('volunteer_home', volunteer_home, name='volunteer_home'),
path('logout/', Logout, name='logout'),
path('donate_now/', donate_now, name='donate_now'),
path('donation_history/', donation_history, name='donation_history'),
path('pending_donation', pending_donation, name='pending_donation'),
path('view_donationdetail/<int:pid>', view_donationdetail, name='view_donationdetail'),
path('accepted_donation', accepted_donation, name='accepted_donation'),
path('add_area', add_area, name='add_area'),
path('manage_area', manage_area, name='manage_area'),
path('edit_area/<int:pid>', edit_area, name='edit_area'),
path('delete_area/<int:pid>', delete_area, name='delete_area'),
path('manage_donor', manage_donor, name='manage_donor'),
path('view_donordetail/<int:pid>', view_donordetail, name='view_donordetail'),
path('delete_donor/<int:pid>', delete_donor, name='delete_donor'),
path('new_volunteer', new_volunteer, name='new_volunteer'),
path('view_volunteerdetail/<int:pid>', view_volunteerdetail, name='view_volunteerdetail'),
path('accepted_volunteer', accepted_volunteer, name='accepted_volunteer'),
path('rejected_volunteer', rejected_volunteer, name='rejected_volunteer'),
path('all_volunteer', all_volunteer, name='all_volunteer'),
path('delete_volunteer/<int:pid>', delete_volunteer, name='delete_volunteer'),
path('accepted_donationdetail/<int:pid>', accepted_donationdetail, name='accepted_donationdetail'),
path('collection_req', collection_req, name='collection_req'),
path('donationcollection_detail/<int:pid>', donationcollection_detail, name='donationcollection_detail'),
path('donationrec_volunteer', donationrec_volunteer, name='donationrec_volunteer'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
