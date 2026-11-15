# Configuration notes

This document describes the exported tested configuration, not universal recommended defaults.

## Boot and firmware

- OpenCore 1.0.8 RELEASE, built-in boot picker, 15-second timeout.
- SecureBootModel: `Disabled`; SIP data: `00000000` (enabled in the observed session).
- `ScanPolicy = 0`; APFS Jumpstart enabled, MinDate/MinVersion `-1`, HideVerbose `true`.
- `Target = 0`, `AppleDebug = false`, `SysReport = false`; no OpenCore file/console debugging.
- `LauncherOption = Disabled`; the repository does not install or change a firmware boot entry.
- Boot arguments: `-v keepsyms=1 debug=0x144 alcid=1 npci=0x2000 -no_compat_check`.

Some arguments and firmware workarounds were inherited from the booting source and have not been independently justified or minimized. No claim is made that `npci=0x2000`, the debug flags or compatibility override are required for all identical boards.

## Memory and kernel quirks

The working EFI retains `AvoidRuntimeDefrag = true`, `EnableWriteUnprotector = true`, `SetupVirtualMap = true`, `EnableSafeModeSlide = true`, `ProvideCustomSlide = true`, `FixupAppleEfiImages = true` and `AllowRelocationBlock = false`. `RebuildAppleMemoryMap` and `SyncRuntimePermissions` are false. These choices must be reviewed for another firmware.

`DisableIoMapper = true`, `AppleCpuPmCfgLock = true`, `AppleXcpmCfgLock = true`, `DisableRtcChecksum = true`, `DisableLinkeditJettison = true` and `PowerTimeoutKernelPanic = true` are enabled. `XhciPortLimit` is false. No proper board-specific USB port map is bundled; do not copy a USBPorts map from a B460 or HP laptop reference.

## ACPI and EFI drivers

| File | Enabled |
| --- | --- |
| SSDT-EC-USBX-DESKTOP.aml | Yes |
| SSDT-PLUG-DRTNIA.aml | Yes |
| SSDT-AWAC.aml | No |
| SSDT-PMC.aml | No |
| OpenRuntime.efi | Yes |
| OpenHfsPlus.efi | Yes |
| Tools/OpenShell.efi | Included; inspect Misc/Tools for picker configuration |

The existing ACPI binaries are included without claiming that they were regenerated from the present BIOS. Source/provenance for those exact compiled files was not independently established.

## Wireless

All four wireless entries have `MinKernel = 25.0.0`, `MaxKernel = 25.99.99` and `Arch = x86_64`. Lilu is loaded before its Bluetooth plugins. AirportItlwm has no competing enabled itlwm entry.

Under Apple NVRAM GUID `7C436110-AB2A-4BBB-A880-FE41995C9F82`:

| Key | Type | Data |
| --- | --- | --- |
| bluetoothExternalDongleFailed | Data | `00` |
| bluetoothInternalControllerInfo | Data | `0000000000000000000000000000` (14 zero bytes) |

Both names also appear in NVRAM/Delete, so an existing value cannot prevent the new data from being applied. This is a targeted replacement of two variables.

AirportItlwm `2.4.0_7204c69` is a development/alpha build with Tahoe-specific ABI support. In the observed session, firmware `68.01d30b0c.0`, country `DE`, modes a/b/g/n/ac and Wi-Fi connected status were reported. The fork documents Wi-Fi 6/HE as opt-in, and no WPA3-only/mandatory-PMF, AWDL/AirDrop or MLO support. No HE-enabling boot argument was added.

Bluetooth firmware v8641 c8641 and USB transport were observed. `THIRD_PARTY_DONGLE` is a software classification and does not mean a separate USB dongle is installed. Discovery and one S21 pairing were confirmed; reconnect, audio and long-term reliability remain open.

## Privacy changes

The public identity was sanitized: empty `SystemSerialNumber`/`MLB`, all-zero SystemUUID and six zero ROM bytes. The disabled, codeless XHCI-unsupported entry's stale `ExecutablePath` was cleared because that bundle has no executable. Its enabled state remains false. The local working EFI was not modified by this export. The marker text file and AppleDouble files are omitted. Raw system reports, historical logs/configs and recovery images are outside the exported EFI.
