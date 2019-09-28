## We have two use problems to show
1. User makes a query from the visualization and gets a prediction on that region
    - Input:
        - Date and time e.g. 2019-04-01 01:00:00+00:00
        - Polygon e.g. POLYGON((42. 7.),(...))
        - Event info for all the days and previous two days in Basel 
        - Weather info for that day and previous two days
               - (min,max,mean) Temerature, (total_prep) precipitation and (max_wind) wind
        - What day it is: Monday, Tuesday, ...?
        - Place type: 
2. Scores for all the regions on the test dataset