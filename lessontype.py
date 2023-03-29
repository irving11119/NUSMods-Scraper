import requests
import json

def get_lesson_types(filepath):
    """Gets available lesson types for scraped data

    Args:
        filepath (string): Filepath of the file containing scraped NUSMods Data
    """
    f = open('nusModsData.json')

    data = json.load(f)

    lesson_types = set()

    for module in data:
        for info in module["timetable"]:
            lesson_types.add(info["lessonType"])

if __name__=='__main__':
    filepath = 'nusModsData.json'
    lesson_types = get_lesson_types(filepath)
    print(lesson_types)
        