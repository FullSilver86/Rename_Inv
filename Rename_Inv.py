import os
from os import listdir
import time
import fitz
import shutil
from datetime import date



company_list = ["POLSKI KONCERN", "Trafineo","Union Tank", "DKV", "Shell", "LOTOS", "E100", "Telepass", "Autopay", "SkyCash", "PKO BP", "mPay"]
mypath = "C:\Przemek\\nazwy"
today = date.today()
file_date = today.strftime("%b-%d-%Y")

try:
    os.startfile(mypath)
except FileNotFoundError:
    os.mkdir("C:\Przemek\\nazwy")
    os.startfile(mypath)

print("Proszę przegrać pliki do otwartego folderu, następnie naciśnij enter")
input()


for file in listdir(mypath):
    if file.endswith(".pdf"):
        with fitz.open(f"{mypath}\\{file}") as doc:
            text = ""
            for page in doc:
                text = page.get_text()
                for company in company_list:
                    comp_present = text.find(company)
                    if comp_present != -1:
                        inv_number_pos = text.find("000")
                        inv_number2 = text[inv_number_pos:inv_number_pos+16].replace("/", "_")
                        inv_number = inv_number2.rstrip()
                        shutil.copy(mypath + "\\" + file, mypath + "\\" + file_date + " " + company + " " + inv_number + ".pdf")



