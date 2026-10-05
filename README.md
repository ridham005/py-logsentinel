# Py-LogSentinel 

A lightweight Python-based security log analyzer and anomaly detection tool designed to parse access and authentication logs, detect brute-force attempts, and surface suspicious activity indicators.

## Features (Planned / In Progress)
- **Log Ingestion:** Support for SSH (`/var/log/auth.log`) and Web Server (`access.log`) formats.
- **Brute-Force Detection:** Automated alert thresholds for repeated failed authentication attempts by IP.
- **Anomaly Detection:** Identification of unusual status codes (e.g., spikes in 401/403/500 errors).
- **Exportable Reports:** Generates structured JSON and CLI summary tables for incident triage.

## Project Structure
```text
py-logsentinel/
├── sentinel/
│   ├── __init__.py
│   ├── parser.py        # Log extraction and regex tokenization
│   ├── detector.py      # Threshold logic & brute-force checks
│   └── reporter.py      # Output formatting (CLI / JSON)
├── samples/             # Sanitized mock log files for testing
├── main.py              # CLI entry point
├── requirements.txt     # Python dependencies
└── README.md
