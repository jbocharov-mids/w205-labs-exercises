# Exercise 2


## Prerequisites

Before the project can be run, the follow administrative actions may be needed:
- Create psql database Tcount
- Create user `postgres` with password `pass`

### Creating the Tcount database

Postgres needs to be configured and running at (relative to the Spark cluster) `localhost:5432` with the user `postgres` identified by the password `pass` having full rights to the `Tcount` database.

The database (if it does not exist) is created using

```sh
createdb Tcount
```

### Creating the postgres user in the Tcount database

Run the `psql` shell for the Tcount database:

```sh
psql -s Tcount
```

Then, inside the prompt, run the following adminstrative command:

```sql
CREATE USER postgres PASSWORD 'pass';
CREATE DATABASE Tcount;
GRANT ALL PRIVILEGES ON DATABASE Tcount TO postgres;
```

Finally, the `Tcount` database needs to have a single `Tweetwordcount` table with `word` character string column and `count` integer. It can be created with the following DDL:

```sql
CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);
```

### Python

The solution requires Python 2.7 with the `tweepy` and `psycopg2` packages installed, as well as Apache Storm, Streamparse, and their dependency chains.

## Running the Twitter ingest solution

Assuming the above prerequisites are met, the xcopy the `exercise2/tweetwordcount` application to the target server. 

On the target server, navigate to the `tweetwordcount` directory, and run it as a Streamparse application using `sparse run`.

```sh
cd tweetwordcount
sparse run
```

## Running the serving scripts

Copy the `exercise_2/finalresults.py` and `exercise_2/histogram.py` scripts to the target server. Run them per assignment instructions using `python <script> [<arg>]`.