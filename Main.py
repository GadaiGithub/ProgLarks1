import PySimpleGUI as sg
import sys,random,glob,os
sg.theme("DarkGreen")
kir=["print(\"Hello,world!\")"]
tab=0
widths=800
heights=600
sda=0
file_list = glob.glob('*', recursive=True)
name_list = [os.path.basename(file) for file in file_list]
fl="\n".join(name_list)
t1=sg.Tab("TextEditor",[[sg.InputText(default_text="tmp.py",key="fnam1",size=(20,10)),sg.Button(button_text="Save",key="save",size=(10,1)),sg.Button(button_text="Read",key="read",size=(10,1)),sg.Button(button_text="->",key="Next",size=(10,1)),sg.Button(button_text="<-",key="Back",size=(10,1)),sg.Button(button_text="Save&Play",key="play",size=(10,1))],[sg.Multiline(default_text="print(\"Hello,world!\")",size=(widths-10,heights-20),font=("Arial",15),key="ftex1")]]) 
t2=sg.Tab("filelist",[[sg.Text(text=fl)]])
layout=[
    [sg.TabGroup([[t1,t2]])]
]
window=sg.Window("KSW Proglarks2.0",layout,size=(widths,heights))
while True:
    event,values=window.read()
    if event is None:
        break
    if event == "save":
        f=open(values["fnam1"],"w")
        f.write(values["ftex1"])
        kir.append(values["ftex1"])
    if event == "read":
        window["ftex1"].update("")
        for line in open(values["fnam1"],"r").readlines():
            window["ftex1"].print(line)
    if event == "Next" and sda <= len(kir)-2:
        sda+=1
        window["ftex1"].update(kir[sda])
    if event == "Back" and sda >= 2:
        sda-=1
        window["ftex1"].update(kir[sda])
    if event == "Play":
        f=open(values["fnam1"],"w")
        f.write(values["ftex1"])
        kir.append(values["ftex1"])
        os.system("start "+values["fnam1"])
