# NiteOpsTech Home Lab: IoT Network Segregation Layout

This document models a defensive home-lab segmentation plan for local IoT
devices. The inventory uses synthetic lab identifiers and RFC1918 addresses.

## VLAN Architecture

| VLAN ID | CIDR | Classification | Security Target State |
| :--- | :--- | :--- | :--- |
| VLAN 10 | `10.10.10.0/24` | Management / Core | Primary workstation, RHEL lab host, administrative tooling. |
| VLAN 20 | `10.10.20.0/24` | Trusted LAN | Personal endpoints, media systems, normal user devices. |
| VLAN 30 | `10.10.30.0/24` | Isolated IoT Mesh | Cameras, smart hubs, local streaming endpoints, Scrypted integration. |

## Firewall Intent

1. **IoT-to-Core Drops**
   - Deny traffic from VLAN 30 to VLAN 10.
   - Deny traffic from VLAN 30 to VLAN 20.

2. **Controlled Management**
   - Allow stateful management from VLAN 10 to approved VLAN 30 endpoints.
   - Log management flows for review.

3. **WAN Restrictions**
   - Restrict IoT egress after local ingestion is validated.
   - Prefer explicit allowlists over broad outbound access.

4. **Telemetry**
   - Export firewall events to the NanoMesh ETL chain.
   - Preserve source VLAN, source IP, destination IP, destination port, and action.

## NanoMesh Role

This repo is Level 6 in the NanoMesh support chain:

```text
asset inventory
-> VLAN segmentation map
-> firewall event expectations
-> ETL/detection/SOAR validation
```

## Safety Boundary

- This is a planning and validation repo.
- It does not configure a live router or firewall.
- It does not contain real credentials.
- It should not contain real public IP addresses, passwords, or production RTSP tokens.
