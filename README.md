# CalorieTracker

#### Latest version updated on:Friday, September 23, 2022
#### By :

LARVINE ASANDE

## Description
This application  tracks your weight and calculates a recommended daily calorie intake. 
In addition, it shows your remaining recommended intake and the number of calories you’ve burned during the day.Provides a clear picture of how many calories you’ve consumed during the day.

## User Story / features
* Sign in with the application to start using.
* Set up a personal profile.
* User can set a goal for calories consumed in a day.
* User can track the amount of calories consumed in a day.
* User can track the type of food consumed in a given day.
* User can add food consumed to check on calories.
* User can search on the food entered earlier.
* User can select on food consumed to get a summary of food consumed in that day.

##  Live Link 
https://calorie-app2022.herokuapp.com/

## Technologies Used
- Visual Studio used as  the source code editor.
- Git and Github were used as my local and online repositories respectively.
- HTML 
- CSS 
- [Bootstrap](https://www.bootstrapcdn.com/)
- [Python3.8](https://www.python.org/)
- [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)
- Heroku (deployment)

## Setup and Installation 
##### Clone the repository: 
 ```bash
https://github.com/asandelarvine/calorieTracker
```
##### Navigate into the folder and install requirements 
 ```bash
cd calorie-tracker, pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations calorie
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.

####  Admin Dashboard

  [Admin Dashboard Login () with credentials]
  
       username : plp2
       
       password : plp@123


## Known Bugs
.
  * User has to login in the Dashbord first to set up his/her profile .

### Behaviour Driven Development [BDD]

  * The program displays login/signup page.
    Given: User login
    When: Home page is displayed with it's content.
    Then: User can change profile,add food,select food and make updates or delete.
    Calorie calculation.
      

  * Admin site should be displayed when "admin/" url is choosen.
    Given: An admin url
    When: User enters admin url in browser
    Then: Admin Login is displayed.

  * User authentication occurs when Admin tries to Login
    Given:Admin page is accessed
    When: User tries to login
    Then: User details are authenticated to confirm if user is an admin

  * User session should end when logout url is chosen
    Given:Logout option is given
    When: User chooses logout option
    Then: User session is ended


### Support and Contact details.

    Incase of any concerms,ideas or queries feel free to contact me through email:asandelarvine@gmail.com

