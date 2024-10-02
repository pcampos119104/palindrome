# List all just commands
default:
  just --list

# Build the docker image
build:
  docker compose build

# Run the Django app in development mode
runserver:
  docker compose up --build

# Run manage.py inside the container
mng command:
  docker compose run --rm web python manage.py {{command}}

