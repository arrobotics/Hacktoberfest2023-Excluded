# Python program for the conversion 
# kmph to mph and vice versa 

# Function to convert kmph to mph 
def kmphTOmph(kmph): 
	mph = 0.6214 * kmph 
	return mph 

# Function to convert mph to kmph	 
def mphTOkmph(mph): 
	kmph =(float)(mph * 1.60934) 
	return kmph 


kmph = 150
mph = 100
print "speed in miles / hr is ", kmphTOmph(kmph) 

print "speed in km / hr is ", mphTOkmph(mph) 
