# Speedgraph
Create simple graph from .csv file created by speedtest-cli

Graph created using matplotlib.

### How to use:
1. Create .csv file from speedtest-cli script. 
2. Rename it to "file".
3. Copy "file" to folder with Speedgraph script.

Gold/Blue line - Download/upload speed set by your ISP. Values can be changed in script or by arguments.<br/>
You can set up speedtest-cli script in Windows Task Scheduler to get more data e.g., from every hour.<br/>

![alt text](https://github.com/shadowplay7/Speedgraph/blob/master/example.PNG)

### usage: <br/>
```
Speedgraph.py [-h] [-d DAYSTICK] [-do DOWNLOAD] [-dt DOWNLOADTICK]
                     [-up UPLOAD] [-sh SHOWHOURS] [-a AUTO] [-W WIDTH]
                     [-H HEIGHT] [-m MARKER] [-f FILE]
```

Create plot for speedtest .csv file<br/>

### optional arguments:<br/>

| Short | Long name | matavar | Description | Default |
| :--- | :--- | :--- | :---  | :---: |
| -h  | --help         |  | show this help message and exit |  |
| -d  | --daysTick     | DAYSTICK      | an integer for days tick on axis X           | 7          |
| -do | --download     | DOWNLOAD      | an integer for download limit on axis Y      | 150        |
| -dt | --downloadTick | DOWNLOADTICK  | an integer for download tick on axis Y       | 15         |
| -up | --upload       | UPLOAD        | an integer for upload on axis Y              | 10         |
| -sh | --showHours    | SHOWHOURS     | 'no' option to hide hours on axis X label    | yes        |
| -a  | --auto         | AUTO          | 'yes' option to set automatic axes alignment | no         |
| -W  | --width        | WIDTH         | plot width                                   | 15         |
| -H  | --height       | HEIGHT        | plot height                                  | 8          |
| -m  | --marker       | MARKER        | marker size                                  | 3          |
| -f  | --file         | FILE          | path to file                                 | file.csv   |
