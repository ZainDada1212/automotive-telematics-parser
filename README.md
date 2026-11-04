# Vehicle Telematics Log Parser

A Python-based ETL pipeline designed to ingest, process, and structure raw vehicle telemetry data for downstream analytics and storage.

## Overview

Modern vehicles generate high-volume telemetry logs containing speed, engine status, fuel levels, and diagnostic indicators. This tool automates the ingestion of raw vehicle log files, handles missing or corrupted data points using Pandas, and structures the processed records into an SQLite database for querying.

## Tech Stack

* **Language:** Python 3.x
* **Data Processing:** Pandas
* **Database:** SQLite3
* **Version Control:** Git & GitHub

## Repository Structure

```text
automotive-telematics-parser/
├── parser.py              # Main execution script / ETL pipeline
├── vehicle_logs.csv       # Raw sample telemetry log data
├── vehicle_telematics.db  # SQLite database destination
└── README.md              # Project documentation