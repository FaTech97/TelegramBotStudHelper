class Lesson:
    name = ""
    prep = ""
    begin = ""
    auditory = ""
    lessonType = ""

    def __init__(self, _name, _prep, _begin, _auditory, _lessonType):
        self.prep = _prep
        self.name = _name
        self.begin = _begin
        self.auditory = _auditory
        self.lessonType = _lessonType

    def print(self):
        print('* {0} ({1}) в {2} ауд. {3} / {4}'.format(self.name, self.prep,self.begin, self.auditory, self.lessonType))

    def getText(self):
        return  '* {0} ({1}) в {2} ауд. {3} / {4} \n'.format(self.name, self.prep, self.begin, self.auditory, self.lessonType)