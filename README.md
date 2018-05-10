# data_viz_project

## this is a readme for the data visualization project
### by: Baiyue cao (bc1561) 

#### Objective: 
This project aims to visualize 311 complaints in new york city in May in 2015. Because of the large size of the dataset, we choose to use May 2015 as a sample for our following visualization. This project is a trial example for my 311 capstone project visualizations. 

the visualization will help people to better visualize the spatial distribution of specific complaint types, as well as helping people to identify the cyclicatity of the complaints. 

#### Data: 
311 complaint data from 2015 May. 

#### Visual Choices: 
The visualization we created will show 1. a scatter map with the chosen complaint category from the drop down menu in a single day. and 2. a line plot showing the time series of the chosen complaint type, as well as a trend line showing the overall trend of the complaint type in May 2015. 

The drop down menu will provide a easy way for people to interact with the plot, selecting the complaint type they want to visualize. The day slider that helps updating the map will give user a sense of how the map changes over a time line. 

The line plot with both actual data and trend analysis, which are generated by taking a rolling mean, will show users how complaints numbers change through out time, as well as showing growing or shrinking trends of the complaints. 

The map we generated will give a straight forward sense of where complaints of chosen type are clustered at each day, which would allow users to identitfy where the complaints are coming from and how that can be related to different neighborhoods. 

#### Outcome: 
The visualizatio will help users to understand 311 data much better. The combination of the map and time series plot gives the user a sense of how complaints change with both spatial and temporal perspecitves. It will serve as a great data exploratory tool for users to identify potential research problems using 311 data. 

In the future, as we move all data onto carto (our backend), we will be able to add more dimensions, such as yearly trends and neighborhood aggregation (which are difficult to do currently because plotly dash has a bug with creating choropleth). 

#### Note: 
app4.py is the choropleth version of the project that has problem updating the map. 
app6.py is the final version of our project that has a map that allows interation by creating scatter maps. 
