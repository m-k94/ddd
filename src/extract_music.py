import os
import xml.etree.ElementTree as ET
import cv2
import matplotlib.pyplot as plt 

PATH = "../data/sources/Hauptmann1853/"

tree = ET.parse(PATH + "Hauptmann1853_tei.xml")
root = tree.getroot() 

ns = { "tei" : "http://www.tei-c.org/ns/1.0" }

for facsimile in root.findall(".//tei:facsimile", ns):
    img_url = facsimile.find(".//tei:graphic", ns).attrib["url"]
    for zone in facsimile.findall(".//tei:zone[@rendition='Music']", ns)[:2]:
        img_id = zone.attrib["{http://www.w3.org/XML/1998/namespace}id"]

        points = zone.attrib["points"]
        ul, ur, lr, ll = points.split()
        x1, y1 = list(map(int, ul.split(",")))
        x2, y2 = list(map(int, lr.split(",")))

        img = cv2.imread(PATH + "Hauptmann1853/" + img_url)
        music_region = img[y1:y2,x1:x2]
        cv2.imwrite(f"../data/music/Hauptmann1853/{img_id}.png", music_region)
    
