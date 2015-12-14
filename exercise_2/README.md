Exercise 2


# Prerequisites

Before the project can be run, the follow administrative actions may be needed:
- Create psql database Tcount
- Create user `postgres` with password `pass`

## Creating the Tcount database

```sh
createdb Tcount
```

## Creating the postgres user in the Tcount database

Run the `psql` shell for the Tcount database:

```sh
psql -s Tcount
```

Then, inside the prompt, run the following adminstrative command:

```sql
CREATE USER postgres PASSWORD 'pass';
CREATE DATABASE Tcount;
GRANT ALL PRIVILEGES ON DATABASE Tcount TO postgres;
\q
```