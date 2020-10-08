import numpy as np
import pandas as pd
import json
import jsonpickle
import datetime

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Thing(object):
    def __init__(self, name):
        self.list = name

def serialise_blend(engine):
    def sql_command(engine):
        data = pd.read_sql("SELECT CARD_NO,ORDER_NO,ORD_TYPE,CUST_NO,DESCR,WORKS_ORDER,DATE_CARD,STD_HRS,QTY_REQ FROM WOOL.V_BLENDHDR WHERE TRUNC(DNT_SCH_S) between (SYSDATE-4) AND (SYSDATE+15)", engine)
        return data

    config = Object()
    config = sql_command(engine).to_dict('records')
    vals = ["FKL     ","FKL","FKL ","FKL  ","FKL   ","FKL    "]
    for num, items in enumerate(config):
        config[num].update(blendhdr_id = num+1)
        config[num]['works_order'] = config[num]['works_order'][5:].strip()
        config[num]['date_card'] = config[num]['date_card'].replace('jan','01').replace('mar','03').replace('apr','04').replace('may','05').replace('jun','06').replace('jul','07').replace('aug','08').replace('sep','9').replace('oct','10').replace('nov','11').replace('dec','12').replace('-20','-2020').replace('-19','-2019').replace('-13','-2013').replace('-16','-2016')
        config[num]['card_no'] = config[num]['card_no'].replace('0201','201').replace('0202','202').replace('0203','203').replace('0204','204').replace('0205','205').replace('0206','206').replace('0208','208').replace('0209','209').replace('0210','210').replace('0211','211').replace('0212','212').replace('0214','214').replace('0215','215')
        if(config[num]['cust_no']  in vals and config[num]['ord_type'] == 'PO'):
            config[num]['cust_no'] = config[num]['cust_no'].replace(config[num]['cust_no'],'pink')
        config[num].update(start=datetime.datetime.strptime(config[num]['date_card'], '%d-%m-%Y %H:%M').timestamp())
    
    return config

def serialise_dye(engine):

    def sql_command(engine):
        data = pd.read_sql("SELECT batch_no,mach_no,sh_code,sh_desc,date_start,std_hrs,qty_dye FROM dye.v_dye_scheduling WHERE TRUNC(date_start) between (SYSDATE-4) AND (SYSDATE+15)",engine)
        return data
    
    batch = Object()
    batch = sql_command(engine).to_dict('records')
    for num,items in enumerate(batch):
        batch[num].update(dye_id = num+1)
        batch[num]['date_start'] = (batch[num]['date_start'] - datetime.datetime(1970,1,1)).total_seconds()

    return batch