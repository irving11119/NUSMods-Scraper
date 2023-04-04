import math
import requests
import json
import datetime

def scrape():
    """
    Retrieves Module Data for all Modules available in AY22/23 Semester 2
    """
    modulepath = "https://api.nusmods.com/v2/2022-2023/moduleList.json"

    result = requests.get(modulepath).json()
    module_list = []
    for module in result:
        
        mc = module["moduleCode"]
        title = module["title"]
        
        moduleinfopath = "https://api.nusmods.com/v2/2022-2023/modules/{}.json".format(mc)
        
        module_data = requests.get(moduleinfopath).json()
        semData = module_data["semesterData"]
        mc1 = module_data["moduleCredit"]
        print("scraping...")
        for i in range(0, len(semData)):
            if semData[i]["semester"] == 2:
                obj = {"moduleCode": mc, "title": title, "moduleCredit": mc1, "timetable": semData[i]["timetable"]}
                module_list.append(obj)
        
        
    with open('nusModsData.json', 'w') as fp:
        json.dump(module_list, fp)
    
def format():    
    """
    Formats the data for use in Java-based team project
    """    
    f = open('nusModsData.json')

    data = json.load(f)

    print("formatting...")
    objList = []
    for obj in data:
        code = obj["moduleCode"]
        title = obj["title"]
        mc = obj["moduleCredit"]
        
        timetable = obj["timetable"]
        datalist = []
        for data in timetable:
            classnumber = data["classNo"]
            startTime = data["startTime"]
            endTime = data["endTime"]
            day = data["day"]
            lessonType = data["lessonType"]
            weeks = data["weeks"]
            
            if not isinstance(weeks, list):
                
                if "weeks" in weeks:
                    weeks = weeks["weeks"]
                    
                elif "weekInterval" in weeks:
                    weeks = getWeeks(weeks["start"], weeks["end"], weeks["weekInterval"])
            
            
            newTt = {"classnumber": classnumber, "startTime": startTime, "endTime": endTime, "day": day, "lessonType": lessonType}
            datalist.append(newTt)
           
        newObj = {"code": code, "title": title, "moduleCredits": mc, "timetable": datalist}
        objList.append(newObj)
    
    with open('data.json', 'w') as fp:
        json.dump(objList, fp)
        
    print("Done!")
    
    
def getWeeks(start_date, end_date, week_interval):
    start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    
    week_interval_int = int(week_interval)
    
    week_list = []
    
    start_week = getWeek(start_date_obj)
    end_week = getWeek(end_date_obj)
    
    for i in range(start_week, end_week, week_interval_int):
        week_list.append(i)
    
    

def getWeek(date):
    start_sem_date = datetime.date(2023, 1, 9)
    delta = date - start_sem_date
    
    week = int(math.ceil(delta / 7))
    
    return week
        
        
        
        
if __name__=='__main__':
    #scrape()
    format()
    