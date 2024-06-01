#Pest Data Project Analysis Summary

#Introduction:
This report examines a pest population dataset collected across various locations in India (1959-2011). It investigates potential relationships between weather conditions and pest activity for ten pest species:

Gall Midge
Brownplanthopper
Greenleafhopper
LeafFolder
Yellowstemborer
Caseworm
Mirid Bug
ZigZagleafhopper
LeafBlast
NeckBlast


#Objective:
The primary objective is to gain insights that can inform pest management strategies across Indian regions.



#Data Analysis:

Data Import: Data imported into a relational database (RDBMS) and stored in the "PESTDATA" table.

#Table Schema:


Observation Year (INT)
Standard Week (INT)
Pest Value (INT)
Collection Type (VARCHAR(20))
Weather Parameters (MAXT, MINT, RH1, RH2, RF, WS, SSH, EVP)
Pest Name (VARCHAR(20))
Location (VARCHAR(20))
Feature Engineering:
Standardized state names based on locations (e.g., Cuttack to ODISHA).
Added a "SEASON" column categorizing observations (Summer, Monsoon, etc.).
Calculated interaction terms:
TEMP_PEST_INTERACTION (MAXT * PESTVALUE)
RAINFALL_PEST_INTERACTION (RF * PESTVALUE)
Added an auto-incrementing ID column (primary key).
Calculated:
Average Relative Humidity (HUMIDITY_AVG)
Temperature Difference (MAXT - MINT)


#Data Cleaning After Transformation:
No null values were found in any column after data transformation.


#About the Data:
This report explores a dataset on pest populations collected across various locations in India from
1959 to 2011

#Data Exploration:
Total Observations: 17636 (using SELECT COUNT(*) FROM PESTDATA;)
Observation Years: 48 (using SELECT COUNT(DISTINCT(OBSERVATIONYEAR)) FROM PESTDATA;)
Distinct Pest Names: Identified using SELECT DISTINCT(PESTNAME) FROM PESTDATA;
Pest Species per Location: Determined using SELECT LOCATION, COUNT(PESTNAME) FROM PESTDATA GROUP BY LOCATION;
Basic Descriptive Statistics:
Total Records: 17636
Locations/States: ANDHRA PRADESH, CHHATTISGARH, Himachal Pradesh, MANIPUR, ODISHA, PUNJAB
Observation Years: 48
Seasons: MONSOON, WINTER, SUMMER, POST-MONSOON
Temperature Summary by State: Provides Min/Max values for each state.
Distribution of Pest Values by Location: Shows average pest value per location.


#Questions for Further Analysis:
Pest Value Variation Across Locations: How does average pest value vary across locations?
Maximum Temperature vs. Average Pest Value
Seasonal Pest Value Variation: How does average pest value vary across seasons for each year?
Rainfall Impact on Summer Pest Value: Does rainfall affect average pest value during summer?
Weather Variables and Pest Value Over Time: How do weather variables and average pest value change across standard weeks?
Average Relative Humidity for High Pest Values: What is the average relative humidity for observations with pest values above the average?
Weather Variables and Pest Value Throughout the Year: How do weather variables and average pest value change across standard weeks?
Season with Highest Average Pest Value: Which season has the highest average pest value?
Weather Variable Variation Across Locations: How do average weather variables vary across different locations?
Pest Species with Highest Maximum Pest Value: Which species has the highest maximum pest value across all states?
Location-Specific Questions: Analyze pest value distribution and relationships with weather variables for each location (Cuttack, Maruteru, etc.).
Sunshine Hours and Pest Value: Is there a relationship between sunshine hours and average pest value?
Highest Total Pest Value by Year: Which five years have the highest total pest value?
Highest Total Pest Value by Location: Which five locations have the highest total pest value summed across all observation years?


#Future Considerations:
The data we have is a good starting point, but it's not enough to say for sure how weather affects pests. By looking at all the data instead of just a small piece, and using tools like pie charts and graphs, we can get a clearer picture of how weather affects pests.








THANK YOU


# Pestdata_Analysis
