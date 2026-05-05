#!/bin/bash

echo "Starting Auto-Healing Monitor..."

while true; do
    if [ -f alert.txt ]; then
        echo "⚠️ Alert detected! Fixing system..."
        
        # Restart the target Docker container
        sudo docker restart webapp
        
        # Remove the alert file after fixing
        rm alert.txt
        echo "✅ System recovered and alert cleared."
    fi
    # Check every 5 seconds
    sleep 5
done
