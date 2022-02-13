# Backend

## Prerequisites

* Python 3.9+
* Poetry (<https://python-poetry.org/docs/>)
* Docker

## Setup

1. Install dependencies with Poetry. This will also create a virtual environment at `.venv` if it does not exist yet.

   ```bash
   poetry install
   ```

2. Activate the virtual environment. The command is different depending on your OS and shell.
   Alternatively, `poetry shell` may work, but it might not launch the correct shell.

   | OS                            | Shell                           | Command                          |
   |-------------------------------|---------------------------------|----------------------------------|
   | Windows                       | PowerShell (preferred)          | `.venv/Scripts/Activate.ps1`     |
   | Windows                       | Command Prompt (don't use this) | `.venv/Scripts/activate.bat`     |
   | Windows                       | Unix shell (eg. Git Bash)       | `source .venv/Scripts/activate`  |
   | Unix-like (eg. Ubuntu, macOS) | Unix shell (eg. bash, zsh)      | `source .venv/bin/activate`      |
   | Unix-like                     | fish                            | `source .venv/bin/activate.fish` |

3. Copy the `template.env` file to `.env`, which will be used to configure the application.

   ```bash
   cp template.env .env
   ```

4. Set up the database. Refer to [Database setup](#database-setup) for instructions on setting up the database within Docker.

5. Run database migrations.

   ```bash
   python manage.py migrate
   ```

6. Seed the database. Refer to [Seed data](#seed-data) for instructions.

7. Set up pre-commit hooks.

   ```bash
   pre-commit install
   ```

8. Run the test suite with coverage

   ```bash
   pytest --cov
   ```

9. Create a local superuser.

   ```bash
   python manage.py createsuperuser
   ```

10. Start the development server. This will listen on localhost:8000.

      ```bash
      python manage.py runserver
      ```

11. Start the frontend server. This will listen on localhost:3000

## Database setup

### Local PostgreSQL installation (Preferred)

1. Use `psql` to create a new user and database for the application with appropriate permissions:

```bash
echo "create user sample login password 'password';
create database sample owner sample;
alter user sample createdb;" | psql -d postgres
```

### Running PostgreSQL in Docker

1. Install Docker for your system [here](http://www.docker.com)

2. Create a volume to persist the database between container restarts:

   ```bash
   docker volume create sample_db
   ```

3. Start the database container:

   ```bash
   docker run -d -v sample_db:/var/lib/postgresql/data -e POSTGRES_USER=sample -e POSTGRES_PASSWORD=password -e POSTGRES_DB=sample -p 5432:5432 --name sample_db postgres
   ```

## Seed data

1. Use `pg_restore` to load the database dump.

   ```bash
   docker exec -i sample_db pg_restore -U sample -v -d sample < ./db_dump.tar.gz
   ```
