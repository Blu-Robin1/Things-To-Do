@echo off
REM Start Docker Compose in detached mode
docker compose up -d

REM Wait a few seconds to make sure the container is running
timeout /t 1

REM Open the browser
start http://localhost:3000