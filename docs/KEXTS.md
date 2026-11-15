# Kext inventory

All 15 bundles from the working source EFI are included. "Disabled" means the bundle is present but its `Kernel/Add` entry is not enabled. It is not evidence of a successfully tested device.

| Bundle | Version | Enabled | Role / upstream |
| --- | --- | --- | --- |
| Lilu | 1.7.2 | Yes | Patch framework, [acidanthera/Lilu](https://github.com/acidanthera/Lilu) |
| VirtualSMC | 1.3.7 | Yes | SMC emulation, [acidanthera/VirtualSMC](https://github.com/acidanthera/VirtualSMC) |
| SMCProcessor | 1.3.7 | Yes | CPU sensor plugin, same VirtualSMC project |
| SMCSuperIO | 1.3.7 | Yes | Super I/O sensor plugin, same VirtualSMC project |
| WhateverGreen | 1.7.0 | Yes | Graphics fixes, [acidanthera/WhateverGreen](https://github.com/acidanthera/WhateverGreen) |
| AppleALC | 1.9.7 | Yes | Audio codec support, [acidanthera/AppleALC](https://github.com/acidanthera/AppleALC); boot layout `alcid=1` |
| RealtekRTL8111 | 2.5.0 | Yes | Onboard Realtek Ethernet, [Mieze/RTL8111_driver_for_OS_X](https://github.com/Mieze/RTL8111_driver_for_OS_X) |
| AirportItlwm | 2.4.0 | Yes | Tahoe alpha `7204c69`, [laobamac/itlwm](https://github.com/laobamac/itlwm/releases/tag/v2.4.0-alpha) |
| IntelBluetoothFirmware | 2.5.3 | Yes | AX200 USB firmware uploader, [lshbluesky fork](https://github.com/lshbluesky/IntelBluetoothFirmware/releases/tag/v2.5.3) |
| IntelBTPatcher | 2.5.3 | Yes | Intel Bluetooth compatibility fixes, same lshbluesky release |
| BlueToolFixup | 2.7.2 | Yes | macOS Bluetooth userspace fixes, [acidanthera/BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM/releases/tag/2.7.2) |
| IntelMausi | 1.0.8 | No | Alternate Intel Ethernet driver, [acidanthera/IntelMausi](https://github.com/acidanthera/IntelMausi); not the onboard Realtek driver |
| NVMeFix | 1.1.3 | No | NVMe fixes, [acidanthera/NVMeFix](https://github.com/acidanthera/NVMeFix); reference storage is SATA |
| RestrictEvents | 1.1.6 | No | Platform workarounds, [acidanthera/RestrictEvents](https://github.com/acidanthera/RestrictEvents) |
| XHCI-unsupported | 0.9.2 | No | Legacy USB controller injector, associated with [RehabMan/OS-X-USB-Inject-All](https://github.com/RehabMan/OS-X-USB-Inject-All); exact original binary provenance not independently established |

The four wireless entries are limited to Darwin `25.0.0–25.99.99`. Other entries retain the source EFI's version constraints. Lilu precedes dependent plugins. These are the installed versions, not a claim that every component is the newest available.

## Release provenance

The OpenCore executable, fallback loader and OpenRuntime were copied from `OpenCore-1.0.8-RELEASE.zip`. OpenHfsPlus and OpenShell were retained from the original EFI; they were not independently rebuilt or replaced during quiet-boot tuning.

The wireless additions were downloaded from these release asset filenames:

- `AirportItlwm-Tahoe-v2.4.0-RELEASE-alpha-7204c69.zip`
- `IntelBluetooth-2.5.3-RELEASE.zip`
- `BrcmPatchRAM-2.7.2-RELEASE.zip` (only BlueToolFixup selected)

Other Kexts and ACPI files were inherited from the already-booting EFI. Bundle versions were read directly from `Contents/Info.plist`; no claim is made that inherited binaries match an independently rebuilt source tree. Exact public file hashes are recorded in `SHA256SUMS`.

## Troubleshooting

```sh
sudo kmutil showloaded | grep -Ei 'itlwm|IntelBluetooth|IntelBTPatcher|BlueTool|Lilu'
system_profiler SPAirPortDataType SPBluetoothDataType
ioreg -r -c IntelBluetoothFirmware -l -w0
```

The successful observed session loaded AirportItlwm 2.4.0, IntelBluetoothFirmware/IntelBTPatcher 2.5.3 and BlueToolFixup 2.7.2. Wi-Fi was connected. Bluetooth reported USB transport and firmware v8641 c8641. A later daemon failure remains documented in the README; loading alone does not demonstrate reliable pairing.
