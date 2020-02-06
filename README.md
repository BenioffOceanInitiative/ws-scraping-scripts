# ws-scraping-scripts
## Scripts for scraping whale-relevant data from external (non-BOI) APIs. 

### about this repo
The bread and butter of this repo are two files: JSON 2 CSV_API Script and GPX_API Script. 
<br/>Both files are python scripts originally designed to scrape data about whale sightings from APIs built by Conserve.io. <br/>The documentation from Conserve.io on using those APIs is the file titled "Conserve.IO API Documentation.txt" 
<br/> The documentation can also be found here: 
https://docs.google.com/document/d/1NImy_RjCgwTyQYrwhryDnx6OqMVGfsHc5BU6Ftbu7ns/edit?ts=5dfaaaab


### system requirements
You need the python library "requests" installed. 
<br/>You can install requests by running "pip install requests" in your terminal. (As shown here: https://pypi.org/project/requests/2.7.0/)
<br/>If you do not have pip installed, you can download the latest python release, which comes with pip, here:
https://www.python.org/downloads/

### running the scripts 
Download the scripts individually into a specific directory or clone the repo into a local directory on your machine. 
<br/>Navigate to that directory in your local machine's terminal and run "python [FILE NAME OF SCRIPT]".
<br/>Follow the user prompts, using your Conserve.io API documentation for guidance. 
<br/>Any files you write will be saved to the same directory where your scripts are saved locally. 

### tips
A few of the Conserve.io APIs require a bounding box (BBOX) parameter. 
<br/>Here is a website that helps you find exact longitude and latitude bounding box values: http://bboxfinder.com/
