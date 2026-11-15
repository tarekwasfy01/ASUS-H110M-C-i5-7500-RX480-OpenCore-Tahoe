# ASUS H110M-C — macOS Tahoe, RX 480 and Intel AX200

Working desktop reference for an **ASUS H110M-C / Core i5-7500 / Radeon RX 480 8 GB**, updated **15 November 2026**.

The owner confirmed **macOS startup, native-menu Wi-Fi and the desired quiet OpenCore startup**. Bluetooth discovery and Samsung Galaxy S21 pairing work, but pairing required repeated attempts and `bluetoothd` crashed during an earlier attempt. **Bluetooth stability is not established.**

**Generate your own SMBIOS identity before booting.** This is a sanitized hardware-specific reference, not a universal EFI or macOS installer. No macOS system files, personal serials, raw diagnostic dumps or pairing databases are included.

## Hardware and status

| Component | Reference hardware |
| --- | --- |
| Motherboard | ASUSTeK H110M-C, DMI board revision `Rev X.0x`, Intel H110 platform |
| BIOS | American Megatrends 3403; firmware date string `07/04/2017` |
| CPU | Intel Core i5-7500, Kaby Lake, 4 cores, nominal 3.40 GHz |
| Graphics | AMD Radeon RX 480, 8 GB, PCI `1002:67DF`, revision `C7` |
| Memory | 8 GB DDR4-2133, one Avant `W641GU67J5213N8` module in DIMM_A1 |
| WLAN | Intel AX200, PCI `8086:2723`, subsystem `8086:0084` |
| Bluetooth | Intel AX200 USB `8087:0029`, firmware reported as v8641 c8641 |
| Ethernet | Realtek RTL8168H/8111H, PCI `10EC:8168` |
| SATA controller | Intel 100-series AHCI, macOS reports Intel 10 Series Chipset |
| Storage attached | SanDisk SDSSDA120G 120 GB SSD; WD WDS240G2G0B-00EPW0 240 GB SSD; Toshiba DT01ACA100 1 TB HDD |
| Optical drive | HL-DT-ST DVDRAM GH24NSC0 |
| Audio | AppleALC 1.9.7 with `alcid=1`; physical analog codec not independently identified |
| Software | macOS Tahoe **26.7.3 / 25G342**, Darwin **25.6.0**, OpenCore **1.0.8 RELEASE** |
| SMBIOS | `iMac20,1`, retained from the tested configuration |

The real motherboard/BIOS/CPU were read from a local pre-spoof OpenCore SysReport; no raw SMBIOS dump is published. The SMBIOS identity presented to macOS is not the physical motherboard model. Storage models and RAM part numbers are included; unique device serials are not.

| Feature | Result on this machine |
| --- | --- |
| Desktop startup | Working, owner confirmed |
| OpenCore startup | Quiet startup and acceptable startup time, owner confirmed |
| Graphics | RX 480 identified with 8 GB; Metal support observed |
| Wi-Fi | Working and connected through native macOS Wi-Fi menu, owner confirmed |
| Bluetooth discovery / S21 pairing | Pairing eventually succeeded after multiple attempts |
| Bluetooth reconnect / long-term use / audio | **Not qualified; pairing-triggered daemon crash observed** |
| Ethernet | Realtek driver/interface observed; throughput not qualified |
| Analog audio / microphone | Driver configured; audible playback and capture not qualified |
| Sleep / wake / hibernation | Not qualified |
| AirDrop / Continuity | Not qualified; this AirportItlwm fork documents no AWDL/AirDrop support |
| USB mapping | AX200 USB device, keyboard and mouse observed; no complete board-specific map included |
| SATA TRIM | Reported as disabled on both SSDs; no TRIM enablement performed |

## Included files

- [`EFI/`](EFI): complete current bootloader, configuration, ACPI tables, EFI drivers, tools and all 15 Kext bundles from the working source, including disabled bundles.
- [`docs/KEXTS.md`](docs/KEXTS.md): versions, enabled states, source projects and roles.
- [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md): relevant boot settings, Bluetooth NVRAM values and remaining limits.
- [`tools/validate_public.py`](tools/validate_public.py): public identity, references and configuration checks.
- [`SHA256SUMS`](SHA256SUMS): hashes of the public files.
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`licenses/`](licenses): attribution and available upstream license texts.

The export originated from **MACRECOVERY/EFI**, identified in the boot log as OpenCore's loaded storage handle. The corrected private EFI was subsequently copied to **OC_EFI**, and the copy passed a SHA-256 file comparison and OpenCore 1.0.8 `ocvalidate`. Partition names and disk numbers are local installation details, not required volume names for this EFI.

## Installation

### 1. Preserve a working boot route

Back up the current EFI and important data. Test this reference on a separate FAT32 USB boot device first. Do not erase Windows, Linux or an existing working EFI. This repository does not repartition disks, remove old systems or install macOS.

The motherboard/CPU, firmware memory quirks, ACPI tables and graphics configuration are specific to the reference machine. Another BIOS, board revision or macOS build needs independent validation. This EFI does not document a measured BIOS-settings profile; do not assume unrelated example EFI settings apply.

