import json
import datetime
from Include.Clases.StudyDay import StudyDay
from Include.Clases.Lesson import Lesson


class Schedule:
    days = []
    beginDate = datetime.date(2020, 2, 3)

    def setDays(self, days):
        self.days = days

    def setBeginDate(self, begDate):
        a = begDate.split('-')
        beginDate = datetime.date(int(a[0]), int(a[1]), int(a[2]))

    def getAllRaps(self):
        headers=["\n1 неделя\nПонедельник:\n","\nВторник:\n","\nСреда:\n","\nЧетверг:\n","\nПятница:\n","","",
                 "\n2 неделя\nПонедельник:\n","\nВторник:\n","\nСреда:\n","\nЧетверг:\n","\nПятница:\n","",""]
        ini = 0
        pars = ''
        for day in self.days:
            row = ''
            row += day.showAllLessons();
            if(row.__len__() > 0 ):
                pars += headers[ini];
                pars += row;
            ini = ini + 1
        return  pars;

    # Один если первая неделя нечетнаяя
    def searchDay(self):
        daysCount = datetime.date.today() - self.beginDate
        studyDayNow = self.days[daysCount.days % 14]
        if (studyDayNow is not None):
            return studyDayNow

    def getDataFromJSON(self):
        with open('rasp.json', 'r', encoding='utf-8') as rasp:
            rasp = json.load(rasp)['schedule']
            sched = Schedule
            studyDays = []
            for _studyDay in rasp:
                lessons = []
                for lesson in _studyDay['StudyDay']:
                    lessons.append(Lesson(lesson['name'], lesson['prep'], lesson['begin'], lesson['auditory'],
                                          lesson['lessonType']))
                sd = StudyDay()
                sd.setLessons(lessons)
                studyDays.append(sd)
            self.days = studyDays
