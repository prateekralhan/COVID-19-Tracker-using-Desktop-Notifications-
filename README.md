# COVID-19-Tracker-using-Desktop-Notifications
Instead of manually navigating to the Website everytime to get the current status of the COVID 19 cases in India, I created this automated python script which can be easily executed to receive notifications for the COVID 19 Cases on your Desktop whenever you want.

Note: 
* The intention of this simple idea is not to create any form of havoc among others' minds regarding the current state of our country as well as the entire world when the no. of cases are increasing at an ever-increasing rate. This is just a humble attempt so that I as a tech aficionado can contribute to our society in the tiniest manner possible. Please take care and stay safe everyone !!
* The data for this script is taken from [here:](https://www.mohfw.gov.in/) 

### System Requirements:
1. plyer (python package for receing desktop notifications in Windows)
2. urllib3 
3. beautifulsoup4 (for HTML parsing of the website)
4. requests

### Installation and Execution:
Simply execute **pip install <package_name>** or **conda install <package_name>** to install the necessary packages.
* You can execute the script using Terminal/CMD/Powershell by using command: **python covid_notify.py**

## Scheduling the script execution:
1. We won't use anything out of the box. Let us make usage of the ***Windows Task Scheduler** present in our WindowsOS.


