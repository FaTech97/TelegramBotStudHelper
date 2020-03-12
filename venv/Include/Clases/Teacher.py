import json

class Teacher:

    def getTeacherFullName(lastname):
        with open('teachers.json', 'r', encoding='utf-8') as rasp:
            gh = json.load(rasp)[lastname]
            print(gh)


