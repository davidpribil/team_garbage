## Inspiration

The garbage collection today is based on a schedule basis which does not change. This creates problems when there are events where lots of garbage accumulates which may not be cleared until the next garbage collection schedule. Why not use the data such as events, weather, etc. to predict and schedule the garbage collection in a city?

## Possible features
1. Weather information
	- Using meteomatics python api
2. Weekday/ Weekend/ Holiday
3. Events
	- Create an account and get a key for downloading the event data
	- [Website](http://api.eventful.com/keys)
	- Our API Key - XjCqG5BpRQfvvXzg
	- Browse the events [here](https://eventful.com/events/categories)
4. Social network e.g. Twitter
5. Geolocation of people



## Installation

pip install meteomatics

## Dataset info
The dataset is based on three components:
1. Image data
2. Weather data
3. Events data

A combined dataset can be found under ```./data``` directory.

Day type
	Weekday - 0
	Weekend - 1
	Holiday - 2

Week day
 Monday, Tuesday,... Sunday --> [0,1,..6]

Place type
['bus_stop' 'secondary' 'tertiary' 'residential' 'no type found' 'primary'
'unclassified' 'footway' 'living_street' 'steps' 'cycleway' 'pedestrian'
'path' 'service' 'motorway_link' 'primary_link' 'secondary_link'] --> [0,1,2,...17]


