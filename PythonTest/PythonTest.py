import matplotlib.pyplot as plt
import matplotlib.dates as pld
import numpy as np
import csv
import dateutil.parser
import datetime

download=[]
upload=[]
date=[]
datePlot=[]


with open('file.csv') as csv_file:
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
    myFmt = pld.DateFormatter('%m-%d | %H:%M')

    plt.grid(True, linewidth=0.1, color='black', linestyle='-')
    plt.gca().xaxis.grid(linewidth=0.5)
    plt.yticks(np.arange(0, 50, 5))
    plt.plot(datePlot, download, 'r.', datePlot, upload,  'b.')
    plt.bar(datePlot, download, width=0.042, align='center', alpha=0.5)
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_locator(pld.DayLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(myFmt)
    
    plt.title("Data from Speedtest")
    plt.xlabel("date")
    plt.ylabel("download")

    plt.axhline(y=2, color='blue', linestyle='-.', linewidth=1)
    plt.axhline(y=45, color='green', linestyle='-.', linewidth=3)

    plt.show()


   # plt.axhline(y=5, color='black', linestyle='--', linewidth=1)
   # i=10
   # while i<44:
   #     plt.axhline(i, color='black', linestyle='--', linewidth=1)
 #       i += 10

    #reg_format = date[a].strftime("%Y-%m-%d %I:%M:%S %p")
    #print(reg_format)

    #for a in range(len(date)):
    #    a.strftime('%Y-%m-%d %H:%M')
        
        
   


#import matplotlib.pyplot as plt
#import csv


#with open('file.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    line_count = 0
#    for row in csv_reader:
#            print(f'\tdownload: {row[6]} || upload {row[7]}.')
#            line_count += 1

#    print(f'Processed {line_count} lines.')