### 2. Personalize the SMBIOS

Use [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) to generate a consistent **iMac20,1** identity. In a private copy of `EFI/OC/config.plist`, fill `PlatformInfo → Generic → SystemSerialNumber`, `MLB`, `SystemUUID` and the six-byte `ROM`.

The public template intentionally contains empty serial/MLB, a zero UUID and zero ROM. **Never upload your personalized configuration.** The retained model matches the tested setup; it is not a claim that iMac20,1 is the optimal SMBIOS for every Kaby Lake installation.

### 3. Validate and copy

With Python 3 available, check the unchanged public checkout:

```sh
python3 tools/validate_public.py
shasum -a 256 -c SHA256SUMS
```

Validate your personalized configuration with the **ocvalidate bundled with OpenCore 1.0.8**. The public checker intentionally rejects personalized identities; a changed config will also differ from the public checksum.

Copy the complete `EFI` directory to the root of the test boot partition. Preserve `EFI/BOOT/BOOTx64.efi`, `EFI/OC/OpenCore.efi` and the matching `OpenRuntime.efi`. Use the firmware's boot menu to select the test device. No specific boot-menu hotkey has been verified for this board.

### 4. Boot and test wireless

The included AirportItlwm build targets **Darwin 25.x / Tahoe**. Do not use the Sequoia or Monterey build on Tahoe. Do not enable `itlwm.kext` and `AirportItlwm.kext` together. This AirportItlwm setup uses the macOS Wi-Fi menu, not HeliPort.

IntelBluetoothFirmware, IntelBTPatcher and BlueToolFixup are enabled for Darwin 25.x. IntelBluetoothInjector is not included or needed for Tahoe. The two Bluetooth NVRAM data values are configured in both `Add` and `Delete` so their old values are selectively replaced at boot. This does not perform a full NVRAM reset.

After changing Bluetooth firmware, fully shut down and cold-start before testing. Verify Wi-Fi association, Bluetooth discovery and a real connection. A visible Bluetooth toggle is not sufficient proof. Test reconnect and sleep/wake separately before treating Bluetooth as reliable.

## Known Bluetooth issue

Samsung Galaxy S21 pairing succeeded after repeated attempts. Earlier pairing attempts caused `bluetoothd` to exit with `SIGBUS`; its crash report and kernel log recorded an APFS compressed-data hash mismatch/page-in failure in the daemon's executable mapping.

Both system and data APFS volumes passed live `diskutil verifyVolume` checks with exit code 0. All four wireless Kexts were confirmed loaded, and the controller was reported on USB with firmware v8641 c8641. These findings do **not** prove a failed SSD, a damaged on-disk binary, or a specific Kext bug. The cause remains unresolved. A cache purge and daemon restart were used as a troubleshooting step; they are not an established permanent fix.

Keep raw logs private and reproduce the failure before changing drivers. Do not replace Apple system binaries or disable SIP merely because Bluetooth pairing is intermittent. No such system modification is part of this repository.

## Quiet OpenCore startup

The reference uses matching OpenCore 1.0.8 **RELEASE** `BOOTx64.efi`, `OpenCore.efi` and `OpenRuntime.efi`, with:

- `Misc → Debug → Target = 0`, `SysReport = false`, `AppleDebug = false`, `DisplayDelay = 0`.
- `UEFI → APFS → HideVerbose = true`.
- The built-in picker remains visible with a 15-second timeout.
- `ScanPolicy = 0` is retained. Scanning was not restricted to specific drives or filesystems.

The macOS boot argument **`-v` remains enabled**. OpenCore's quiet startup and macOS verbose kernel boot are separate. If desired, remove only `-v` from a private config after establishing a reliable boot route; the distributed config preserves the tested arguments.

## Sources and credits

- [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg) and [Dortania](https://dortania.github.io/OpenCore-Install-Guide/).
- [laobamac/itlwm](https://github.com/laobamac/itlwm): Tahoe-specific AirportItlwm alpha build `7204c69`.
- [lshbluesky/IntelBluetoothFirmware](https://github.com/lshbluesky/IntelBluetoothFirmware/releases/tag/v2.5.3).
- [acidanthera/BrcmPatchRAM](https://github.com/acidanthera/BrcmPatchRAM): BlueToolFixup and Bluetooth NVRAM requirements.
- Individual component sources are listed in the Kext inventory and third-party notices.

## Privacy and licensing

This export omits system serial/MLB/UUID/ROM, personal MAC addresses, disk UUID reports, raw SysReport and boot/crash logs, old configuration backups and local recovery images. ACPI binaries and Kext files are retained as shipped in the tested EFI. Private identity remains in local recovery copies outside this public package.

The root MIT license applies to the original repository documentation and validation tool only. Third-party drivers, bootloader binaries, firmware and ACPI material retain their own licenses. Upstream source links and version information are provided; no ownership of third-party code is claimed. This project is unaffiliated with Apple, ASUS, Intel or AMD.
