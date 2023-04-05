import ctypes,sys
import os
import time
import pathlib
import shutil
import webbrowser
import pywinauto
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import winapps
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QWidget
from guidata.utils import is_program_installed
from main import *
from main import MainWindows
from ui_Download import Ui_Download
from main import *
import win32api as w
from pathlib import Path
from subprocess import Popen
import subprocess
from elevate import elevate
from pyuac import main_requires_admin
import glob as gb
import winreg
import win32com.client
from pywinauto import application
import win32gui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def DownloadAndLoadingSoft(self,url,xpath_site,file,process,search,button):
    options = webdriver.ChromeOptions()
    prefs = {'safebrowsing.enabled': 'false'}
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)
    browser.get(url)
    # full xpath для нахождения кнопки Download
    xpath = xpath_site
    browser.find_element(By.XPATH, xpath).click()

    file_path = file
    # Не закрывайте браузер, пока файл в папке "Загрузки" не будет полностью загружен.
    while not os.path.isfile(file_path):
        time.sleep(1)
    print("Файл загружен!")
    browser.quit()
    proces = subprocess.Popen(process, shell=True)
    proces.wait()
    if os.path.isdir(search):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/image/icon/icons8-галочка-64.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        button.setIcon(icon1)
def buttonViberDownload(self):
    url='https://www.viber.com/ru/download/'
    xpath_site = '/html/body/div[1]/div/main/div/div[2]/div/div[2]/span[1]/a'
    file = f"C:/Users/{self.nameUsers}/Downloads/ViberSetup.exe"
    process = f'/Users/{self.nameUsers}/Downloads/ViberSetup.exe'
    search=f"C:/Users/{self.nameUsers}/AppData/Roaming/ViberPC"
    button = self.pushDownloadViber
    self.DownloadAndLoadingSoft(url,xpath_site,file,process,search,button)




