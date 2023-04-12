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
    print("scraping...")
    for module in result:
        
        mc = module["moduleCode"]
        title = module["title"]
        
        moduleinfopath = "https://api.nusmods.com/v2/2022-2023/modules/{}.json".format(mc)
        
        module_data = requests.get(moduleinfopath).json()
        semData = module_data["semesterData"]
        mc1 = module_data["moduleCredit"]
        
        for i in range(0, len(semData)):
            if semData[i]["semester"] == 1 or  semData[i]["semester"] == 2:
                obj = {"moduleCode": mc, "title": title, "moduleCredit": mc1, "semester": semData[i]["semester"], "timetable": semData[i]["timetable"]}
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
        sem = obj["semester"]
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
                    if weeks["weekInterval"] == 0:
                        continue
                    weeks = getWeeks(sem, weeks["start"], weeks["end"], weeks["weekInterval"])
                    
                else:
                    weeks = getWeeks(sem, weeks["start"], weeks["end"], 1)
            
            if weeks == []:
                continue
            
            newTt = {"classNumber": classnumber, "startTime": startTime, "endTime": endTime, "day": day, "lessonType": lessonType, "weeks": weeks}
            datalist.append(newTt)
           
        newObj = {"code": code, "title": title, "moduleCredits": mc, "semester": sem, "timetable": datalist}
        objList.append(newObj)
    
    with open('data.json', 'w') as fp:
        json.dump(objList, fp)
        
    print("Done!")
    
    
def getWeeks(sem, start_date, end_date, week_interval):
    start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    
    week_interval_int = int(week_interval)
    
    week_list = []
    
    start_week = getWeek(start_date_obj,sem)
    end_week = getWeek(end_date_obj, sem)
    
    for i in range(start_week, min(end_week, 13), week_interval_int):
        week_list.append(i)
        
    return week_list
    
    

def getWeek(date, sem):
    if sem == 2:
         start_sem_date = datetime.date(2023, 1, 9)
         
    if sem == 1:
        start_sem_date = datetime.date(2022, 8,8)
              
    delta = date - start_sem_date
    week = calculateWeekNumber(delta)
    
    return week

def calculateWeekNumber(delta):
    return int(delta.days / 7) + 1
            
if __name__=='__main__':
    #scrape()
    format()
    