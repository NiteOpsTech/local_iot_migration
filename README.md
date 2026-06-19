# Local IoT Migration

Defensive home-lab planning repo for migrating IoT devices into a segmented,
local-first architecture.

## Purpose

This project models how cameras, hubs, and local streaming services can be
tracked as structured inventory and mapped into isolated network zones.

The repo is intentionally documentation and validation focused. It does not
configure a live router, firewall, or IoT platform.

## Contents

- `iot_asset_inventory.json`: synthetic IoT asset inventory
- `network_segregation_map.md`: VLAN and firewall intent map
- `validate_inventory.py`: inventory validation script
- `test_validate_inventory.py`: unit tests

## Run Validation

```bash
python validate_inventory.py
python -m unittest discover
```

## NanoMesh Role

This is Level 6 in the NanoMesh support chain:

```text
local assets
-> segmentation map
-> expected firewall events
-> ETL/detection/SOAR validation
```

## Safety Boundary

- Uses synthetic lab identifiers.
- No credentials.
- No production RTSP tokens.
- No router/firewall changes.
- No third-party network testing.
