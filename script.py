import pandas as pd
import numpy as np
import datetime
import json
import jsonpickle

class Object:
    def toJSON(self):

        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

def GanttConfig(data):
    time_list=[]
    finish_list=[]
    id_list =[]
    label_list = []
    card_list = []
    cards = []
    unique_list=[]

    for items in data.values:
        if items[4] is not None:
            time_list.append(datetime.datetime.strptime(items[4].replace('jan','01').replace('mar','03').replace('apr','04').replace('may','05').replace('jun','06')
            .replace('jul','07').replace('aug','08').replace('nov','11').replace('-20','-2020').replace('-19','-2019').replace('-13','-2013').replace('-16','-2016'), '%d-%m-%Y %H:%M').timestamp())
        else:
            time_list.append(0)
    for num, items in enumerate(data.values, start = 0):
        finish_list.append(time_list[num]+(items[5]*6000))
    i = 1
    while i<=len(data.values):
        id_list.append(str(i))
        i = i +1
    j = 0
    for items in data.values:
        label_list.append(items[2])
    k = 0
    for items in data.values:
        card_list.append(items[0].replace('0201','0').replace('0202','1').replace('0203','2').replace('0204','3').replace('0205','4').replace('0206','5').
        replace('0208','6').replace('0209','7').replace('0211','8').replace('0212','9').replace('0215','11').replace('0214','10'))
    for items in data.values:
        cards.append(items[0])

    dataset = np.array(cards)
    cards = np.unique(dataset).tolist()
    for num,items in enumerate(cards):
        unique_list.append(str(num))

    datafile = np.array(card_list)
    datafile = np.unique(datafile).tolist()
    ge = []
    for item in datafile:
        ge.append(int(item))

    ge.sort()
   
    config = Object()
    config.chart = Object()
    config.chart.items=Object()
    config.chart.items.time=Object()
    config.height = 600
    config.list = Object()
    config.list.columns = Object()
    config.list.columns.data = Object()
    config.list.columns.data.id = Object()
    config.list.columns.data.id.data = "id"
    config.list.columns.data.id.header = Object()
    config.list.columns.data.id.header.content = "ID"
    config.list.columns.data.id.id = "id"
    config.list.columns.data.id.width = 40
    config.list.columns.data.label = Object()
    config.list.columns.data.label.data = "label"
    config.list.columns.data.label.header = Object()
    config.list.columns.data.label.header.content = "Carding Machine"
    config.list.columns.data.label.id = "label"
    config.list.columns.data.label.width = 200
    
    #Creation of items object
    config.chart.items = [Object() for i in range(len(card_list))]

    j = 0
    while j < len(card_list):
        config.chart.items[j].id=str(j)
        config.chart.items[j].label=str(label_list[j])
        config.chart.items[j].rowId=str(card_list[j])
        config.chart.items[j].time = Object()
        config.chart.items[j].time.end=finish_list[j]
        config.chart.items[j].time.start=time_list[j]
        j = j + 1
    
    # Creation of rows ID and Label
    config.list.rows = [Object() for i in range(len(unique_list))]
    n = 0
    while n < len(unique_list):  
        config.list.rows[n].id = str(unique_list[n])
        config.list.rows[n].label = cards[n]
        n = n + 1
    return config

def serialize(data):
    
    return 


