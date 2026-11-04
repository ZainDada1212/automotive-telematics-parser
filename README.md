# Automotive Telematics Log Parser

An automated data engineering pipeline built with Python, Pandas, and SQLite to ingest, clean, and analyze raw automotive telematics logs.

## Features
- **Data Ingestion:** Reads continuous raw log streams from external CSV sources.
- **Error Filtering:** Isolates device warning states, offline statuses, and connection errors (`ERR_CONNECTION_TIMEOUT`, `ERR_PROTOCOL_MISMATCH`, `ERR_GPS_SYNC_FAIL`).
- **Relational Storage:** Automatically populates an SQLite database (`vehicle_telematics.db`) with structured error records.
- **Automated Reporting:** Executes SQL aggregation queries to summarize total fault counts and error codes per Vehicle ID (VIN).

## Tech Stack
- **Language:** Python 3
- **Data Processing:** Pandas
- **Database:** SQLite3

## How to Run
1. Clone this repository to your local machine.
2. Install dependencies:
   ```bash
   pip install pandas