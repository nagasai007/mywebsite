from rest_framework import serializers

from farms.models import house_hold,persons_info,farm_info,season_info,well_info,well_observation,crops,farm_yield

#Django provides both Form classes and ModelForm classes, REST framework includes both Serializer classes, and ModelSerializer classes.
#It's important to remember that ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:
class householdserializer(serializers.ModelSerializer):
	class Meta:#Meta defines database name...etc
		model=house_hold#Define the model
		#fields='__all__'
		fields=('id','mon_income','point','links')#Fields  should be in the same order as in your database

class personsinfoserializer(serializers.ModelSerializer):
	class Meta:
		model=persons_info
		#fields='__all__'
		fields=('id','house_id','name','gender','DOB')

class farminfoserializer(serializers.ModelSerializer):
	class Meta:
		model=farm_info
		#fields='__all__'
		fields=('id','house_id','poly','area')

'''class farmlocationserializer(serializers.ModelSerializer):
	class Meta:
		model=farm_location
		#fields='__all__'
		fields=('id','farm_id','sequence_no','lat','lon')
'''
class cropserializer(serializers.ModelSerializer):
	class Meta:
		model=crops
		#fields='__all__'
		fields=('id','farm_id','crop','crop_area')

class seasoninfoserializer(serializers.ModelSerializer):
	class Meta:
		model=season_info
		#fields='__all__'
		fields=('id','farm_id','season','crop','area')


class wellinfoserializer(serializers.ModelSerializer):
	class Meta:
		model=well_info
		#fields='__all__'
		fields=('id','farm_id','lat','lon','depth_in_meters','Avg_wateryield')

class wellobservationserializer(serializers.ModelSerializer):
	class Meta:
		model=well_observation
		#fields='__all__'
		fields=('id','well_id','date_of_observation','well_id','wateryield')

class farmyieldserializer(serializers.ModelSerializer):
	class Meta:
		model=farm_yield
		#fields='__all__'
		fields=('id','farm_id','Yield')
