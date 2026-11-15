#!/usr/bin/env python3
"""Validate this public EFI template without changing it (Python 3 stdlib)."""
from pathlib import Path
import plistlib
import sys

ROOT = Path(__file__).resolve().parents[1]
OC = ROOT / 'EFI' / 'OC'
errors = []
with (OC / 'config.plist').open('rb') as handle:
    config = plistlib.load(handle)
generic = config['PlatformInfo']['Generic']
for name in ('SystemSerialNumber', 'MLB'):
    if generic.get(name) != '':
        errors.append(f'Private identity present: {name}')
if generic.get('SystemUUID') != '00000000-0000-0000-0000-000000000000':
    errors.append('Private SystemUUID present')
if generic.get('ROM') != bytes(6):
    errors.append('Private ROM present')
for entry in config['Kernel']['Add']:
    bundle = OC / 'Kexts' / entry['BundlePath']
    for field in ('PlistPath', 'ExecutablePath'):
        if entry[field] and not (bundle / entry[field]).is_file():
            errors.append(f'Missing {bundle.name}/{entry[field]}')
    if not bundle.is_dir():
        errors.append(f'Missing Kext: {bundle.name}')
for entry in config['ACPI']['Add']:
    if not (OC / 'ACPI' / entry['Path']).is_file():
        errors.append(f'Missing ACPI: {entry["Path"]}')
for entry in config['UEFI']['Drivers']:
    if not (OC / 'Drivers' / entry['Path']).is_file():
        errors.append(f'Missing EFI driver: {entry["Path"]}')
for required in (ROOT / 'EFI/BOOT/BOOTx64.efi', OC / 'OpenCore.efi'):
    if not required.is_file():
        errors.append(f'Missing boot file: {required.name}')
nvram = config['NVRAM']['Add']['7C436110-AB2A-4BBB-A880-FE41995C9F82']
for key, expected in [('bluetoothExternalDongleFailed', bytes(1)),
                      ('bluetoothInternalControllerInfo', bytes(14))]:
    if nvram.get(key) != expected:
        errors.append(f'Incorrect Bluetooth NVRAM data: {key}')
for path in ROOT.rglob('*'):
    if '.git' in path.parts or not path.is_file():
        continue
    if path.name.startswith('._') or path.suffix in ('.ips', '.dmg', '.pkg', '.log'):
        errors.append(f'Unexpected private/generated file: {path.relative_to(ROOT)}')
    if path.name.startswith('opencore-') or 'SysReport' in path.parts:
        errors.append(f'Unexpected diagnostic dump: {path.relative_to(ROOT)}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Public template OK: {len(config["Kernel"]["Add"])} Kext entries; identities sanitized; references and Bluetooth data valid.')
print('Also run OpenCore 1.0.8 ocvalidate. Passing these checks is not a boot or hardware test.')
