# 🚀 Logging System

## 📌 Overview
The **Logging System** is a scalable and efficient log management solution that provides structured logging, log rotation, system logging, and advanced retrieval capabilities. It ensures smooth log collection, processing, and access through RESTful APIs, making it ideal for monitoring and debugging large-scale applications.

## 🔥 Features

### ✅ Log Ingestion
- Collects logs from multiple sources.
- Uses **Redis** as a message broker for efficient queuing.

### ✅ Log Processing
- Formats and stores logs systematically.
- Implements **log rotation** using `RotatingFileHandler` to manage file sizes.
- Supports **system logging (Syslog)** via `SysLogHandler`.

### ✅ Log Retrieval APIs
| Endpoint        | Description                                      |
|---------------|------------------------------------------------|
| `GET /logs/recent` | Fetches the most recent logs (`tail`). |
| `GET /logs/search?q=<query>` | Searches logs by keyword (`grep`). |
| `GET /logs/filter?level=<level>` | Filters system logs (`journalctl`). |

## 🛠️ Tech Stack
- **Backend:** Python (`logging`, `Flask`)
- **Queue Management:** Redis
- **Containerization:** Docker, Docker Compose
- **Deployment:** Render, Neon.tech (PostgreSQL)

## 🚀 Deployment & Infrastructure
- Runs inside **Docker containers** orchestrated via **Docker Compose**.
- Uses **Neon.tech PostgreSQL** for structured log storage.
- Can be deployed on **Render** or similar cloud platforms.

## ⚡ Challenges & Solutions
- **Efficient Log Storage:** Implemented **log rotation** to manage disk space.
- **High Availability:** Used **Redis queues** to handle large log volumes.
- **Fast Log Retrieval:** Optimized APIs using native system utilities (`tail`, `grep`, `journalctl`).

## 🔮 Future Enhancements
- Implement **structured JSON logging** for better analytics.
- Add **real-time log streaming** via WebSockets or Kafka.
- Integrate with **Elasticsearch + Kibana** for advanced log visualization.

## 📜 License
This project is open-source under the **MIT License**.

---

💡 **Contributions & Feedback are welcome!**
