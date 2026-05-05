import random
import time

log_file = "logs.txt"

while True:
    # 25% chance of generating an ERROR, 75% chance of INFO
    status = random.choice(["INFO", "INFO", "INFO", "ERROR"])
    msg = random.choice([
        "User login",
        "Request processed",
        "Database query",
        "Timeout error",
        "Server overload"
    ])

    with open(log_file, "a") as f:
        f.write(f"{status}: {msg}\n")

    print(status, msg)
    time.sleep(2)
