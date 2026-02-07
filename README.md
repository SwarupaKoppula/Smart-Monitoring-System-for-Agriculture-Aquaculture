# IoT-Based Smart Monitoring System for Agriculture & Aquaculture
## Project Overview

This project implements an end-to-end IoT monitoring system for agricultural and aquaculture environments, designed to acquire, transmit, process, and analyze environmental parameters in real time. The system enables automated decision support by generating alerts when monitored parameters exceed predefined operational thresholds.

Target parameters include soil moisture and temperature for agricultural use cases, and water pH and dissolved oxygen (DO) for aquaculture systems.

## System Architecture

The system follows a layered IoT edge–cloud architecture:

Sensor Layer → Edge/Gateway Layer → Cloud Layer → Application Layer


Sensor Layer: Acquires environmental data using analog and digital sensors

Edge/Gateway Layer: Performs sensor interfacing, data preprocessing, and network communication

Cloud Layer: Handles data ingestion, storage, analytics, and rule-based alert evaluation

Application Layer: Provides data visualization and alert status via a dashboard

## Sensor Interface and Selection

The system integrates industry-standard sensors selected based on accuracy, response time, and compatibility with embedded platforms:

Soil Moisture Sensor – capacitive/analog sensor for soil water content measurement

Temperature Sensor (DHT11/DHT22) – digital sensor for ambient temperature monitoring

pH Sensor – electrochemical probe for water acidity measurement

Dissolved Oxygen Sensor – electrochemical/optical sensor for oxygen concentration

Sensor data is sampled at configurable intervals and converted into engineering units at the edge.

## Data Flow and Communication

Sensors generate raw analog/digital signals

The gateway device (ESP32 / Arduino / Raspberry Pi) reads sensor data via GPIO/ADC

Data is formatted into structured payloads (JSON)

Payloads are transmitted to the cloud using MQTT or HTTP over Wi-Fi

Cloud services ingest, store, and analyze incoming data streams

## Alert Logic and Processing

Threshold-based rule engines are implemented to detect abnormal operating conditions:

Agriculture: Soil moisture below threshold → irrigation alert

Aquaculture: DO below safe limit or pH outside acceptable range → aeration alert

Critical alerts can be evaluated at the edge layer to minimize latency, while the cloud layer supports historical analysis, logging, and user notifications.

## Sample Data Payload
'''json
{
  "temperature": 28.9,
  "soil_moisture": 41,
  "pH": 7.2,
  "dissolved_oxygen": 5.6,
  "alert_flag": true,
  "alert_type": "Aeration"
}

## Monitoring and Visualization

The cloud-hosted dashboard provides:

Real-time sensor telemetry

Threshold breach indicators

Historical trend analysis

System status monitoring

## Conclusion

This project demonstrates a scalable and deployable IoT monitoring architecture, integrating embedded systems, network communication, cloud analytics, and alert-driven automation. The design reflects real-world constraints and industry-standard practices suitable for smart agriculture and aquaculture applications.
