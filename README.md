## Inspiration

Garbage collection today is conducted on a fixed schedule chosen on human's bias observation. This creates problems when there are events such as concerts where lots of garbage accumulates which may not be cleared until the next garbage collection schedule. This project addresses the problem by predicting a city cleaning index (CCI) for every street and venue around the city. This prediction is made from publicly available data, such as previous events, weather and day characteristics. With this information, the sweeper company is able to develop an optimal schedule and clean the city when needed. Thus, avoiding redundancy around cleaning and ensuring a cleaner city.

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


