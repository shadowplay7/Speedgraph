import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as pld
import numpy as np
import csv
import dateutil.parser
import datetime
import sys

parser = argparse.ArgumentParser(description='Create plot for speedtest .csv file')
parser.add_argument('-d', '--daysTick', type=int, help='an integer for days tick on axis X. Default: 7.', action="store", default=7)
parser.add_argument('-do', '--download', type=int, help='an integer for download limit on axis Y. Default: 150.', action="store", default=150)
parser.add_argument('-dt', '--downloadTick', type=int, help='an integer for download tick on axis Y. Default: 15.', action="store", default=15)
parser.add_argument('-up', '--upload', type=int, help='an integer for upload on axis Y. Default: 10.', action="store", default=10)
parser.add_argument('-sh', '--showHours', type=str, help="'no' option to hide hours on axis X label. Default: yes.", action="store", default='yes')
parser.add_argument('-a', '--auto', type=str, help="'yes' option to set automatic axis alignment. Default: no.", action="store", default='yes')
parser.add_argument('-W', '--width', type=int, help="plot width. Default: 15.", action="store", default=15)
parser.add_argument('-H', '--height', type=int, help="plot height. Default: 8.", action="store", default=8)
parser.add_argument('-m', '--marker', type=int, help="marker size. Default: 3.", action="store", default=3)
parser.add_argument('-f', '--file',  help="path to file", action="store", default='file.csv')

args = parser.parse_args()

print("Days tick set to: " + str(args.daysTick))
print("Download limit set to: " + str(args.download))
print("Download tick set to: " + str(args.downloadTick))
print("Upload set to: " + str(args.upload))
print("Show hours set to: " + args.showHours)
print("Auto mode set to: " + args.auto)
print("Width set to: " + str(args.width))
print("Height set to: " + str(args.height))
print("Marker size set to: " + str(args.marker))

download=[]
upload=[]
date=[]
datePlot=[]

with open(args.file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
           download.append(float(row[6]))
           upload.append(float(row[7]))
           date.append(row[3])
           continue

    for a in range(len(date)):
        date[a]=datetime.datetime.strptime(date[a], "%Y-%m-%dT%H:%M:%S.%fZ")

    for a in range(len(download)):
        download[a]=download[a]/1000000
        download[a]=float((round(download[a], 3)))

    for a in range(len(upload)):
        upload[a]=upload[a]/1000000
        upload[a]=float((round(upload[a], 3)))

    datePlot = pld.date2num(date)

    if args.showHours == 'yes':
       myFmt = pld.DateFormatter('%m-%d | %H:%M')
    else:
       myFmt = pld.DateFormatter('%m-%d')

    if args.auto == 'yes':
       plt.yticks(np.arange(0, max(download)+15, max(download)/10))
       plt.axhline(y=args.upload, color='blue', linestyle='-.', linewidth=1)
       plt.axhline(y=args.download, color='green', linestyle='-.', linewidth=1)
       if len(date) < 15:
              plt.gca().xaxis.set_major_locator(pld.DayLocator(interval=1))
       else:
              plt.gca().xaxis.set_major_locator(pld.AutoDateLocator())
    else:
       plt.axhline(y=args.upload, color='blue', linestyle='-.', linewidth=1)
       plt.axhline(y=args.download, color='green', linestyle='-.', linewidth=1)
       plt.yticks(np.arange(0, args.download+10, args.downloadTick))
       plt.gca().xaxis.set_major_locator(pld.DayLocator(interval=args.daysTick))
       plt.yticks(np.arange(0, max(download)+15, args.downloadTick))

    plt.grid(True, linewidth=0.1, color='black', linestyle='-')
    plt.gca().xaxis.grid(linewidth=0.5)
    plt.plot(datePlot, download, 'r.', datePlot, upload,  'b.', markersize=args.marker)
    plt.bar(datePlot, download, width=0.042, align='center', alpha=0.5)
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.gcf().set_size_inches(args.width,args.height)
  
    plt.title("Data from Speedtest")
    plt.xlabel("date")
    plt.ylabel("download")

    plt.show()
