'''
**** Purpose ****
- Reserve meeting room 5746 (5S) in Main library
    - Chosen because it is the only meeting room in main thats open 6-10

**** Problems ****
- not very user-friendly to reserve other rooms
- isn't self automated
- doesn't iterate over dates
'''

from splinter import Browser
import atexit, datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

class Person:
    def __init__(self, f, l, e):
        self.fname = f
        self.lname = l
        self.email = e

# People whose emails are reserving the room
ethan = Person('Ethan', 'Lee', 'ethanlee2020@u.northwestern.edu')
mike = Person('Michael', 'Considine', 'michaelconsidine2020@u.northwestern.edu')
miles = Person('Miles', 'Cameron', 'milescameron2020@u.northwestern.edu')

# Fourth person doesn't need to reserve all 3 hours worth so is separate
connor = Person('Connor', 'Loughlin', 'connorloughlin2020@u.northwestern.edu')

People = [mike, ethan, miles]

def enter_date(date):
    # date is a string in format 'yyyy-mm-dd'
    browser.select('d', date)
    browser.find_by_text('Change Date')[1].click()

def enter_information(fname, lname, email, title, ppl):
    # This function enters information in the field to submit
    browser.fill('fname', fname)
    browser.fill('lname', lname)
    browser.fill('email', email)
    browser.fill('nick', title)
    browser.fill('q1', ppl)
    browser.select('q2', 'Undergraduate')

def submitting_times(person):
    # Checks off the last times on the form
    element_array = browser.find_by_name('sid[]')
    length = len(element_array)

    for num in range(length - 6,length):
        element_array[num].click()

    enter_information(person.fname, person.lname, person.email, 'study', '7')

def submitting_times_last_person(person):
    # Checks off the last 2 times on the form
    element_array = browser.find_by_name('sid[]')
    length = len(element_array)

    for num in range(length - 2,length):
        element_array[num].click()

    enter_information(person.fname, person.lname, person.email, 'study', '7')

def run(date):
    for ppl in People:
        browser.visit('http://northwestern.libcal.com/rooms_acc.php?gid=12753')

        enter_date(date)
        submitting_times(ppl)
        browser.find_by_id('s-lc-rm-ac-but').click()

    browser.visit('http://northwestern.libcal.com/rooms_acc.php?gid=12753')
    enter_date(date)
    submitting_times_last_person(connor)
    browser.find_by_id('s-lc-rm-ac-but').click()

browser = Browser('chrome')

def run_date():
    today = datetime.date.today()
    days_in_advance = datetime.timedelta(days=20)
    date_to_reserve = str(today + days_in_advance)
    run(date_to_reserve)

# scheduler = BackgroundScheduler()
# # Run program once a day
# while True:
#     scheduler.start()
#     scheduler.add_job(run_date, trigger=IntervalTrigger(seconds=3), id='reserving_room', name='reserving a room', replace_existing=True)
#     atexit.register(lambda: scheduler.shutdown())

# sched = BlockingScheduler()
# sched.add_job(run_date, 'interval', hours=24)
# sched.start()
