from datetime import datetime
from os import getcwd


where_am_i = getcwd()
odds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,24,25]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("this is minute seems a little odd.")
else:
    print("not date");
