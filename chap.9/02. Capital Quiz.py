# Chapter.9
# 02. Capital Quiz

def make_dictionary():
    dictionary = {}
    dictionary['Alabama'] = 'Montgomery'
    dictionary['Alaska'] = 'Juneau'
    dictionary['Arizona'] = 'Phoenix'
    dictionary['Arkansas'] = 'Little Rock'
    dictionary['California'] = 'Sacramento'
    dictionary['Colorado'] = 'Denver'
    dictionary['Connecticut'] = 'Hartford'
    dictionary['Delaware'] = 'Dover'
    dictionary['Florida'] = 'Tallahassee'
    dictionary['Georgia'] = 'Atlanta'
    dictionary['Hawaii'] = 'Honolulu'
    dictionary['Idaho'] = 'Boise'
    dictionary['Illinois'] = 'Springfield'
    dictionary['Indiana'] = 'Indianapolis'
    dictionary['Iowa'] = 'Des Moines'
    dictionary['Kansas'] = 'Topeka'
    dictionary['Kentucky'] = 'Frankfort'
    dictionary['Louisiana'] = 'Baton Rouge'
    dictionary['Maine'] = 'Augusta'
    dictionary['Maryland'] = 'Annapolis'
    dictionary['Massachusetts'] = 'Boston'
    dictionary['Michigan'] = 'Lansing'
    dictionary['Minnesota'] = 'Saint Paul'
    dictionary['Mississippi'] = 'Jackson'
    dictionary['Missouri'] = 'Jefferson City'
    dictionary['Montana'] = 'Helena'
    dictionary['Nebraska'] = 'Lincoln'
    dictionary['Nevada'] = 'Carson City'
    dictionary['New Hampshire'] = 'Concord'
    dictionary['New Jersey'] = 'Trenton'
    dictionary['New Mexico'] = 'Santa Fe'
    dictionary['New York'] = 'Albany'
    dictionary['North Carolina'] = 'Raleigh'
    dictionary['North Dakota'] = 'Bismarck'
    dictionary['Ohio'] = 'Columbus'
    dictionary['Oklahoma'] = 'Oklahoma City'
    dictionary['Oregon'] = 'Salem'
    dictionary['Pennsylvania'] = 'Harrisburg'
    dictionary['Rhode Island'] = 'Providence'
    dictionary['South Carolina'] = 'Columbia'
    dictionary['South Dakota'] = 'Pierre'
    dictionary['Tennessee'] = 'Nashville'
    dictionary['Texas'] = 'Austin'
    dictionary['Utah'] = 'Salt Lake City'
    dictionary['Vermont'] = 'Montpelier'
    dictionary['Virginia'] = 'Richmond'
    dictionary['Washington'] = 'Olympia'
    dictionary['West Virginia'] = 'Charleston'
    dictionary['Wisconsin'] = 'Madison'
    dictionary['Wyoming'] = 'Cheyenne'
    return dictionary
def question(dictionary): 
    count = 0
    for i in range(50):
        key, value = dictionary.popitem()
        print('Enter a capital for a displayed state :', key)
        capital = input('Enter a capital: ')
        if capital == value:
            count += 1
            print('Right!')
    print('The number of correct answer is', count)
    print('The nubmer of incorrect answer is', 50 - count)
def main():
    dictionary = make_dictionary()
    question(dictionary)
main()
