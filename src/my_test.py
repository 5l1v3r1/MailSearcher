import json
import os
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


email_miss_counter = 0


class Person:

    def __init__(self, person_dict):
        global email_miss_counter
        self.name = person_dict['name']
        if 'email' not in person_dict['contact']:
            self.email = ''
            email_miss_counter += 1
            # pass
        else:
            email_addr = str(person_dict['contact']['email']).lower().replace(' at ', '@').replace(' dot ', '.').replace(' ', '').replace('\n', '')
            self.email = email_addr + '  [' + person_dict['contact']['email'] + ']'


class MyTest:

    def __init__(self):
        print os.path.abspath('.')
        self.people = []

    def get_test_people_list(self):
        file_name = '../citation_top_1000.json'
        json_content = open(file_name).read()
        people_list = json.loads(json_content)
        for person_dict in people_list:
            person = Person(person_dict)
            if person.email:
                self.people.append(Person(person_dict))

    def display(self):
        for person in self.people:
            print person.email


if __name__ == '__main__':
    testCase = MyTest()
    testCase.get_test_people_list()
    print email_miss_counter
    testCase.display()