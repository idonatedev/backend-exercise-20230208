# iDonate Backend Exercise

## Overview

- There is a Flask app defined in `backend/web.py` and mounted at `/`.
- There is a FastAPI app defined in `backend/api.py` and mounted at `/api`, with Swagger docs at `/api/docs`.
- The database is SQLite, models are defined in `backend/models.py` and sample data has been loaded.
- `./run_dev.sh` will run the app in development mode on port 8000, with auto-reloading enabled.

## FastAPI Tasks

- Implement a simple FastAPI Dependency that wraps a database session object to use in the following endpoints.
- Implement an endpoint that returns a list of donors in the database for a given Charity, filterable by Date Range.
    - Include (or explain how you would include) aggregated data for "donation_count" and "total_donation_amount" for
      each donor.
- Implement an endpoint that returns a list of donations in the database, sorted by created_at, filterable by Charity
  ID, Donor ID, Campaign ID and/or Date Range.
- Implement an endpoint that returns details for a specific Donation (by ID). Include Donor, Charity and Campaign
  details in the output.

## Flask Tasks

- Implement a "Charity List" view that displays a list of charities in the database by name, with a link to a "Charity
  Detail" view for each charity. The Charity Detail view should display the charity's name, description, and a list of
  donations made to that charity. Include the Donor's name for each donation.
- Implement a "Donor List" view that displays a list of donors in the database by name, with a link to a "
  Donor Detail" view for each donor. The Donor Detail view should display the donor's name, email, and a list of
  donations made by that donor - as well as which Charity and Campaign each donation was made to.
