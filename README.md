# Supervised-Learning-Predictions
A collection of regression algorithm applications (linear and complex), including examples and applications



<hr>




# Vaccine Priority Tracker

!Note: All sections of this readME file are currently subject to change as the project is still underway. 

## Inspiration 
I was inspired to build something relating to the COVID-19 vaccine rollout after I got my vaccine and listening from several sources that they had no access to vaccines where they are. This personally bothered me as I know vaccine arrival to Alberta is central, and so the problem is clearly within the dispersion system from AHS to local hospitals and pharmacies across zones, as well as the priority through which age groups are able to book vaccines fairly. 

## How it works
<a href="https://github.com/Lujaina-E/Supervised-Learning-Predictions/blob/main/ML%20COVID%20Vaccine%20Rate%20Predictor.pdf">Planning Page</a>

 <a href="https://health-infobase.canada.ca/covid-19/vaccination-coverage/">Data Retrieval</a>   CSV document "National Vaccine Coverage"

## Challenges
- Importing proper data that fit the criteria of what I needed to achieve my main goal as orginally planned
- making sure the data was in a proper format before I input it (csv file, dates were written as numbers rather than date form)
- isolating the slope and comparing it against the slope of the other line after pulling data 

## What I learned
Planning out the project beforehand, especially when regression is involved, is very helpful because I won't know what kind of data I'm be exposed to. I also editted my docuemnt continuously to ensure I didn't stray off from my original goal when I had to fix my planning to account for challenges I wasn't expecting (eg. not finding precisely the type of data I was expecting to) Micromanaging the data and making it more suitable for the graphs that I am making was also a valuable skill I learned as many hours were spent on Excel filtering and sorting the data to ensure I would only get the values I needed and that the values used would give me the prediction results that I was expecting(percentages gave accurate results.) This required me to truly understand all the nitty-gritty details of my project, and the importance of always keeping the end goal in mind but being open to changes along the way. 

I also learned the details of how to interpret the data that I'm using, and the slope of the line of best fit. This was especially apparent because I had to be able to isolate the x-values of the intersection point of different lines to be able to decide what demographic the program should suggest increased exposure to the vaccine for. 

## Features for the Future
- Pulling live data from the "Health Infobase Canada" website and CSV document
- Finding some way to write the time values as dates rather "days since ..."
