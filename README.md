# COVID-19 Tracker using Desktop Notifications [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
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
2. Just search Windows Task scheduler in the Start Menu and launch the application. Please refer screenshots given below. 

* Select **Create Basic Task** option.
![image](https://user-images.githubusercontent.com/29462447/78518901-5541a800-77df-11ea-88a7-b88aee91761a.png)

* Enter the name of the task and suitable description, I took it as COVID 19 Tracker INDIA.
![image](https://user-images.githubusercontent.com/29462447/78519033-ab165000-77df-11ea-901a-8adf5d465f95.png)

* Set the frequency for task execution, i.e daily,weekly,monthly etc.
![image](https://user-images.githubusercontent.com/29462447/78519053-b8333f00-77df-11ea-9265-ad468db55bf4.png)

* Set the time interval(s), since I want to execute our script daily.
![image](https://user-images.githubusercontent.com/29462447/78519076-ca14e200-77df-11ea-946b-739697b3d2d0.png)

* Select the action - **Start a program**, as we just want to execute the code periodically. We can send E-mails , display messages too but these two features will be soon removed after some subsequent patches.
![image](https://user-images.githubusercontent.com/29462447/78519100-def17580-77df-11ea-874e-53bb288a673f.png)

* Click on **Browse** to select the ***covid_notify.bat*** file. Please note you have to edit the executable batch file by entering the details of your Python Installation Directory as well as the location of storage of your Python script. You can add the paths in the batch file I have attached here.
![image](https://user-images.githubusercontent.com/29462447/78519161-119b6e00-77e0-11ea-9b42-dfd1715a82fa.png)

Finally, click on save to create the Task. Now, completely forget about it !! As you can now receive Desktop Notifications at the time interval set by you. Happy Automation :)

![image](https://user-images.githubusercontent.com/29462447/78519896-4dcfce00-77e2-11ea-873d-749b88b00922.png)
