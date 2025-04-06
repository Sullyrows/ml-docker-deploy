#!/bin/bash

# Get the project root directory (where the script is run from)
PROJECT_ROOT=$(pwd)

# Path to the compose file
COMPOSE_FILE="$PROJECT_ROOT/arima/compose.yml"

# Check if the compose file exists
if [ ! -f "$COMPOSE_FILE" ]; then
    echo "Error: Compose file not found at $COMPOSE_FILE"
    exit 1
fi

# Run docker-compose with the specified file
echo "Running docker-compose with file: $COMPOSE_FILE"
trap 'echo -e "\nStopping containers..."; docker compose -f "$COMPOSE_FILE" down' INT

docker compose -f "$COMPOSE_FILE" up

if [ $? -ne 0 ]; then
    echo "Error running docker-compose"
    exit 1
fi
