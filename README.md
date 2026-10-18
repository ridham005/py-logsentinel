
# Py-LogSentinel

A lightweight, modular Python-based security log analyzer and anomaly detection CLI designed to parse authentication and web server logs, detect brute-force attempts, and surface actionable incident triage indicators.

---

## Core Capabilities

- **Auth and Access Log Ingestion:** Parses standard Linux SSH (`/var/log/auth.log`) and Web Server (`access.log`) formats using regex tokenization.
- **Brute-Force Detection:** Flags source IP addresses exceeding configurable failed authentication threshold limits within sliding windows.
- **Anomaly Heuristics:** Identifies anomalous spikes in HTTP error codes (`401`, `403`, `500`) and rapid sequential connection attempts.
- **Incident Triage Reporting:** Generates human-readable CLI summary tables and structured JSON outputs designed for SIEM pipeline integration.

---

## Installation & Setup

### Requirements
- Python 3.9+
- Linux / macOS / WSL2 environment

### Setup Instructions
```bash
git clone https://github.com/ridham005/py-logsentinel.git
cd py-logsentinel
pip install -r requirements.txt

```

---

## Usage Examples

### 1. Analyze Authentication Logs

Run baseline brute-force analysis with a failure threshold:

```bash
python main.py --file samples/auth.log --threshold 5

```

### 2. Structured JSON Export for SIEM Ingestion

Export detection output directly to JSON for automated downstream pipeline parsing:

```bash
python main.py --file samples/auth.log --threshold 5 --export json --output report.json

```

---

## Sample CLI Output

```text
[+] Parsing: samples/auth.log ...
[+] Analyzed 1,420 events across 18 unique source addresses.

[!] SUSPICIOUS ACTIVITY DETECTED:
+-----------------+------------------+---------------+----------------------+
| Source IP       | Failed Attempts  | First Seen    | Status               |
+-----------------+------------------+---------------+----------------------+
| 192.168.1.105   | 14               | 12:04:11 UTC  | [ALERT] Brute-Force  |
| 10.0.0.42       | 8                | 12:06:55 UTC  | [WARN] Threshold Met |
+-----------------+------------------+---------------+----------------------+
[+] Execution finished: Triage report generated successfully.

```

---

## Repository Architecture

```text
py-logsentinel/
├── sentinel/
│   ├── __init__.py
│   ├── parser.py       # Log extraction and regex tokenization
│   ├── detector.py     # Threshold heuristics and brute-force evaluation
│   └── reporter.py     # CLI table formatting and JSON serialization
├── samples/            # Sanitized test log samples
├── main.py             # CLI entrypoint and argument parser
├── requirements.txt    # Project dependencies
└── README.md

```

---

## Development Roadmap

* [x] Linux SSH `auth.log` parsing and threshold-based brute-force detection
* [x] Structured JSON and CLI table reporting
* [ ] Automated MITRE ATT&CK mapping (T1110 - Brute Force)
* [ ] Local LLM integration for automated incident triage summaries and plain-English threat reporting
* [ ] Sigma rule translation support for exportable SIEM detection queries

---

## Contributing & Collaboration

Contributions, issues, and feature collaborations are welcome. If you are interested in collaborating on the roadmap items above (MITRE ATT&CK mapping, local LLM triage integration, or Sigma rule exports), feel free to open an issue, submit a pull request, or reach out directly:

- **LinkedIn:** [Ridham Patel](https://www.linkedin.com/in/ridhampatel-sec)
- **GitHub:** [@ridham005](https://github.com/ridham005)
