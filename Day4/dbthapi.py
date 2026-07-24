from fastapi import FastAPI, HTTPException, Query

app = FastAPI(
    title="DBTH Near-Live Performance API",
    description="Prototype API for publishing fictional DBTH performance metrics.",
    version="1.0.0"
)

# Fictional sample performance data
performance_history = [
    {
        "reporting_date": "2026-07-18",
        "rtt": 72.8,
        "ae_4_hour": 78.2,
        "diagnostics": 89.4,
        "opel_level": 3
    },
    {
        "reporting_date": "2026-07-19",
        "rtt": 73.0,
        "ae_4_hour": 79.1,
        "diagnostics": 89.8,
        "opel_level": 3
    },
    {
        "reporting_date": "2026-07-20",
        "rtt": 73.1,
        "ae_4_hour": 80.3,
        "diagnostics": 90.1,
        "opel_level": 2
    },
    {
        "reporting_date": "2026-07-21",
        "rtt": 73.2,
        "ae_4_hour": 80.8,
        "diagnostics": 90.5,
        "opel_level": 2
    },
    {
        "reporting_date": "2026-07-22",
        "rtt": 73.3,
        "ae_4_hour": 81.0,
        "diagnostics": 91.0,
        "opel_level": 2
    },
    {
        "reporting_date": "2026-07-23",
        "rtt": 73.4,
        "ae_4_hour": 81.2,
        "diagnostics": 91.4,
        "opel_level": 2
    },
    {
        "reporting_date": "2026-07-24",
        "rtt": 73.5,
        "ae_4_hour": 81.4,
        "diagnostics": 92.0,
        "opel_level": 2
    }
]


# Home route
@app.get("/")
def home():
    return {
        "message": "DBTH Near-Live Performance API",
        "organisation_code": "RP5",
        "documentation": "/docs"
    }


# Get the latest performance metrics
@app.get("/v1/organisations/RP5/performance/latest")
def get_latest_performance():
    latest = performance_history[-1]

    return {
        "organisation_code": "RP5",
        "organisation_name": (
            "Doncaster and Bassetlaw Teaching Hospitals "
            "NHS Foundation Trust"
        ),
        "reporting_date": latest["reporting_date"],
        "provisional": True,
        "metrics": {
            "rtt": {
                "value": latest["rtt"],
                "unit": "percent",
                "target": 92.0,
                "description": (
                    "Percentage of incomplete RTT pathways "
                    "within 18 weeks"
                )
            },
            "ae_4_hour": {
                "value": latest["ae_4_hour"],
                "unit": "percent",
                "target": 95.0,
                "description": (
                    "Percentage of A&E attendances completed "
                    "within four hours"
                )
            },
            "diagnostics": {
                "value": latest["diagnostics"],
                "unit": "percent",
                "target": 99.0,
                "description": (
                    "Percentage of diagnostic patients waiting "
                    "less than six weeks"
                )
            },
            "opel_level": {
                "value": latest["opel_level"],
                "unit": "level",
                "description": "Current operational pressure escalation level"
            }
        }
    }


# Get RTT history
@app.get("/v1/organisations/RP5/performance/history/rtt")
def get_rtt_history(
    days: int = Query(
        default=7,
        ge=1,
        le=30,
        description="Number of days of RTT history to return"
    )
):
    if days > len(performance_history):
        raise HTTPException(
            status_code=400,
            detail=(
                f"Only {len(performance_history)} days of sample data "
                "are currently available."
            )
        )

    selected_data = performance_history[-days:]

    rtt_history = []

    for record in selected_data:
        rtt_history.append(
            {
                "reporting_date": record["reporting_date"],
                "value": record["rtt"]
            }
        )

    return {
        "organisation_code": "RP5",
        "organisation_name": (
            "Doncaster and Bassetlaw Teaching Hospitals "
            "NHS Foundation Trust"
        ),
        "metric_code": "rtt",
        "metric_name": "Referral to Treatment performance",
        "unit": "percent",
        "target": 92.0,
        "days_returned": days,
        "provisional": True,
        "data": rtt_history
    }
