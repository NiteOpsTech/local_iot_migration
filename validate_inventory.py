import ipaddress
import json
import re
from pathlib import Path


MAC_PATTERN = re.compile(r"^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$")
EXPECTED_VLANS = {10, 20, 30}


def load_inventory(path="iot_asset_inventory.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_asset(asset):
    required_top_level = {
        "asset_id",
        "device_type",
        "vendor",
        "model",
        "mac_address",
        "network_configuration",
        "integration_telemetry",
    }
    missing = required_top_level - set(asset)
    if missing:
        raise ValueError(f"{asset.get('asset_id', 'unknown')} missing fields: {sorted(missing)}")

    if not MAC_PATTERN.match(asset["mac_address"]):
        raise ValueError(f"{asset['asset_id']} has invalid MAC address format")

    network = asset["network_configuration"]
    vlan = network["assigned_vlan"]
    if vlan not in EXPECTED_VLANS:
        raise ValueError(f"{asset['asset_id']} uses unexpected VLAN {vlan}")

    ipaddress.ip_address(network["ip_address"])

    telemetry = asset["integration_telemetry"]
    if not telemetry.get("target_platform"):
        raise ValueError(f"{asset['asset_id']} missing target platform")


def validate_inventory(path="iot_asset_inventory.json"):
    inventory = load_inventory(path)
    assets = inventory.get("network_assets", [])
    if not assets:
        raise ValueError("inventory contains no network assets")

    seen_ids = set()
    for asset in assets:
        asset_id = asset["asset_id"]
        if asset_id in seen_ids:
            raise ValueError(f"duplicate asset_id: {asset_id}")
        seen_ids.add(asset_id)
        validate_asset(asset)

    return len(assets)


if __name__ == "__main__":
    count = validate_inventory()
    print(f"[OK]: inventory validated ({count} assets)")
