## Inspiration

Garbage collection today is conducted on a fixed schedule chosen on human's bias observation. This creates problems when there are events such as concerts where lots of garbage accumulates which may not be cleared until the next garbage collection schedule. This project addresses the problem by predicting a city cleaning index (CCI) for every street and venue around the city. This prediction is made from publicly available data, such as previous events, weather and day characteristics. With this information, the sweeper company is able to develop an optimal schedule and clean the city when needed. Thus, avoiding redundancy around cleaning and ensuring a cleaner city.

## Setup
The server setup can be found under `garbage_backend`

## Dataset info
The dataset is based on three components:
1. Image based data provided by BUCHER Municipal AG from [here](https://www.dropbox.com/sh/e2e2uljizqou68u/AAAWSOtHb8dTggYBUvUAFK7Oa?dl=0)
2. Weather data taken from [Meteomatics](https://www.meteomatics.com/en/weather-api/)
3. Events data taken from [Eventful](http://api.eventful.com/keys)

A combined dataset can be found under ```./data``` directory.
