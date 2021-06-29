
# Vaccine Priority Tracker
A relevant application of supervised learning. Linear Regression is used to predict vaccine supply within Canada based on the current rate of vaccinations within each province. 
!Note: All sections of this readME file are currently subject to change as the project is still underway. 

<hr>

## Inspiration 
I was inspired to build something relating to the COVID-19 vaccine rollout after I got my vaccine and listening from several sources that they had no access to vaccines where they are in the country. Because I know vaccines are distributed under the federal government's hand, it led me to believe that the government is not accurately distributing vaccines to the provinces in a way for all of them to get their largely differing populations vaccinated and the same, or at least simialr, rates. I was inspired to track how much of each province's population has been getting vaccinated over time to make suggestions based on what provinces should receive more vaccines in order to make access to the vaccine more fair across the country. 

## How it works
<a href="https://github.com/Lujaina-E/Supervised-Learning-Predictions/blob/main/COVID%20Vaccine%20Rate%20Predictor%20Action%20Plan.pdf">Planning Page</a>

 <a href="https://health-infobase.canada.ca/covid-19/vaccination-coverage/">Data Retrieval</a> - CSV document "National Vaccine Coverage"

## Challenges
- Importing proper data that fit the criteria of what I needed to achieve my main goal as orginally planned
- Understanding and accounting for every pattern within the data by myself
- Scaling the data properly to account for the oustanding vaccine percentage of the Northwest Territories and Nunavut as their trendline lines gave negative [impossible] values (I later realized there would be no proper way to graph a trendline for these territories without ruining the data, so I made a seperate graph for just the three territories)

## What I learned
Planning out the project beforehand, especially when regression is involved, is very helpful because I won't know what kind of data I'm be exposed to. Preprocessing my acquired data and making it more suitable was also a valuable skill I learned as many hours were spent on Excel filtering and sorting the data to ensure I would only get the values I needed and that the values used would give me the prediction results that I was expecting(percentages gave accurate results.) This required me to truly understand all the nitty-gritty details of my project, and the importance of always keeping the end goal in mind but being open to changes along the way. 

I also learned the details of how to interpret the data that I'm using, and the slope of the line of best fit. This was especially apparent because I had to be able to isolate the x-values of the intersection point of different lines to be able to decide what demographic the program should suggest increased exposure to the vaccine for. 
How important it is to fully undertand the data, problem, and what my data means to me at every step along the way because it is easy to get lost in the numbers and forget what it all means. 

<hr>

## Features for the Future
- Pulling live data from the "Health Infobase Canada" website and CSV document
- Finding some way to write the time values as dates rather "days since ..."
- More specific suggestions. For example: increase vaccinations by 30%
- Make the intersectional analysis more multi-dimensional and allow it to account for all patterns rather than just intersections
