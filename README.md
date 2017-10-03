# library-reserve
## Automates library room reservation process at Northwestern University
### Install Packages
This program uses Splinter to navigate through web pages and APScheduler to run the program on a scheduled basis. To install, run:

`pip install requirements.txt`

### Set up settings.py
Create a file called settings.py and create Person objects of the people who are going to be reserving the room and an array of these objects called ROOM_RESERVERS

```python
from person import Person
john = Person('John', 'Doe', 'johndoe@northwestern.edu')

ROOM_RESERVERS = [john]
```
