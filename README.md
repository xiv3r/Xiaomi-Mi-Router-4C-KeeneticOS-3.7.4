# KeeneticOS 3.7.4 with USB-mod support for Xiaomi 4C Router

<img align="center" width="800" height="600" src="https://github.com/xiv3r/Xiaomi-Mi-Router-4A-Gigabit-KeeneticOS-3.7.4/blob/main/firmwares/Screenshot_2023_1227_121024.png">


Note: SPI_NOR must be GigaDevice GD25Q128B | WINBOND W25Q128 | CFEON EN25QX128A

Note: If you have a router without USB, then you can install it too.

Note: Tested on R4C with firmware 2.14.128 and 3.0.23.

## Installations:

 1. [Download Here!!!](https://codeload.github.com/xiv3r/Xiaomi-Router-4C-Keenetic-v3.7.4-Firmware/zip/refs/heads/main)   the archive with scripts and unpack it. There are many files in the folder, we are only interested in `!Start.bat`.

 2. First `Reset` the router then reconfigure it again with a password of `12345678`.
 
 3. Connect your router to the PC.

 4. Run `!Start.bat` select item `11`  Follow the instructions on the window. place the password `12345678`

 5. Run `22` , a backup of your firmware will be created in the `/data` folder.

 6. Run `55` - to install Keenetic. wait 5-10 minutes then the firmware will be installed
 
 7. Go to [http://192.168.1.1](http://192.168.1.1)

## FEATURES

<details><summary>Overview</summary>

 ## Wi-Fi interface
Provides the core wireless functionality. This component will be installed automatically if needed.

- USB interface
Allows to use the USB host port on this device.

- Network accelerator engine
Improves routing performance.

- DHCP server
Allows a computer to be configured automatically when connected to this device. Install this component if unsure.

- IGMP/PPPoE proxy service
The IGMP/PPPoE proxy relays IGMP/PPPoE traffic between network segments.

- UPnP service
Allows the NAT and firewall rules on this device to be configured automatically.

- SSH server
Allows to gain secure access to the device's command line.

- Wi-Fi system controller
Centralized Mesh Wi-Fi System management.

## System operating mode
- Repeater/Extender mode
For expanding the wireless network of another Keenetic.

## Internet safety

- Yandex.DNS
Safe Internet browsing.

- SkyDNS
Safe Internet browsing.

- AdGuard DNS
Safe Internet browsing.

- Cloudflare DNS
Safe Internet browsing.

## Network functions

- PPPoE client
Allows to establish PPPoE connections from this device.

- PPTP client
Allows to establish PPTP connections from this device.

- L2TP client
Allows to establish L2TP connections from this device.

- 802.1X client
Provides a login/password based authentication support over Ethernet networks.

- Application-layer gateway (ALG) for FTP
Provides customized NAT traversal filters to support address and port translation for FTP protocol.

- Application-layer gateway (ALG) for PPTP/GRE
Provides customized NAT traversal filters to support address and port translation for PPTP/GRE protocols.

- Application-layer gateway (ALG) for RTSP
Provides customized NAT traversal filters to support address and port translation for RTSP protocol.

- Application-layer gateway (ALG) for SIP
Provides customized NAT traversal filters to support address and port translation for SIP protocol.

- Application-layer gateway (ALG) for H.323
Provides customized NAT traversal filters to support address and port translation for H.323 protocol.

 ## Utilities and services

- Internet connection status monitoring (Ping Check)
Performs icmp- and tcp-based tests to verify the Internet connection status. Test results may be used to switch between primary and backup connections.

- Traffic shaper
Provides basic network bandwidth limitation functionality.

- Dynamic DNS (DDNS) client
Keeps track of dynamic public IP address on this appliance, and maps it to a static domain name when changed.

- DNS-over-TLS proxy
Provides domain names resolution via secure DNS-over-TLS protocol.

- DNS-over-HTTPS proxy
Provides domain names resolution via secure DNS-over-HTTPS protocol.

 ## USB modems and extension modules

- Serial interface for 4G/3G USB modems
Enables 4G/3G network connection via a USB modem with a serial interface.

- CDC Ethernet interface for 4G/3G USB modems
Enables 4G/3G network connection via a USB modem of the CDC Ethernet type.

- NDIS interface for 4G/3G USB modems
Enables 4G/3G network connection via a USB modem with an NDIS interface.

- QMI interface for 4G/3G USB modems
Enables 4G/3G network connection via an external - or internal (on select Keenetic models) - USB modem that supports the QMI protocol.

 ## USB drives

- USB storage support
Allows a USB drive to be connected to this device.

- NTFS filesystem
Allows a NTFS-formatted USB drive to be connected to this device.

- FAT32 filesystem
Allows a FAT32-formatted USB drive to be connected to this device.

- HFS+ filesystem
Allows an HFS+-formatted USB drive to be connected to this device.

- exFAT filesystem
Allows an exFAT-formatted USB drive to be connected to this device.

- Ext filesystem
Allows an Ext-formatted USB drive to be connected to this device.

- SMB file and printer sharing
Allows sharing of USB drives and printers with Windows/Apple/Linux computers and other networked devices.

## Media Server
Allows this device to stream content stored on a USB drive to networked digital media players.

- FTP server
Allows file sharing via the FTP protocol.

- SFTP server
Allows secure file sharing via the SFTP protocol.

- Folder permissions control
Allows to specify individual user rights for folders on a USB drive.

## Support

-  Multiple WAN with failover

   0. Wireless Wan
   1. LTE/4G/3G USB WAN
   2. 3 Ethernet WAN 3 Ethernet LAN Ethernet (custom settings)
   3. MultiWAN with failover
   4. File Server
   5. Custom Mac address through breed
  
</details>

👉 [RECOVERY](https://github.com/xiv3r/Xiaomi-Mi-Router-4C-CH341A-Flasher)
