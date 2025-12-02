#!/bin/sh
while true; do
  echo "Connecting to server..."
  curl http://server:8080
  sleep 5
done
