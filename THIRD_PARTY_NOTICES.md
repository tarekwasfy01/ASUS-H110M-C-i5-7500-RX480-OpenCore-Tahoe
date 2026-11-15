# Third-party notices

The repository's MIT license does not apply to third-party EFI files. Preserve all upstream notices when redistributing. Source links below identify the projects and release lineage; inherited binary provenance is explicitly described in `docs/KEXTS.md`.

| Components | Upstream source | License notice |
| --- | --- | --- |
| OpenCore, BOOTx64, OpenRuntime, OpenHfsPlus, OpenShell | [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg), version 1.0.8 for replaced boot binaries | `licenses/OpenCore.txt`; OpenCorePkg contains additional contributor/component notices |
| Lilu | [Lilu](https://github.com/acidanthera/Lilu) | `licenses/Lilu.txt` |
| VirtualSMC, SMCProcessor, SMCSuperIO | [VirtualSMC](https://github.com/acidanthera/VirtualSMC) | `licenses/VirtualSMC.txt` |
| WhateverGreen | [WhateverGreen](https://github.com/acidanthera/WhateverGreen) | `licenses/WhateverGreen.txt` |
| AppleALC | [AppleALC](https://github.com/acidanthera/AppleALC) | `licenses/AppleALC.txt`; upstream codec/resource notices also apply |
| IntelMausi | [IntelMausi](https://github.com/acidanthera/IntelMausi) | `licenses/IntelMausi.txt` |
| NVMeFix | [NVMeFix](https://github.com/acidanthera/NVMeFix) | `licenses/NVMeFix.txt` |
| RestrictEvents | [RestrictEvents](https://github.com/acidanthera/RestrictEvents) | `licenses/RestrictEvents.txt` |
| AirportItlwm | [laobamac/itlwm](https://github.com/laobamac/itlwm), alpha commit `7204c69`, derived from OpenIntelWireless/OpenBSD | `licenses/AirportItlwm.txt`; per-file BSD and Intel firmware notices in upstream source also apply |
| IntelBluetoothFirmware, IntelBTPatcher | [lshbluesky/IntelBluetoothFirmware](https://github.com/lshbluesky/IntelBluetoothFirmware), v2.5.3 | `licenses/IntelBluetoothFirmware.txt`; Intel firmware redistribution terms are separate from driver code |
| BlueToolFixup | [BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM), 2.7.2 | `licenses/BrcmPatchRAM.txt` |
| RealtekRTL8111 | [Mieze/RTL8111_driver_for_OS_X](https://github.com/Mieze/RTL8111_driver_for_OS_X), bundle reports 2.5.0 | See upstream source license/copyright notices |
| XHCI-unsupported | [RehabMan/OS-X-USB-Inject-All](https://github.com/RehabMan/OS-X-USB-Inject-All), inherited bundle reports 0.9.2 | See upstream notices; exact inherited binary origin not independently established |
| SSDT ACPI binaries | Inherited from local working EFI; table names follow common Dortania/OpenCore samples | Exact matching DSL source and authorship were not established; no new ownership or license claim is made |

Upstream repositories contain the source and build instructions. Intel Wi-Fi/Bluetooth firmware embedded in driver binaries remains owned by Intel and retains Intel's redistribution conditions. It is not relicensed by the root MIT license. This repository does not publish an Apple macOS installer, kernel collection, recovery image or Apple system executable.

The included license texts were retrieved from upstream projects during preparation. Read upstream per-file notices and release sources as well; top-level licenses are not an exhaustive account of every embedded dependency.
