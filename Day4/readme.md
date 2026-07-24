</> Markdown
# DBTH Near-Live Performance API
 
## Introduction
 
This API shows near-live performance for DBTH including current A&E wait times and number of waiters in A&E (both updated hourly).  Also Referral to Treatment average weeks wait, updated daily.  This API would not replace nationally available data, but would instead provide an earlier version of a subset of performance metrics.
The initial rollout of this API is a FastAPI prototype on  a virtual PC. It will use hard-coded values of sample data only to prove the concept and demonstrate the endpoint.
In a future version, the hard-coded data would be replaced by a database table, refreshed hourly from the DBTH data warehouse.
 
Access to the API will be similar to existing national API’s for NHS data, for example…

ODS Data https://digital.nhs.uk/developer/api-catalogue/organisation-data-service-ord
Public Health Data  https://fingertips.phe.org.uk/profile/guidance/supporting-information/ap

 
## Target Users
DBTH operational managers, partner organisations, website developers, dashboard developers, mobile alert app (future development).
 
## Example Endpoints##
- GET /v1/organisations/RP5/performance/latest
- GET /v1/organisations/RP5/performance/history/rtt?days=7


##Examples URL's for prototype

http://127.0.0.1:8000/v1/organisations/RP5/performance/latest
http://127.0.0.1:8000/v1/organisations/RP5/performance/history/rtt
http://127.0.0.1:8000/v1/organisations/RP5/performance/history/rtt?days=7

 
## Product Backlog

- Define API purpose and users

- Define metrics and JSON structure

- Build Endpoints using hard-coded values

- Publish to Github

- Design future database integration

- Propose additional usage of API e.g. mobile app, dashboards and websites

