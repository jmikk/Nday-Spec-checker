import requests
from bs4 import BeautifulSoup
import csv
import os
import sys
import time

Version = "4.0"
print("This is Version: " + Version)

user_agent = input("Enter your desired user-agent: ")


filename = "puppet.csv"

if os.path.exists("specs.txt"):
    os.remove("specs.txt")
if os.path.exists("econ.txt"):
    os.remove("econ.txt")
if os.path.exists("nukes.txt"):
    os.remove("nukes.txt")
if os.path.exists("shields.txt"):
    os.remove("shields.txt")


with open("specs.txt", "a+") as sp:
    with open("econ.txt", "a+") as e:
        with open("nukes.txt", "a+") as n:
            with open("shields.txt", "a+") as sh:
                with open("int.txt", "a+") as intel:
                    with open(filename) as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            # row.replace(" ", "_")
                            headers = {
                                "User-Agent": user_agent
                                + "Used by 9003"
                                + str(time.time),
                            }
                            r = requests.get(
                                "https://www.nationstates.net/page=nukes/nation="
                                + row[0],
                                headers=headers,
                            )
                            # r = requests.get('https://www.nationstates.net/page=nukes/nation='+"9003")
                            soup = BeautifulSoup(r.content, "html.parser")
                            elements = soup.find_all(
                                "span", class_="smalltext", style="color:red"
                            )

                            # Check if any of the found elements contain the text 'DESTROYED'
                            for element in elements:
                                if "DESTROYED" in element.text:
                                    continue

                            job_elems = soup.find("span", class_="fancylike")
                            for job_elem in job_elems:
                                # input
                                input(row[0] + " is " + job_elem + "...")
                                sp.writelines(row[0] + " is " + job_elem + "\n")
                                # print(job_elem)
                                if "Military" in job_elem:
                                    n.writelines(row[0] + "\n")
                                    # Strategic
                                if "Strategic" in job_elem:
                                    sh.writelines(row[0] + "\n")
                                if "Eco" in job_elem:
                                    e.writelines(row[0] + "\n")
                                if "Intel" in job_elem:
                                    n.writelines(row[0] + "\n")
