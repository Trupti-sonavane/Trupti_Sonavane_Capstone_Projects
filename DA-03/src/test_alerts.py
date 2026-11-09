from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
ALERTS_FILE = PROJECT_DIR / "supply_chain_alerts.csv"


def load_alerts():
    """Load generated alerts from the project CSV file."""
    assert ALERTS_FILE.exists(), "Alerts CSV file was not found!"

    alerts = pd.read_csv(ALERTS_FILE)
    return alerts


def test_alert_file_exists():
    assert ALERTS_FILE.exists()


def test_required_columns_exist():
    alerts = load_alerts()

    required_columns = {
        "alert_type",
        "item_id",
        "message",
        "severity",
    }

    assert required_columns.issubset(set(alerts.columns))


def test_alerts_are_not_empty():
    alerts = load_alerts()

    assert len(alerts) > 0


def test_alert_types_are_valid():
    alerts = load_alerts()

    valid_types = {
        "LOW_STOCK",
        "DELAYED_SHIPMENT",
    }

    assert set(alerts["alert_type"]).issubset(valid_types)


def test_alert_severity_is_valid():
    alerts = load_alerts()

    valid_severities = {"HIGH", "MEDIUM"}

    assert set(alerts["severity"]).issubset(valid_severities)


def test_alert_messages_are_not_empty():
    alerts = load_alerts()

    assert alerts["message"].notna().all()
    assert alerts["message"].str.strip().ne("").all()


if __name__ == "__main__":
    tests = [
        test_alert_file_exists,
        test_required_columns_exist,
        test_alerts_are_not_empty,
        test_alert_types_are_valid,
        test_alert_severity_is_valid,
        test_alert_messages_are_not_empty,
    ]

    passed = 0

    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except Exception as error:
            print(f"FAIL: {test.__name__} - {error}")

    print(f"\nResult: {passed}/{len(tests)} tests passed")

    if passed != len(tests):
        raise SystemExit(1)