from fastapi import FastAPI
import sqlite3

app = FastAPI()

DB = "dbth_performance.db"

# Create database and sample data if it doesn't exist
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS performance
(
    reporting_date TEXT,
    rtt REAL,
    ae4hour REAL,
    diagnostics REAL
)
""")

cur.execute("SELECT COUNT(*) FROM performance")

if cur.fetchone()[0] == 0:

    cur.executemany(
        "INSERT INTO performance VALUES (?,?,?,?)",
        [
            ("2026-07-18",72.8,78.2,89.4),
            ("2026-07-19",73.0,79.1,89.8),
            ("2026-07-20",73.1,80.3,90.1),
            ("2026-07-21",73.2,80.8,90.5),
            ("2026-07-22",73.3,81.0,91.0),
            ("2026-07-23",73.4,81.2,91.4),
            ("2026-07-24",73.5,81.4,92.0)
        ]
    )

conn.commit()
conn.close()


@app.get("/")
def home():
    return {"message":"DBTH Performance API (SQLite)"}


@app.get("/v1/organisations/RP5/performance/latest")
def latest():

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    row = conn.execute("""
        SELECT *
        FROM performance
        ORDER BY reporting_date DESC
        LIMIT 1
    """).fetchone()

    conn.close()

    return {
        "organisation_code":"RP5",
        "organisation_name":"Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust",
        "reporting_date":row["reporting_date"],
        "rtt":row["rtt"],
        "ae4hour":row["ae4hour"],
        "diagnostics":row["diagnostics"],
        "data_source":"SQLite"
    }


@app.get("/v1/organisations/RP5/performance/history/rtt")
def history(days:int=7):

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    rows = conn.execute("""
        SELECT reporting_date,rtt
        FROM performance
        ORDER BY reporting_date DESC
        LIMIT ?
    """,(days,)).fetchall()

    conn.close()

    rows=list(reversed(rows))

    return {
        "organisation_code":"RP5",
        "metric":"RTT",
        "days":days,
        "data":[
            {
                "reporting_date":r["reporting_date"],
                "value":r["rtt"]
            }
            for r in rows
        ]
    }