import webbrowser
from plyer import notification
import time
import datetime

def TimeSlot(hr, mn):
    t = hr*100 + mn
    if (t < 910 or t > 1620): return 0;
    else:
        if (t < 1010): return 1;
        elif (t < 1100 and t >= 1010): return 2;
        elif (t < 1200 and t >= 1110): return 3;
        elif (t < 1300 and t >= 1210): return 4;
        elif (t < 1440 and t >= 1350): return 5;
        elif (t < 1620 and t >= 1440): return 6;
        else: return 0;

d = { 
    'chill': 'https://youtube.com',
    'Maths': 'https://meet.google.com/lookup/dbez42233p',
    'OS': 'https://meet.google.com/lookup/ctz6mb45bk',
    'DAA': 'https://meet.google.com/lookup/bxvvorjed6',
    'CPS': 'https://meet.google.com/lookup/aueq5gsrfy',
    'CCTS': 'https://meet.google.com/lookup/edzhe63ohh',
    "APP Lab": 'https://meet.google.com/lookup/bsyv3yjbtk',
    'CC': 'https://meet.google.com/lookup/amftslckjg',
    'APP': 'https://meet.google.com/lookup/dgdvksdhmp',
    'SEPM': 'https://meet.google.com/lookup/bxrlz2rb4k',
    'EVS': 'https://meet.google.com/lookup/ck6gosg4n5',
    'SE': 'https://meet.google.com/lookup/afoasoacdt',
    "SEPM Lab": 'https://meet.google.com/lookup/e7blylmdez',
    "CC Lab": 'https://meet.google.com/lookup/fed5nybme7'
    }

def subTable(week, _timeSlot):
    t = _timeSlot
    if week == 6 or week == 7: week = 0
    l = [
        ['chill', 'chill', 'chill', 'chill','chill', 'chill', 'chill'],
        ['chill','Maths', 'OS', 'DAA', 'CPS','CCTS', "APP Lab"], # monday
        ['chill', 'CC', 'CPS', 'APP','Maths', 'SEPM', 'DAA'], # tuesday
        ['chill', 'Maths', 'OS', 'APP','EVS', 'DAA', 'OS'], # wednesday
        ['chill', 'SEPM', 'CC', 'APP','Maths', 'SE', "SEPM Lab"], # thursday
        ['chill', 'DAA', 'OS', 'SEPM','chill', 'Maths', "CC Lab"], # friday  
        ]
    return l[week][t]


if __name__ == "__main__":
    pre = -1
    while 1:
        # stores previous class timeSlot
        v = datetime.datetime.now()
        hr = int(v.strftime('%H')) # hour
        w = int(v.strftime('%w')) # week
        mn = int(v.strftime('%M')) # minute
        _timeSlot = TimeSlot(hr, mn) # storing value in a variable

        if _timeSlot != pre: # running it only if previous class was different from current one
            Class = subTable(w, _timeSlot)
            url = d[Class]
            webbrowser.open_new(url)

            pre = _timeSlot # to update the prev
            text = subTable(w, _timeSlot)

            notification.notify(
                            title = "Upcoming Class",
                            message = text, 
                            timeout = 4   # duration it will show notification
                           )
        time.sleep(60) # freq of every notification