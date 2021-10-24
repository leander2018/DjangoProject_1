from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 # path('location',views.location,name='location'),
 path('new_turf',views.new_turf,name='new_turf'),
 path('turf_view',views.turf_view,name='turf_view'),
path(r'turf_booking/(?P<id>\w+)',views.turf_booking,name='turf_booking'),
path('turf_booking2',views.turf_booking2,name='turf_booking2'),
path('turf_booking3',views.turf_booking3,name='turf_booking3'),
path('bookings',views.bookings,name='bookings'),
path('Match_host',views.Match_host,name='Match_host'),
path('Match_host2',views.Match_host2,name='Match_host2'),
path('Match_host3',views.Match_host3,name='Match_host3'),
path('Join_match',views.Join_match,name='Join_match')


]