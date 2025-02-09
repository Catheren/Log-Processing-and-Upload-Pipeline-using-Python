import os
import json
import time
import re
import boto3


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# AWS S3 Configuration
BUCKET_NAME = "<your s3 bucket name>"
AWS_REGION = "<AWS region>"
LOCAL_LOG_FOLDER = "logs"  # Directory to watch for new logs
PROCESSED_FOLDER = "output"  # Where processed logs will be stored 
# Initialize S3 client
s3 = boto3.client("s3", region_name="us-east-1")

# Regex to extract log details
LOG_PATTERN = re.compile(r'time="([^"]+)"\s*'     # Capture timestamp
        r'level=(\w+)\s*'        # Capture log level
        r'msg="([^"]+)"\s*'      # Capture message
        r'file="([^"]+)"\s*'     # Capture file path
        r'func=([\w/.]+)\s*'     # Capture function
        r'kind=(\w+)'  
                        )

# Function to process logs and save as JSON
def process_log(file_path):
    log_entries = []
    with open(file_path, "r") as log_file:
        for line in log_file:
            match = LOG_PATTERN.search(line)
            if match:
                log_entries.append(match.groupdict())  # Convert regex match to dictionary
    
    json_filename = os.path.basename(file_path).replace(".txt", ".json")
    json_filepath = os.path.join(PROCESSED_FOLDER, json_filename)
    with open(json_filepath, "w") as json_file:
        json.dump(log_entries, json_file, indent=4)
    
    print(f"✅ Processed {file_path} → {json_filepath}")
    return json_filepath

# Function to upload JSON file to S3
def upload_to_s3(file_path):
    file_name = os.path.basename(file_path)
    s3_key = f"logs/{file_name}"
    s3.upload_file(file_path, BUCKET_NAME, s3_key)
    print(f"✅ Uploaded {file_path} to s3://{BUCKET_NAME}/{s3_key}")

# Function to handle file creation events
def on_created(event):
    if event.is_directory or not event.src_path.endswith(".txt"):
        return  # Ignore directories and non-log files
    
    time.sleep(2)  # Small delay to avoid file lock issues
    print(f"📌 New log detected: {event.src_path}")
    json_file = process_log(event.src_path)
    upload_to_s3(json_file)

# Function to start monitoring logs
def start_monitoring():
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)  # Create folder if not exists
    
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created  # Assign event function
    
    observer = Observer()
    observer.schedule(event_handler, LOCAL_LOG_FOLDER, recursive=False)
    observer.start()
    
    print(f"👀 Monitoring {LOCAL_LOG_FOLDER} for new logs...")
    
    try:
        while True:
            time.sleep(10)  # Keep running
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

# Run the monitoring function
if __name__ == "__main__":
    start_monitoring()
