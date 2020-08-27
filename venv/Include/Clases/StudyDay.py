from Include.Clases.Lesson import Lesson
from datetime import datetime


class StudyDay:
    lessons = []

    def showAllLessons(self):
        strr = ''
        for lesson in self.lessons:
            strr = strr + lesson.getText()
        return strr

    def setLessons(self, _lessons):
        self.lessons = _lessons

    def timeBeforeNextLeson(self):
        minTime = 86400
        lessonNumber = 0
        intLesson = 0
        paraMessage = 'Пар нет, отдыхайте'
        for lesson in self.lessons:
            now = datetime.now()
            timeToLesson = datetime(now.year, now.month, now.day, int(lesson.begin.split(':')[0]),
                                    int(lesson.begin.split(':')[1]))
            dist = timeToLesson.timestamp() - now.timestamp();
            if (timeToLesson.timestamp() > now.timestamp()):
                if ((minTime > dist) & (dist > 0)):
                    minTime = dist
                    intLesson = lessonNumber
            lessonNumber += 1
        if (minTime < 86400):
            paraMessage = ('Пара "' + self.lessons[intLesson].name + '" через ' + str(int(minTime / 3600)) + ' ч. ' + str(
                int((minTime % 3600) / 60)) + ' мин. в ауд ' + self.lessons[intLesson].auditory)
        return paraMessage
