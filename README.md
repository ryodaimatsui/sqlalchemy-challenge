# SQLAlchemy-Challenge
![thomas-ashlock-7G5dkthFyxA-unsplash](https://github.com/ryodaimatsui/sqlalchemy-challenge/assets/137141385/ca12adea-5310-4419-8255-d1d5d459c205)

This particular challenge encompasses two parts: 
- First, an analysis and data exploration of a SQLite database containing data pertaining to the climate in Hawaii.
- Second, the creation of an API utilizing Flask.

The first part of the challenge entails, first and foremost, the creating of an engine to connect to the database file. Following this, the method, 'automap_base()' is assigned to a variable titled 'Base.' The database is reflected into a new model using the engine and the Base. By doing so, we are able to access the tables within the database which is saved into variables for easy access. Upon completion of these steps, we can finally begin querying the data for our specific objectives by creating a session which links the database to the specific python file in use. 

For this specific challenge, we are to find the most recent date, calculate the date a year from this most recent date, and retrieve the data values associated with the precipitation (inches) and its corresponding date for the entire year. In other words, the precipitation levels from August 23, 2016 through to August 23, 2017. Having retrieved these data points, a dataframe is created in order to plot the data using Matplotlib as seen in the following image.

<img width="623" alt="Screenshot 2023-09-09 at 17 42 11" src="https://github.com/ryodaimatsui/sqlalchemy-challenge/assets/137141385/519e28ec-b4e9-4f88-bc3b-b16f8741eb2e">

In addition to this, we are also tasked with find the most active station in the database (out of 9 total stations) and find the temperature observation data for this particular station for the entire year. We follow the previous steps and plot a histogram:

<img width="620" alt="Screenshot 2023-09-09 at 17 45 38" src="https://github.com/ryodaimatsui/sqlalchemy-challenge/assets/137141385/bd0d6643-a165-41e8-b406-3bfff065fe8e">

The second part of the challenge, as aforementioned, entails the development of 6 distinct routes for an API. These include:
- the 'about' route, which serves as the main page that directs users to the different sub-routes availble.
- 'precipitation' route, which lists the date and precipitation levels for a given year.
- 'stations' route, listing all nine stations.
- 'tobs' route, listing the date and temperature for a given year.
- 'start_date' route, which is a dynamic route designed to retrieve the min, avg, and max temperatures for a given start date chosen by the user.
- and finally, a 'start_date/end_date' route, which is another dynamic route similar to the previous one, only this time the user defines the start and end dates. 
