from cgitb import text
from io import open_code
from logging import captureWarnings
from re import T
import requests
from bs4 import BeautifulSoup
from colorama import Fore, init
import metadata_parser
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

init()

doc = input("Enter the .txt file which has the major, minor and specialisation links: ")

with open(doc, 'r') as file:
    for i in file:
        url = i.rstrip('\r\n')
        urlk = f'{url}'

        page = metadata_parser.MetadataParser(url)

        url = requests.get(url)

        if url.status_code != 200:
            printing = Fore.RED + f'{urlk}'
            print(printing)

        elif "the site encountered an error" in url.text:
            printing = Fore.LIGHTRED_EX + f'{urlk}'
            print(printing)

        else:
            capture = ""

            a = page.metadata

            majorname = ''
            majoracronym = ''
            majoryear = ''
            majorcode = ''

            if a is not None:

                if page.get_metadatas('major-name') is not None:
                    majorname = page.get_metadatas('major-name')[0]
                if page.get_metadatas('major-acronym') is not None:
                    majoracronym = page.get_metadatas('major-acronym')[0]
                if page.get_metadatas('major-year') is not None:
                    majoryear = page.get_metadatas('major-year')[0]
                if page.get_metadatas('major-code') is not None:
                    majorcode = page.get_metadatas('major-code')[0]

                soup2 = BeautifulSoup(url.content, "html.parser")

                for i in soup2.find_all(class_="tab-content", recursive=True):
                    j = i.find('div',class_='body__inner w-doublewide copy')
                b = str(j)

                if ('table-detail-units' in b):
                    list = []
                    table = soup2.find_all('table')
                    for i in table:
                        for row in i.tbody.find_all('tr'):
                            columns = row.find_all('td')
                        if columns != []:
                            code = columns[0].text.strip()
                            code = code + ' '
                            title = columns[1].text.strip()
                            title = title + ' '
                            units = columns[2].text.strip()
                            units = units + ' '
                            a = code + title + units
                            list.append(a)
                            j = ", ".join(list)
                else:
                    if not isinstance(j, str):
                        j = j.text
                        j = j.replace('\n',' ')

            if ('table-detail-units' in b):
                capture = urlk + ' | ' + 'Major Acronym: ' + majoracronym + ' | ' + 'Major Code: ' + majorcode + ' | ' + 'Major Year: ' + majoryear + ' | ' + 'Major Name: ' + majorname + ' | Requirements: ' + j
                with open('valid.txt', 'a') as f:
                    f.write(capture + '\n')
                f.close()

            else:
                capture = urlk + ' | ' + 'Major Acronym: ' + majoracronym + ' | ' + 'Major Code: ' + majorcode + ' | ' + 'Major Year: ' + majoryear + ' | ' + 'Major Name: ' + majorname + ' | ' + 'Requirements: ' + j
                with open('valid.txt', 'a') as f:
                    f.write(capture + '\n')
                f.close()

            valid = Fore.GREEN + f'{urlk}'
            print(valid)

