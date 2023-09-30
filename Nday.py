import requests
from bs4 import BeautifulSoup
import csv
import os
import sys

Version = "3.0"
print("This is Version: " + Version)

user_agent = input("Enter your desired user-agent: ")
headers = {
    "User-Agent": user_agent + "Using 9003's Nday Spec Checker Discord: @9003"
}

filename = "puppet.csv"

if os.path.exists("specs.txt"):
    os.remove("specs.txt")
if os.path.exists("econ.txt"):
    os.remove("econ.txt")
if os.path.exists("nukes.txt"):
    os.remove("nukes.txt")
if os.path.exists("shields.txt"):
    os.remove("shields.txt")
if os.path.exists("intel.txt"):
    os.remove("shields.txt")


with open("specs.txt", "a+") as sp:
    with open("econ.txt", "a+") as e:
        with open("nukes.txt", "a+") as n:
            with open("shields.txt", "a+") as sh:
                with open("shields.txt", "a+") as int:
                    with open(filename) as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            # row.replace(" ", "_")
                            r = requests.get(
                                "https://www.nationstates.net/page=nukes/nation=" + row[0],
                                headers=headers,
                            )
                            # r = requests.get('https://www.nationstates.net/page=nukes/nation='+"9003")
                            soup = BeautifulSoup(r.content, "html.parser")
                            job_elems = soup.find("span", class_="fancylike")
                            for job_elem in job_elems:
                                var = input(row[0] + " is " + job_elem + "...")
                                sp.writelines(row[0] + " is " + job_elem + "\n")
                                # print(job_elem)
                                if "Military" in job_elem:
                                    n.writelines(row[0] + "\n")
                                    # Strategic
                            if "Strategic" in job_elem:
                                sh.writelines(row[0] + "\n")
                            if "Eco" in job_elem:
                                sh.writelines(row[0] + "\n")
                            if "Int" in job_elem:
                                int.writelines(row[0] + "\n)
