# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.utils import LayerMapping
from django.db import models
from django.contrib.gis.db import models


seasons=sorted(["summer","winter","rainy","monsoon"])
seasons=((item,item) for item in seasons)
crop=["paddy","groundnut","maize","sugarcane","turmeric"]
crop=((item,item) for item in crop)
crp=["paddy","groundnut","maize","sugarcane","turmeric"]
crp=((item,item) for item in crp)

class house_hold(models.Model):

	#lat=models.DecimalField(max_digits=15, decimal_places=6)
	#lon=models.DecimalField(max_digits=15, decimal_places=6)
	mon_income=models.IntegerField(default=0)
	point = models.PointField(srid=4326,null=True, blank=True)
	objects=models.GeoManager()
	links=models.CharField(default="gfdxgh", max_length=50)
	def __unicode__(self):
		return '%s'%(self.id)

class persons_info(models.Model):
	house_id = models.ForeignKey(house_hold,on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	gender=models.CharField(max_length=2)
	DOB=models.DateField(null=True)
	def __unicode__(self):
		return '%s'%(self.name)

class farm_info(models.Model):
	house_id = models.ForeignKey(house_hold,on_delete=models.CASCADE)
	poly = models.PolygonField(default="")
	objects=models.GeoManager()
	#lat=models.DecimalField(max_digits=15, decimal_places=6)
	#lon=models.DecimalField(max_digits=15, decimal_places=6)
	area=models.DecimalField(max_digits=6, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.id)
'''class farm_location(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	sequence_no=models.IntegerField(default=0)
	lat=models.DecimalField(max_digits=15, decimal_places=6)
	lon=models.DecimalField(max_digits=15, decimal_places=6)
	def __unicode__(self):
		return '%s'%(self.farm_id)

'''
class crops(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	crop=models.CharField(choices=crp,default="paddy", max_length=20)
	crop_area=models.IntegerField(default=0)
	def __unicode__(self):
		return '%s'%(self.farm_id)

class season_info(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	season=models.CharField(choices=seasons,default="summer", max_length=20)
	crop=models.CharField(choices=crop,default="paddy", max_length=20)
	area=models.DecimalField(max_digits=6, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.farm_id)


class well_info(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	lat=models.DecimalField(max_digits=15, decimal_places=6,default=0.0)
	lon=models.DecimalField(max_digits=15, decimal_places=6,default=0.0)
	#point = models.PointField(srid=4326,null=True, blank=True)
	#objects=models.GeoManager()
	depth_in_meters=models.DecimalField(max_digits=6, decimal_places=2)
	Avg_wateryield=models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.id)



class well_observation(models.Model):
	well_id = models.ForeignKey(well_info,on_delete=models.CASCADE)
	depth_in_meters=models.DecimalField(max_digits=6, decimal_places=2)
	date_of_observation=models.DateTimeField(null=True)
	wateryield=models.DecimalField(max_digits=8, decimal_places=2)
	def __unicode__(self):
		return '%s'%(self.well_id)

class farm_yield(models.Model):
	farm_id = models.ForeignKey(farm_info,on_delete=models.CASCADE)
	Yield = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s'%(self.farm_id)

	

