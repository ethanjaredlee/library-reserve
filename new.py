from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from settings import ROOM_RESERVERS

mudd = 'http://northwestern.libcal.com/rooms_acc.php?gid=15697'
main = 'http://northwestern.libcal.com/rooms_acc.php?gid=12753'

libraries = [mudd, main]

content = [requests.get(library).content for library in  libraries]

def run_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    h2 = soup.find_all('h2')
    relevant = [h for h in h2 if '2174' in h.text]
    if len(relevant) != 1:
        print 'something went wrong'
        return
    relevant = relevant[0]
    boxes = relevant.parent.parent.find_all('div')[1:]
    boxIDs = [box.input['id'] for box in boxes]
    return boxIDs

def run_on_dates(dates, library):
    '''
    takes a list of dates and returns a list of urls to navigate to
    date should be formatted as YYYY-MM-DD
    '''
    extendedURLs = []
    for date in dates:
        url = library + '&d={}&cap=0'.format(date)
        extendedURLs.append(url)
    return extendedURLs

if __name__ == "__main__":
    driver = webdriver.Chrome()
    dates = run_on_dates(['2017-10-05'], mudd)
    for date in dates:
        driver.get(date)
        boxIDs = run_soup(requests.get(date).text)
        count = 0
        for box in boxIDs:
            print box
            count += 1
            if count == 6:
                break
            checkbox = driver.find_element_by_id(box)
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)
            checkbox.click()




# def submit_form(person):
#     browser.fill('fname', person.fname)
#     browser.fill('lname', person.lname)
#     browser.fill('email', person.email)
#     browser.select('q1', 'Undergraduate student')
#     browser.find_by_id('s-lc-rm-ac-but').click()

# if __name__ == "__main__":
#     browser = Browser('chrome')
#     browser.visit(mudd)
#     muddIDs = run_soup(content[0])
#     # if content size != to 48, then alert me

#     for person in ROOM_RESERVERS:
#         counter = 0
#         while len(muddIDs) != 0:
#             checkbox = muddIDs.pop(0)
#             browser.find_by_css('#' + checkbox).click()
#             counter += 1
#             if counter == 6:
#                 break
#         submit_form(person)



# def enter_date(date):
#     # date is a string in format 'yyyy-mm-dd'
#     browser.select('d', date)
#     browser.find_by_text('Change Date')[1].click()

# def enter_information(fname, lname, email, title, ppl):
#     # This function enters information in the field to submit
#     browser.fill('fname', fname)
#     browser.fill('lname', lname)
#     browser.fill('email', email)
#     browser.fill('nick', title)
#     browser.fill('q1', ppl)
#     browser.select('q2', 'Undergraduate')

# def submitting_times(person):
#     # Checks off the last times on the form
#     ipdb.set_trace()
#     element_array = browser.find_by_name('sid[]')
#     length = len(element_array)

#     for num in range(length - 6,length):
#         element_array[num].click()

#     enter_information(person.fname, person.lname, person.email, 'study', '7')

# def submitting_times_last_person(person):
#     # Checks off the last 2 times on the form
#     element_array = browser.find_by_name('sid[]')
#     length = len(element_array)

#     for num in range(length - 2,length):
#         element_array[num].click()

#     enter_information(person.fname, person.lname, person.email, 'study', '7')

# def run(date):
#     for ppl in ROOM_RESERVERS:
#         browser.visit('http://northwestern.libcal.com/rooms_acc.php?gid=12753')

#         enter_date(date)
#         submitting_times(ppl)
#         browser.find_by_id('s-lc-rm-ac-but').click()

#     # browser.visit('http://northwestern.libcal.com/rooms_acc.php?gid=12753')
#     # enter_date(date)
#     # submitting_times_last_person(connor)
#     # browser.find_by_id('s-lc-rm-ac-but').click()

# def run_date():
#     today = datetime.date.today()
#     days_in_advance = datetime.timedelta(days=20)
#     date_to_reserve = str(today + days_in_advance)
#     run(date_to_reserve)
