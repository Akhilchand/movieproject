from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
#from matrix_field import MatrixField


# Create your models here.

STATUS = (
            ('S', 'Selected'),
            ('N', 'Not Selected'),) 



class Movie(models.Model):
	movie_name = models.CharField(max_length = 30, null = True, blank = True)
	category = models.CharField(max_length =30, null = True, blank = True)
	release_date = models.DateTimeField('release date', null = True)

	def __unicode__(self):
 		return unicode(self.movie_name)


class MovieDetail(models.Model):
	movie = models.ForeignKey(Movie)
	hero = models.CharField(max_length = 30, null = True, blank = True)
	heroine = models.CharField(max_length = 30, null = True, blank = True)
	director = models.CharField(max_length = 30, null = True, blank = True)
	musicdirector = models.CharField(max_length = 30, null = True, blank = True)
	producer = models.CharField(max_length = 30, null = True, blank = True)

	def __unicode__(self):
 		return unicode(self.movie.movie_name)


class MovieCategory(models.Model):
	id = models.AutoField(primary_key = True)
	movie_category = models.ForeignKey(Movie, null = True)


class UserDetail(models.Model):
	user = models.ForeignKey('auth.user')
	name = models.CharField(max_length = 30, null = True, blank = True)
	first_name = models.CharField(max_length = 30, null = True, blank = True) 
	last_name = models.CharField(max_length = 30, null = True, blank = True)
	address = models.CharField(max_length = 50, null = True, blank = True)
	mobile = models.CharField(max_length = 30, null = True, blank = True)
	mail = models.EmailField(max_length = 50,null = True , blank = True) 

	def __unicode__(self):
 		return unicode(self.user)


class Songs(models.Model):
	movie = models.ForeignKey(Movie)
	track = models.CharField(max_length = 30, null = True, blank = True)


class Booking_info(models.Model):
	movie = models.ForeignKey(Movie)
	show_details = models.CharField(max_length = 30, null = True, blank = True)
	timings = models.DateTimeField('show time', null = True)
	seat_available = models.IntegerField(blank = True, null = True)
	seat_num = models.CharField(max_length = 1000,null = True, blank = True)
	total_seats = models.CharField(max_length = 1000,null = True, blank = True)
	
	def __str__(self):
		return self.movie.movie_name
	

class User_sel(models.Model):
	booking = models.ForeignKey(Booking_info)
	user = models.ForeignKey('auth.user')
	seats = models.IntegerField(blank = True, null = True)
	selected_seats = models.CharField(max_length = 100,null = True, blank = True)

	def __unicode__(self):
 		return unicode(self.user)


class Transaction(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey('auth.user')
	time = models.DateTimeField(default=timezone.now)
	amount = models.DecimalField(blank=True,null=True,default=0,max_digits=10,decimal_places=2)

	def __unicode__(self):
 		return unicode(self.user)

class Seats(models.Model):
	show = models.ForeignKey(Booking_info,null = True, blank = True)
	seat = models.CharField(max_length = 100,null = True, blank = True)
	seat_status = models.BooleanField(default = False,)
	user = models.ForeignKey('auth.user')
	cost_of_ticket = models.DecimalField(blank=True,null=True,default=0,max_digits=10,decimal_places=2)


	def __str__(self):
		return self.show.movie.movie_name

class BookingTransactions(models.Model):
	seat = models.ForeignKey(Booking_info,null = True, blank = True)
	seat_selected = models.CharField(max_length = 100,null = True, blank = True)
	user = models.ForeignKey('auth.user')
	amount = models.DecimalField(default=0,max_digits=10,decimal_places=2)

	def __str__(self):
		return self.seat.movie.movie_name

