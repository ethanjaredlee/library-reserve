# library-reserve
## Automates library room reservation process at Northwestern University
### Install Packages
This program uses Splinter to navigate through web pages and APScheduler to run the program on a scheduled basis. To install, run:

`pip install requirements.txt`

## Splinter allows a user to navigate through a web page enabling the automation of clicking links and filling out forms with information
I used this ability to register my email and 3 friend's emails to reserve a library room as a normal student would, only the entire process is controlled by this script

## APScheduler allows a user to run a function periodically
The main script function will only run once every day, allowing a library room to be reserved as soon as it opens up. 

## Limitations
Currently can't specify which library room you would like to reserve due to crude implementation and unpredictable pattern of what rooms might already be reserved and reservation dates. 

## Future Development
* Specify which room to reserve
* Send an email or notification if reservation process of the room fails
