# AQUAGUARD – IoT Smart Monitoring System for Agriculture & Aquaculture

This project focuses on designing an IoT-based smart monitoring solution for agricultural fields and aquaculture ponds. The system continuously monitors soil and water parameters and provides timely alerts to support efficient irrigation and aeration management.

## System Overview

The system uses multiple sensors deployed in agriculture or aquaculture environments to collect real-time data. An ESP32 edge device acquires sensor readings, performs basic validation, and forwards the data to a cloud platform through a WiFi gateway. The cloud layer stores the data, visualizes trends, and executes alert rules.

## Data Flow

Sensors → ESP32 (Edge Node) → WiFi Gateway → Cloud Server → Monitoring Dashboard → Alert Notifications

This flow ensures reliable communication between physical sensors and cloud-based applications.

## Sensors Used
### Agriculture Monitoring

Soil Moisture Sensor – Measures soil water content to optimize irrigation

Temperature Sensor – Monitors ambient conditions affecting crop growth

### Aquaculture Monitoring

pH Sensor – Tracks water acidity levels for aquatic safety

Dissolved Oxygen Sensor – Ensures sufficient oxygen levels in ponds

Each sensor is selected to directly support critical decision-making.

## Features

Continuous monitoring of soil and water parameters

Edge-to-cloud data transmission using IoT architecture

Real-time dashboard visualization

Threshold-based alert mechanism

Scalable and practical system design

## Alert Logic

### Agriculture:
When soil moisture falls below a predefined limit, an irrigation alert is generated.

### Aquaculture:
When pH or dissolved oxygen values exceed safe limits, an aeration alert is generated.

Alert conditions can be evaluated at both edge and cloud levels.

## Conclusion

The AQUAGUARD system demonstrates a practical implementation of an IoT-based smart monitoring system. It satisfies the requirements of sensor selection, data flow, alert logic, and edge–cloud integration, making it suitable for real-world agriculture and aquaculture applications.
