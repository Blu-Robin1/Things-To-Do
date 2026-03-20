#!/bin/bash
docker compose up -d
sleep 0.5
xdg-open http://127.0.0.1:3000
