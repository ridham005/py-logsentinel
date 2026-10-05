import argparse
import sys
from sentinel.parser import parse_log_file
from sentinel.detector import detect_bruteforce

def main():
    parser = argparse.ArgumentParser(description="Py-LogSentinel - Security Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to authentication log file")
    parser.add_argument("--threshold", type=int, default=5, help="Failed attempt threshold for brute-force alert")
    args = parser.parse_args()

    print(f"\n[*] Py-LogSentinel Initializing...")
    print(f"[*] Ingesting log file: {args.file}")

    try:
        events = parse_log_file(args.file)
    except FileNotFoundError:
        print(f"[!] Error: File '{args.file}' not found.")
        sys.exit(1)

    print(f"[+] Parsed {len(events)} relevant SSH authentication events.")

    alerts, stats = detect_bruteforce(events, threshold=args.threshold)

    print("\n" + "=" * 55)
    print("                 DETECTION REPORT                 ")
    print("=" * 55)

    if not alerts:
        print("[*] No brute-force signatures detected above threshold.")
    else:
        for alert in alerts:
            print(f"[!] [ALERT] Potential Brute-Force Detected!")
            print(f"    Source IP       : {alert['ip']}")
            print(f"    Failed Attempts : {alert['failed_attempts']}")
            print(f"    Target Accounts : {', '.join(alert['targets'])}")
            print(f"    Severity        : {alert['status']}\n")

    print("=" * 55)
    print("Summary:")
    for ip, count in stats.items():
        print(f"  - IP: {ip:<15} | Failed Attempts: {count}")
    print("=" * 55 + "\n")

if __name__ == "__main__":
    main()
