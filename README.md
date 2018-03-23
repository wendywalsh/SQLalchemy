<!--lint disable no-heading-punctuation-->
# SQLAlchemy
<!--lint enable no-heading-punctuation-->

<img src='images/surfs-up.jpeg' />

### Plan your vacation dates to Honolulu, Hawaii based on weather analysis based on daily percipitation and temperature analysis. A web application was created to allow for independent inquiries into Honolulu weather.

#### Data and Analysis:
- Initial data from two csv files.
- Pandas use to clean and manipulate data.
- SQLAlchemy used to model table schemas and create database.
- Analysis created on each weather recording station, percipitation rates, and temperature.
---

---


#### Climate App

Flask api based on the queries that you have just developed.


- Routes

* `/api/v1.0/precipitation`

  * Query for the dates and temperature observations from the last year.

  * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

  * Return the json representation of your dictionary.

* `/api/v1.0/stations`

  * Return a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Return a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

Author: Wendy Walsh

Acknowlegements: UT Austin Data Analytics Boot Camp Oct 2017
