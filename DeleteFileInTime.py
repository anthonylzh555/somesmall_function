import os, datetime

"""
This function can delete file.
And keep the file in the folder in a latest period of time.
parameters can be set: 
path
days
hours
minutes
seconds
"""

def delete_pic(path, days = 0,hours = 0, minutes = 0, seconds = 0):
    
    path_list=os.listdir(path)
    path_list.sort() 
    
    now = datetime.datetime.now()
    
    days = datetime.timedelta(days = days)
    hours = datetime.timedelta(hours = hours)
    minutes = datetime.timedelta(minutes = minutes)
    seconds = datetime.timedelta(seconds = seconds)
 
    delta_time_sum = days + hours + minutes + seconds
    
    if path_list != []:
        for img in path_list:
            obj_path = os.path.join(path,img)
            #print(obj_path)
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(obj_path))
            #print(ctime)
            if ctime < (now - delta_time_sum):
                os.remove(obj_path)
    
if __name__ == '__main__':
    
    path = "/home/asidemo/Env_test/testing/haha/"
    delete_pic(path, minutes = 20)