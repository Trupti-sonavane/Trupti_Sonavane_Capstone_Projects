from pathlib import Path
import os
import json
import pandas as pd
from urllib.request import Request, urlopen

PROJECT_DIR = Path(__file__).resolve().parent.parent
ALERT_FILE = PROJECT_DIR / "supply_chain_alerts.csv"

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

if not WEBHOOK_URL:
    raise ValueError("SLACK_WEBHOOK_URL environment variable is not set.")

if not ALERT_FILE.exists():
    raise FileNotFoundError(f"Alert file not found: {ALERT_FILE}")

alerts = pd.read_csv(ALERT_FILE)

if alerts.empty:
    message = "Retail Supply Chain Update: No active alerts."
else:
    details = alerts.head(10).to_string(index=False)
    message = (
        f"*Retail & Supply Chain Control Tower Alerts*\n"
        f"Total alerts: {len(alerts)}\n\n"
        f"*Alert details (first 10):*\n```{details}```"
    )

payload = json.dumps({"text": message}).encode("utf-8")

request = Request(
    WEBHOOK_URL,
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=20) as response:
    if response.status == 200:
        print("Slack alerts sent successfully!")
    else:
        print("Slack returned status:", response.status)