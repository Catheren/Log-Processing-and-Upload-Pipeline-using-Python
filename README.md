# Log-Processing-and-Upload-Pipeline-using-Python
This project implements an automated log processing pipeline that monitors a directory for new log files, extracts structured data from them, converts them into JSON format, and uploads the processed data to an AWS S3 bucket for storage.
## Features
✅ Real-time monitoring of a local directory for new log files.\
✅ Automated log processing to extract structured data using regular expressions. \
✅ Conversion of log data into JSON format for easy analysis. \
✅ AWS S3 integration for centralized cloud storage. \
✅ Modular and extensible pipeline design.\

## Dependencies
	• Python 3.x
	• watchdog (File system monitoring)
	• boto3 (AWS SDK for S3 interaction)
	• Regular Expressions (re) (Log parsing)
## Project Structure
log-processing-pipeline\
│── logs/                 # Directory being monitored (input logs)\
│── output/               # Processed logs stored as JSON (before upload)\
│── main.py               # Main script for monitoring and processing\
│── README.md             # Project documentation

## Implementation
**1. Install dependencies mentioned using the commands:**
```
pip install boto3
pip install watchdog
```
**2. AWS Configuration**
This script uses boto3 to upload files to AWS S3. Configure AWS credentials using:
```
aws configure
```
Provide your AWS Access Key, Secret, and Region
## How it Works
**1. Monitoring for New Logs**
	• The script monitors the logs/ folder for newly created .txt log files.\
	• It uses the watchdog library to detect filesystem changes in real-time.\
 **2. Processing Log Files**
 	• When a new log file is detected, it reads the content and extracts structured data using regular expressions.\
	• The extracted data includes: \
		○ Timestamp (time)\
		○ Log Level (level)\
		○ Message (msg)\
		○ Source File (file)\
		○ Function Name (func)\
		○ Event Type (kind)\
	• The processed logs are saved in output/ as .json files.\
**3. Uploading to AWS S3**\
	• The script uploads the JSON files to an AWS S3 bucket under logs/ directory.\
	• The boto3 library is used to handle S3 interactions.\

