from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class turf(models.Model):
    turf_name = models.CharField(max_length=400, blank=False)
    address = models.CharField(max_length=500)
    location = models.CharField(max_length=1000, blank=True)
    place = models.CharField(max_length=200, blank=True)
    icon = models.ImageField(upload_to='images/', blank=True)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    contact_no = models.CharField(max_length=50)
    s1 = models.CharField(max_length=50, blank=True)
    s2 = models.CharField(max_length=50, blank=True)
    s3 = models.CharField(max_length=50, blank=True)
    s4 = models.CharField(max_length=50, blank=True)
    s5 = models.CharField(max_length=50, blank=True)
    s_count = models.IntegerField(blank=True, default=1)
    g1 = models.CharField(max_length=50, blank=True)
    g2 = models.CharField(max_length=50, blank=True)
    g3 = models.CharField(max_length=50, blank=True)
    g4 = models.CharField(max_length=50, blank=True)
    g_count = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.turf_name


class turf_add(models.Model):
    owner_name = models.CharField(max_length=400, blank=False)
    turf_nm = models.CharField(max_length=400, blank=False)
    address = models.CharField(max_length=500, blank=True)
    sports = models.CharField(max_length=200, blank=True)
    contact_no = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.owner_name


class turf_facility(models.Model):
    turf = models.ForeignKey(turf, on_delete=models.CASCADE)
    f1 = models.CharField(max_length=200, blank=True)
    f2 = models.CharField(max_length=200, blank=True)
    f3 = models.CharField(max_length=200, blank=True)
    f4 = models.CharField(max_length=200, blank=True)
    f5 = models.CharField(max_length=200, blank=True)
    f6 = models.CharField(max_length=200, blank=True)
    f7 = models.CharField(max_length=200, blank=True)
    f8 = models.CharField(max_length=200, blank=True)
    f_count = models.IntegerField(default=1)

    def __str__(self):
        return self.turf.turf_name


class Pricing_chart(models.Model):
    turf = models.ForeignKey(turf, on_delete=models.CASCADE)
    c1 = [('Football', 'Football'),
          ('Cricket', 'Cricket'),
          ('Football & Cricket', 'Football & Cricket'), ]
    s_type = models.CharField(max_length=100, choices=c1)
    c2 = [('Weekday', 'Weekday'),
          ('Weekend', 'Weekend'),
          ('Holiday', 'Holiday'),
          ('Weekday,Weekend,Holiday', 'Weekday,Weekend,Holiday'), ]
    day = models.CharField(max_length=100, choices=c2)
    c3 = [('00:00-06:00', '00:00-06:00'),
          ('00:00-10:00', '00:00-10:00'),
          ('00:00-02:00', '00:00-02:00'),
          ('00:00-05:00', '00:00-05:00'),
          ('00:00-01:00', '00:00-01:00'),
          ('06:00-10:00', '06:00-10:00'),
          ('06:00-12:00', '06:00-12:00'),
          ('06:00-18:00', '06:00-18:00'),
          ('06:00-17:00', '06:00-17:00'),
          ('02:00-06:00', '02:00-06:00'),
          ('10:00-16:00', '10:00-16:00'),
          ('12:00-16:00', '12:00-16:00'),
          ('16:00-18:00', '16:00-18:00'),
          ('17:00-18:00', '17:00-18:00'),
          ('18:00-23:59', '18:00-23:59'),
          ('05:00-09:00', '05:00-09:00'),
          ('09:00-17:00', '09:00-17:00'),
          ('05:00-16:00', '05:00-16:00'),
          ('05:00-18:00', '05:00-18:00'),

          ('05:00-10:00', '05:00-10:00'),
          ('10:00-16:00', '10:00-16:00'),
          ('16:00-18:00', '16:00-18:00'),
          ('16:00-23:59', '16:00-23:59'),
          ('18:00-19:00', '18:00-19:00'),
          ('19:00-23:59', '19:00-23:59'),
          ('18:00-23:59', '18:00-23:59'),
          ('00:00-23:59', '00:00-23:59'), ]
    timing = models.CharField(max_length=100, choices=c3)

    c4 = [('₹1200/hour', '1200'),
          ('₹1000/hour', '1000'),
          ('₹1300/hour', '1300'),
          ('₹1500/hour', '1500'),
          ('₹1800/hour', '1800'),
          ('₹0800/hour', '0800'),
          ('₹0900/hour', '0900'),
          ('₹0700/hour', '0700'),
          ('₹3000/hour', '3000'),
          ('₹2000/hour', '2000'),
          ('₹3600/hour', '3600'),
          ('₹1100/hour', '1100'),
          ('₹1400/hour', '1400'),
          ('₹1700/hour', '1700'),
          ('₹0400/hour', '0400'),
          ('₹0500/hour', '0500'),

          ]
    price = models.CharField(max_length=100, choices=c4)

    def __str__(self):
        return self.turf.turf_name

class Booking_slot3(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    t_name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    s_time=models.CharField(max_length=100)
    e_time=models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    s_type=models.CharField(max_length=50)




    def __str__(self):
        return self.user.username




class  M_Host(models.Model):
    t1_name=models.CharField(max_length=100)
    t2_name=models.CharField(max_length=100,blank=True)
    date=models.CharField(max_length=50)
    s_time=models.CharField(max_length=50)
    e_time=models.CharField(max_length=50)
    s_type=models.CharField(max_length=100,default=0)
    turf_name=models.CharField(max_length=100)
    no_pl=models.IntegerField(default=5)


    def __str__(self):
        return self.t1_name
