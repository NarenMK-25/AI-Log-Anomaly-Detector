# 🛡️ AI-Based Log Anomaly Detection and Auto-Healing System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Machine Learning](https://img.shields.io/badge/ML-Isolation%20Forest-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

## 📖 Project Overview
This project presents an intelligent, self-sustaining system deployed on AWS EC2 that utilizes Machine Learning to monitor system logs and automatically recover from failures. 

By shifting away from traditional manual monitoring, this system learns normal behavior, automatically detects unusual patterns (anomalies) using an **Isolation Forest** algorithm, and executes self-healing actions (restarting Docker containers) without human intervention.

## ✨ Key Features
*   **Real-Time Monitoring:** Replaces manual log checking with an intelligent, continuous monitoring script.
*   **Unsupervised Anomaly Detection:** Utilizes scikit-learn's Isolation Forest to identify anomalies without the need for extensively labeled datasets.
*   **Autonomous Recovery:** An auto-healing bash script instantly restarts failing Docker services to minimize system downtime.
*   **Live Dashboard:** A lightweight Streamlit UI to visualize system health, live logs, and active alerts.
*   **Cloud & Container Ready:** Designed to run seamlessly on an Ubuntu AWS EC2 instance using Docker.

## 🏗️ System Architecture Workflow
`Log Generation` ➔ `Data Preprocessing` ➔ `ML Model Evaluation` ➔ `Anomaly Detection` ➔ `Alert Triggered` ➔ `Auto-Healing Script` ➔ `System Recovery`

---

## 📂 Project Structure
```text
AI-Log-Anomaly-Detector/
├── ai_model.py         # The Isolation Forest ML model for anomaly detection
├── app.py              # Streamlit web dashboard for live monitoring
├── heal.sh             # Bash script for auto-healing Docker containers
├── log_generator.py    # Script to simulate system logs (INFO/ERROR)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation



🚀 Installation & Setup Guide
1. Cloud Environment Setup (AWS EC2)
Launch an Ubuntu instance on AWS EC2 and configure the Security Group with the following Inbound Rules:

Port 22 (SSH): For remote terminal access.

Port 80 (HTTP): For the web application running in Docker.

Port 8501 (Custom TCP): For the Streamlit UI.

2. Clone the Repository
SSH into your EC2 instance and clone this repository:

Bash
git clone [https://github.com/NarenMK-25/AI-Log-Anomaly-Detector.git](https://github.com/NarenMK-25/AI-Log-Anomaly-Detector.git)
cd AI-Log-Anomaly-Detector
(Note: Don't forget to replace YourUsername with your actual GitHub username!)

3. Install System Dependencies & Docker
Update your system and install Docker and Python virtual environment tools:

Bash
sudo apt update
sudo apt install docker.io python3 python3-venv python3-pip -y
sudo systemctl start docker
sudo systemctl enable docker
4. Setup Python Environment
Create and activate an isolated Python environment, then install the dependencies:

Bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
5. Deploy the Target Application
Run a sample Nginx web server using Docker. This is the application our system will monitor and auto-heal.

Bash
sudo docker run -d --name webapp -p 80:80 nginx
💻 Usage Instructions
To run the full system, you will need to open multiple terminal sessions (or use tmux/screen) to run the following components simultaneously:

1. Start the Log Generator:
Simulates incoming system logs.

Bash
python log_generator.py
2. Start the AI Model:
Analyzes the logs.txt file in real-time.

Bash
python ai_model.py
3. Start the Auto-Healing Script:
Monitors for alerts and restarts Docker if needed.

Bash
chmod +x heal.sh
while true; do ./heal.sh; sleep 5; done
4. Launch the Streamlit Dashboard:
View the live status of your system.

Bash
streamlit run app.py --server.address 0.0.0.0
Access the dashboard in your web browser at: http://YOUR-EC2-PUBLIC-IP:8501

🧪 Testing the Auto-Healing
To verify the system works:

Open log_generator.py.

Change the log generation probability to force errors: modify ["INFO", "INFO", "INFO", "ERROR"] to ["ERROR", "ERROR", "ERROR"].

Save and restart log_generator.py.

Watch the magic: The AI model will detect the anomaly, generate alert.txt, the healing script will automatically restart the Nginx Docker container, and the Streamlit UI will reflect the recovery!

🔮 Future Enhancements
Integrate Deep Learning models (LSTMs) for complex sequence prediction.

Connect to real-world system logs (e.g., actual Nginx or AWS CloudWatch logs).

Add multi-channel alert notifications via AWS SNS (Email/SMS).
