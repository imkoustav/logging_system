# Logging System with Redis Pub/Sub

## Overview

This system provides:

- A log ingestion service (API) to receive logs.
- A log processing service that listens to Redis and writes logs to a file.
- A log retrieval service that fetches logs and provides metrics.

## Setup

### 1️⃣ Start the system

```sh
docker-compose up --build


```
