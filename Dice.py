import random
import easygui as g
import plotly
from datetime import datetime
from plotly.graph_objs import Bar,Histogram,Box,Layout
from plotly import offline


class Dice():
    def __init__(self,time,faces = 6,scores = [1,2,3,4,5,6],visualization = \
        True):
        self.faces = faces
        self.scores = scores
        self.time = time
        self.visualization = visualization
        self.dice_answers = []
        self.max_answer_index = []

    def made_image(self):
        x_values = self.dice_answers
        data = [Bar(x = x_values,y = self.dice_answers)]

        x_axis_config = {'title':'结果'}
        y_axis_config = {'title':'结果的频率'}
        my_layout = Layout(title = '投掷一个' + str(self.faces) + '面的骰子' + \
            str(self.time) + '次的结果',
                         xaxis = x_axis_config,yaxis = y_axis_config)
        date = datetime.today()
        today = str(date.year) + '-' + str(date.month) + '-' + str(date.day)\
         + ' ' + str(date.hour) + '-' + str(date.minute) + '-' \
         + str(date.second)
        offline.plot({'data': data,'layout': my_layout},filename = \
            'temp/play_dices' + ' ' + today + ' ' + f'{self.faces}面的骰子.html')

    def start(self):
    # try:
        if not len(self.scores) == self.faces:
            g.msgbox("输入有误，检查下数据吧！")
            return
        for answer_number in range(self.time):
            k = random.choice(self.scores)
            self.dice_answers.append(k)
        t = 0
        s = 0
        dice_answer_count = []
        for dice_answer in self.dice_answers:
            t += 1
            s += dice_answer
            print(f'第{t}次结果：{dice_answer}')
        print(f'总和：{s}')
        for _count in self.scores:
            c = self.dice_answers.count(_count)
            dice_answer_count.append(c)
        max_answer_index = dice_answer_count.index(max(dice_answer_count))
        dice_answer_count[dice_answer_count.index(max(dice_answer_count))] = 0
        # while str(dice_answer_count.index(max(dice_answer_count))) in str(max_answer_index):
        #     max_answer_index = dice_answer_count.index(max(dice_answer_count))
        #     dice_answer_count[dice_answer_count.index(max(dice_answer_count))] = 0
        # if len(str(max_answer_index)) >= 1:
        #     if len(str(max_answer_index)) == self.faces:
        #         print(f'骰子所有面出现的次数一样多')
        #     else:
        #         print(f'{max_answer_index}出现的次数最多')
        # else:
        #     print(f'{max_answer_index[0]}出现的次数最多')
        if self.visualization:
            self.made_image()
    # except Exception as e:
    #     

