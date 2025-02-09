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
log-processing-pipeline/
│── logs/                 # Directory being monitored (input logs)\
│── output/               # Processed logs stored as JSON (before upload)\
│── main.py               # Main script for monitoring and processing\
│── README.md             # Project documentation
