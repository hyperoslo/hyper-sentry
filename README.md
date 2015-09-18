# Hyper Sentry

Hyper's custom [Sentry](https://github.com/getsentry/sentry) repository with
support for Heroku.

> Sentry is a realtime event logging and aggregation platform. It specializes
> in monitoring errors and extracting all the information needed to do a proper
> post-mortem without any of the hassle of the standard user feedback loop
> realtime, platform-agnostic error logging and aggregation platform


## Requirements

- Python 2.7.8
- virtualenv
- pip
- PostgreSQL


## Setup

    $ virtualenv .virtualenv --no-site-packages
    $ source .virtualenv/bin/activate
    $ pip install -r requirements.txt


## Environment variables

Copy the sample environment file and update accordingly:

    $ cp .env-sample .env
    
Make sure to generate a new unique `SECRET_KEY`.


## Database Creation

    $ psql template1 -c 'CREATE DATABASE "hyper-sentry-development"'


## Running Sentry (in virtual environment)

    $ source .virtualenv/bin/activate
    $ sentry --config=config.py start

Alternatively, using [Foreman](https://github.com/ddollar/foreman):

    $ foreman start


## Deployment to Heroku

Add the application remote:

    $ git remote add heroku git@heroku.com:hyper-sentry.git

Deploying:

    $ git push heroku master

You may also need to run:

    $ heroku run sentry --config=config.py upgrade
