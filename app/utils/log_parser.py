def parse_log(log_line):
    try:
        parts = log_line.split()
        return {
            "ip_address": parts[0],
            "user": parts[2],
            "request": parts[4].strip('"'),
            "status": int(parts[5]),
            "body_bytes_sent": int(parts[6]),
            "referer": parts[7].strip('"'),
            "user_agent": parts[8].strip('"'),
            "request_time": float(parts[9].split('=')[1])
        }
    except Exception as e:
        return {"error": str(e)}
