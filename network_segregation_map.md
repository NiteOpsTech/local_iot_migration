# 🌐 NiteOpsTech Home Laboratory: IoT Network Segregation Layout

## 🏗️ VLAN Architecture Topology
To enforce an absolute zero-trust framework, network assets are divided into strict virtual broadcast domains managed via an upstream firewall.

| VLAN ID | Subnet Mask | Classification | Security Target State |
| :--- | :--- | :--- | :--- |
| **VLAN 10** | `10.10.10.0/24` | Management / Core | Primary workstation (BlackBox), RHEL server instances, and trusted engineering platforms. |
| **VLAN 20** | `10.10.20.0/24` | Trusted LAN | Primary consumer mobile devices, computing endpoints, and media units. |
| **VLAN 30** | `10.10.30.0/24` | Isolated IoT Mesh | Smarthome devices, Blink integration points, and localized video substreams. |

---

## 🛡️ Stateful Ingress/Egress Firewall Intercept Matrix

1. **Rule Block 01 (IoT-to-Core Drops):** Explicitly DROP all traffic originating from **VLAN 30 (IoT)** targeting **VLAN 10 (Management)** or **VLAN 20 (LAN)**. 
2. **Rule Block 02 (Cross-VLAN Management):** ALLOW traffic originating from **VLAN 10** to establish stateful connections into **VLAN 30** (enabling your workstation to manage the cameras local endpoints).
3. **Rule Block 03 (WAN Restrictions):** DENY all outbound external internet routes for local video processing hubs once stream ingestion keys are mapped to the **Scrypted** local engine.