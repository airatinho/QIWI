
import time
from random import randint

dance_music=['electrohouse','rnb','pop-music']
class Person:
    """Типаж людей"""

    __genders=['мальчик','девочка']
    def __init__(self,gender:str = None,dance_style:str=None,state:str=None):
        self.__gender=gender or self.__genders[randint(0,len(self.__genders)-1)]
        self.__dance_style=dance_style or dance_music[randint(0,len(dance_music)-1)]
        self.__state=state
    def get_gender(self):
        return self.__gender
    def get_dance_style(self):
        return self.__dance_style
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,state):
        if isinstance(state,str):
            self.__state=state
        else:
            raise ValueError('Неверный тип состояния')
    @property
    def get_all(self):
        return self.__gender,self.__dance_style,self.__state
class NightClub:
    """Ночной клуб"""
    __dance_music=['electrohouse','rnb','pop-music']
    __states=['танцует','пьет водку в баре']
    __visitors={} #посетители
    __current_music=None
    def __init__(self,capacity:int=None,music:list=None,duration:int=4):
        self.__capacity = capacity or randint(3,10) #вместительность клуба
        self.__music = music or self.__dance_music  #набор музыки в клубе
        self.__duration=duration                    #длительность работы клуба

    @property
    def custom_visitors(self):
        return self.__visitors

    @custom_visitors.setter
    def custom_visitors(self, value:dict):
        if isinstance(value,dict):
            if len(value)>self.__capacity:
                raise ValueError('Столько человек в клуб не вместится!')
            for n in self.__visitors.keys():
                if not isinstance(value[n],Person):
                    raise ValueError('Неверный тип данных посетителей')
            self.__visitors=value
        else:
            raise ValueError('Неверный тип данных посетителей')

    def __call__(self, num_come=None):
        """запуск этого метода означает заполнение клуба людьми
        и началом проигрывания музыки"""
        num_come=num_come or randint(0,self.__capacity) #сколько пришло людей
        if len(self.__visitors)==0:
            for i in range(num_come):
                self.__visitors[f'Посетитель_{i+1}']=Person()
            print(len(self.__visitors))
        else:
            print(f'Количество посетителей {len(self.__visitors)}')
        for d in range(self.__duration):
            self.__current_music= self.__music[randint(0,len(self.__music)-1)]
            print(f"В клубе играет музыка {self.__current_music}")
            time.sleep(2)
            for k in self.__visitors.keys():
                if self.__visitors[k].get_dance_style()==self.__current_music:
                    self.__visitors[k].state=self.__states[0]
                else:
                    self.__visitors[k].state=self.__states[1]
                print(f'{k}, Пол:{self.__visitors[k].get_gender()},'
                      f' любит {self.__visitors[k].get_dance_style()}, '
                      f'Сейчас {self.__visitors[k].state} ')

if __name__ == '__main__':
    morozko=NightClub()

    #можно закоментить следующие три строчки
    morozko.custom_visitors={'вася':Person(gender='мальчик'),
                             'Роза':Person(gender='девочка'),
                             'Саша':Person(gender='не определился')}

    morozko()