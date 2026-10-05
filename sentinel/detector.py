from collections import defaultdict

def detect_bruteforce(events, threshold=5):
    failed_counts = defaultdict(int)
    targeted_users = defaultdict(set)
    
    for event in events:
        if event['status'] == 'Failed':
            ip = event['ip']
            failed_counts[ip] += 1
            targeted_users[ip].add(event['user'])
            
    alerts = []
    for ip, count in failed_counts.items():
        if count >= threshold:
            alerts.append({
                "ip": ip,
                "failed_attempts": count,
                "targets": list(targeted_users[ip]),
                "status": "CRITICAL"
            })
    return alerts, failed_counts
