import requests
import json

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
        for i in range(0, len(semData)):
            if semData[i]["semester"] == 2:
                obj = {"moduleCode": mc, "title": title, "moduleCredit": mc1, "timetable": semData[i]["timetable"]}
                module_list.append(obj)
                print(obj)
        
    with open('nusModsData.json', 'w') as fp:
        json.dump(module_list, fp)
    
def format():    
    """
    Formats the data for use in Java-based team project
    """    
    f = open('nusModsData.json')

    data = json.load(f)

    print(data)
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
            
            
            newTt = {"classnumber": classnumber, "startTime": startTime, "endTime": endTime, "day": day, "lessonType": lessonType}
            datalist.append(newTt)
            
        newObj = {"code": code, "title": title, "moduleCredits": mc, "timetable": datalist}
        objList.append(newObj)
    
    with open('data.json', 'w') as fp:
        json.dump(objList, fp)
        
        
if __name__=='__main__':
    scrape()
    format()
    