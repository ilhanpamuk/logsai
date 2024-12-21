from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.geoip_utils import enrich_with_geo
from app.utils.anomaly_detection import detect_anomalies
from app.utils.log_parser import parse_log

router = APIRouter()

class LogItem(BaseModel):
    log: str

@router.post("/analyze")
def analyze_logs(logs: list[LogItem]):
    enriched_logs = []
    request_times = []

    for item in logs:
        parsed_data = parse_log(item.log)
        if "error" in parsed_data:
            continue
        geo_data = enrich_with_geo(parsed_data["ip_address"])
        parsed_data.update(geo_data)
        enriched_logs.append(parsed_data)
        request_times.append(parsed_data["request_time"])

    # Anomali tespiti
    if request_times:
        anomalies = detect_anomalies(request_times)
        for i, log in enumerate(enriched_logs):
            log["anomaly"] = anomalies[i] == -1

    return {"processed_logs": enriched_logs}
