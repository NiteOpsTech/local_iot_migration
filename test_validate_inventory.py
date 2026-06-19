import json
import tempfile
import unittest
from pathlib import Path

from validate_inventory import validate_inventory


class TestValidateInventory(unittest.TestCase):
    def test_repo_inventory_is_valid(self):
        self.assertEqual(validate_inventory(), 3)

    def test_invalid_ip_fails(self):
        payload = {
            "network_assets": [
                {
                    "asset_id": "IOT-BAD-01",
                    "device_type": "Camera",
                    "vendor": "Lab",
                    "model": "Sim",
                    "mac_address": "02:00:00:00:30:99",
                    "network_configuration": {
                        "assigned_vlan": 30,
                        "ip_address": "999.999.999.999",
                        "assignment_type": "DHCP Reservation",
                    },
                    "integration_telemetry": {
                        "target_platform": "Scrypted",
                        "ingestion_method": "RTSP Substream",
                        "local_stream_url": "N/A",
                        "cloud_status": "restricted",
                    },
                }
            ]
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "inventory.json"
            path.write_text(json.dumps(payload), encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_inventory(path)


if __name__ == "__main__":
    unittest.main()
