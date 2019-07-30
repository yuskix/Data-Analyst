# Ford GoBike System Analysis (July 2018 to June 2019)
## by Yuski X


## Dataset

> Bay Wheels (Ford GoBike) is a regional public bicycle sharing system in the San Francisco Bay Area. It becomes the first regional and large-scale bicycle sharing system deployed in California. As of January 2018, the system had seen nearly 500,000 rides since the launch in 2017 and had about 10,000 annual subscribers. This project explores the Ford GoBike's trip data for public containing approximately 2,289,396 bike rides for a full calendar year (July 2018 to June 2019). The dataset includes info regarding users' general info, bike rental info, etc. After I cleaned the dataset, there are total 2,151,147 data points left. The orginal dataset can be found at the [Ford GoBike](https://www.lyft.com/bikes/bay-wheels/system-data) official website.


## Summary of Findings

> Based on the analysis, I found that there are two types of users using the system: subscribers and customers. They have both similar and differnt behaviors. Subscribers are typically local residents, they use bike for daily commute during the weekdays from 8am to 9am and from 5pm to 6pm. They prefer quick and short rides, and they are using bike to replace daily walking distance to save time. On the other hand, customers are ususally travellers, who rent bike a lot during weekends for tour purpose. In addition, early spring, summer and fall season (March to April, July to October) are relatively more popular than the rest of the seasons for bike rental services. This is probably due to the nicer weather conditions compared to cold winter. Lastly, I check if genders play roles in the analysis. Results demonstrates the similar trends for males and females, except for subscribers, amount of female riders are very consistant through the entire year.


## Key Insights for Presentation

> I focus on the relationship among users' type on the Bike Rental Services in Bay Area. The way I am going to present is based on the amount of users' daily and weekly bike usage. At first, I splited the user into two groups (Customers/Subscribers). Then I analyzed each group's bike rental behaviors during the day and week based on the heatmap (the darker the color, the higher the demand). Lastly, I use boxplot to check ride duration based on the user type to see if there is any behavior difference.