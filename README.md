# NUSMods-Scraper

NUSMods scraper using Python 3 and the NUSMods API.

## Description

This project was created for the purpose of NUS's Software Engineer and Object Oriented Programming (CS2113) Class. The following files contains the scripts necessary to scrape NUS Module data to supplement the team project for the class. The NUSMods API does not have an endpoint to scrape all modules and data within a single semester. Hence, this script manually scrapes the data and formats it to return all modules and its relevant information for AY22/23

## Getting Started

### Dependencies

Ensure your Operating System has the lastest version of Python 3 installed. This script has been run on both MacOS and Linux based operating systems. While it has not been tested on Windows, it should still be able to run as long as Python 3 is installed.

### Installing

Clone the repository using the following command

```bash
git clone https://github.com/irving11119/NUSMods-Scraper.git
```

### Running the Program

To run the script, move over the directory containing the relevant python files.

```bash
cd NUSMods-Scraper
```

To obtain NUSMods data, run the following command:

```bash
python3 scraper.py
```

This creates 2 files, `nusModsData.json`, which is the raw NUSMods data scraped from the NUSMods API, and `data.json` which is the formatted data used for CS2113 TP.

To obtain all lesson types across all modules, run the following command:

```bash
python3 lessontype.py
```

This prints to the console all the possible lesson types available across all modules in AY22/23 which was then used in the project.

## Acknowledgements
