from sklearn.ensemble import IsolationForest
import time

def encode(line):
    # Simple encoding: 1 for ERROR, 0 for INFO
    return 1 if "ERROR" in line else 0

data = []

print("Training model on existing logs...")
# Initial training phase
try:
    with open("logs.txt") as f:
        for line in f:
            data.append([encode(line)])
except FileNotFoundError:
    print("logs.txt not found. Please run log_generator.py first.")
    exit()

if not data:
    print("Not enough data to train. Please wait for logs to generate.")
    exit()

# Train the Isolation Forest model
model = IsolationForest(contamination=0.2)
model.fit(data)

print("Model trained successfully. Starting continuous monitoring...")

# Continuous monitoring phase
while True:
    try:
        with open("logs.txt") as f:
            # Read the last 5 log lines
            lines = f.readlines()[-5:]
        
        if len(lines) >= 5:
            test = [[encode(l)] for l in lines]
            pred = model.predict(test)

            # -1 indicates an anomaly detected by Isolation Forest
            if -1 in pred:
                print("Anomaly Detected! Triggering alert...")
                with open("alert.txt", "w") as f:
                    f.write("ANOMALY")
    except FileNotFoundError:
        pass
        
    time.sleep(5)
