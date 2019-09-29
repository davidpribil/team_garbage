## Inspiration

Garbage collection today is conducted on a fixed schedule chosen on human's bias observation. This creates problems when there are events such as concerts where lots of garbage accumulates which may not be cleared until the next garbage collection schedule. This project addresses the problem by predicting a city cleaning index (CCI) for every street and venue around the city. This prediction is made from publicly available data, such as previous events, weather and day characteristics. With this information, the sweeper company is able to develop an optimal schedule and clean the city when needed. Thus, avoiding redundancy around cleaning and ensuring a cleaner city.

## Project details
Please check the project info on [Devpost](https://devpost.com/software/team_garbage)

## Setup
1. The server setup can be found under `garbage_backend` [here](https://github.com/davidpribil/team_garbage/tree/master/garbage_backend)
2. Setting up a [conda environment](https://www.anaconda.com/distribution/) to train the model:
```
git clone https://github.com/davidpribil/team_garbage # Clone this repo
cd team_garbage
conda create -n new environment --file requirements.txt ## Based on anaconda3
```

## Dataset info
The dataset is based on three components:
1. Image based data provided by BUCHER Municipal AG from [here](https://www.dropbox.com/sh/e2e2uljizqou68u/AAAWSOtHb8dTggYBUvUAFK7Oa?dl=0)
2. Weather data taken from [Meteomatics](https://www.meteomatics.com/en/weather-api/)
3. Events data taken from [Eventful](http://api.eventful.com/keys)

A combined dataset can be found under ```./data``` directory.

## URL to webservice
You can see the webservice at [CleanPath](http://ec2-52-31-147-235.eu-west-1.compute.amazonaws.com:8000/map/)
