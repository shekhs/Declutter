# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:19:58 2020

@author: Shushank
"""
import os
def MakeIfNotExist(foldr):
    if not os.path.exists(foldr):
        os.makedirs(foldr)

def move(folder,files):
    for file in files:
        os.replace(file,f"{folder}/{file}")

MakeIfNotExist("Imgs")
MakeIfNotExist("Docs")
MakeIfNotExist("Media")
MakeIfNotExist("Others")

files=os.listdir()
files.remove("declutter.py")        

imgExt=[".jpg",".png",".jpeg",".gif"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExt]
 
docExt=[".doc",".pptx",".pdf",".ppt",".txt"]
documents=[file for file in files if os.path.splitext(file)[1].lower() in docExt]

mediaExt=[".mov",".mp4",".mp3",".flv",".avi"]
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

others=[]
for file in files:
    if ((file not in images) and (file not in medias) and (file not in documents) and os.path.isfile(file)): 
        others.append(file)

move("Imgs",images)
move("Docs",documents)
move("Media",medias)
move("Others",others)
