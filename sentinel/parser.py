import re

LOG_REGEX = re.compile(
    r'^(?P<month>\w{3})\s+(?P<day>\d+)\s+(?P<time>[\d:]+)\s+\S+\s+sshd\[\d+\]:\s+'
    r'(?P<status>Failed|Accepted)\s+(?:password|publickey)\s+for\s+(?:invalid user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>[\d.]+)'
)

def parse_auth_line(line):
    match = LOG_REGEX.search(line.strip())
    if match:
        return match.groupdict()
    return None

def parse_log_file(filepath):
    events = []
    with open(filepath, 'r', errors='ignore') as f:
        for line in f:
            parsed = parse_auth_line(line)
            if parsed:
                events.append(parsed)
    return events
