"""Чать первая: в приведённом фрагменте кода программа принимает ввод пользователя
и сопоставляет первое слово с командой в verb_dict. В случае совпадения вызывается соответствующая функция"""
#метод split разделяет ввод на отдельные слова
def say(noun):
    return 'You said "{}"'.format(noun)



#=====Часть вторая=====
#Goblin наследует от GameObject потому, что он является своего рода GameObject
class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc

#=====Часть вторая и третья=====
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self.desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off."
        elif health <= 0:
            health_line = "It is dead."
        return self.desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value

#Зачем инструкция desc была была превращена в свойство? Так её можно динамически создавать при доступе.

    def hut(noun):
        if noun in GameObject.objects:
            thing = GameObject.objects[noun]
            if type(thing) == Goblin:
                thing.health = thing.health - 1
                if thing.health == 0:
                    msg = "You killed the goblin!"
                else:
                    msg = "You hit the {}".format(thing.class_name)
        else:
            msg = "There is no {} here.".format(thing.class_name)
        return msg


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here".format(noun)

verb_dict = {"say": say, "examine": examine}

goblin = Goblin("Gobbly")



class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc