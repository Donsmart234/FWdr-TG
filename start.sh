#!/bin/bash
# Start forwarder bot with background keep-alive
termux-wake-lock
nohup python forwarder.py > forwarder.log 2>&1 &
echo "✅ Forwarder bot is now running in the background."
