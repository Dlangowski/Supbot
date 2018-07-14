import requests
from bs4 import BeautifulSoup as bs
import os
import sys
import git
from distutils.dir_util import copy_tree
import shutil
from pathlib import Path


def getCurrentDirct():
    global inf_path
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    info_path = os.path.join(application_path)

    return info_path

def versionComparison():
    data = requests.get("https://github.com/Dlangowski/Supbot/blob/master/fileReader.app/Contents/MacOS/info") #NEED TO CHANGE TO ACTUAL GITHUB WHEN DONE
    text = data.text
    soup = bs(text, "lxml")
    NewestVersion = soup.find('td', {'id':'LC1'}).text.split(" ")[1]
    info_path = getCurrentDirct()
    currentVersionFile = open(info_path +"/info", 'r')
    currentVersion = currentVersionFile.readline().split(" ")[1]

    if currentVersion < NewestVersion:
        update(NewestVersion, info_path)
    else:
        print("you're up to date!")

def update(info_path):
    p = Path(info_path).parents[1]
    if os.path.exists(p):
        shutil.rmtree(p)
    os.makedirs(p)
    git.Git(p).clone("https://github.com/Dlangowski/Supbot.git")


versionComparison()
