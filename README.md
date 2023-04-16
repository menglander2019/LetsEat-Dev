# LetsEat-Dev
The development repository for the senior capstone design project called LetsEat, a machine learning-powered restaurant recommender.


# Command Line Test
1. In the root of the file directory, there is a file called cmd-line-test.py, this will install all of the dependencies for you if you want to.
2. If you use the docker setup, it will automatically install all of the dependencies inside the docker images. 

# Web address
1. If you want to run the application locally, you need to change the web addresses to localhost
2. In the folder react->letseat-app->src-> WebsiteURL.js and WebsiteURLFront.js, change the url to localhost (keep the port numbers at the end)
3. In app.py (root of folder structure), change the origins to localhost (keep the port numbers)

# Database
1. Our database is hosted on RDS, if you want to host one locally, use MySql
2. The database configuration is in backend->db->db_schema.sql
3. To change the database variables, change the config in backend->db->db_management.py
4. If you want to run docker, you will have to change the docker-compose.yml file database variables in the root of the folder structure

# Docker
1. Install Docker Desktop
2. Install Docker - pip install docker
3. Run docker-compose up --build
4. The backend and frontend images should both be running
5. Once thats done, you should have a running application, go to the web address to see it (make sure port 3000 is at the end)
6. To take the application down, run docker-compose down

# Ideas for Future Projects:

Partnership with a company like Yelp that collects this data so it is applicable to more restaurants
Pipeline/Scheduled SQS of AWS lambda scraping to EC2 instance so we are automatically updating restaurant information
Functionality for users to rate restaurants they indicate they are attending and use this data to retrain the machine learning model
Use REACT Native to create a mobile-friendly app for the Apple App Store and/or Google Play Store
During the restaurant recommendation process, ask the user more specific questions to get more specific recommendations. Example questions include parking information, travel information, and more details about allergies/restrictions

# Ideas for Next Steps:

Partner with reservation company (like OpenTable or Resy), so after users get a recommendation, they can make a reservation for that restaurant at their selected time.
Distribute a LetsEat Newsletter to promote new restaurants and features. This can also allow for ads as a revenue method.
Partner with restaurants to have a featured restaurants section. This can act as a revenue method.