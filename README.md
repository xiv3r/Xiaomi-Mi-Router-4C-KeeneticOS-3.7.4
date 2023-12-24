# Xiaomi Router 4C Keenetic 3.7.4 Firmware with USB-mod support

Install Keenetic on Xiaomi 4C Router | SPI_NOR GigaDevice GD25Q128*

Note: If you have a router without USB, then you can install it too.

Note: Tested on R4C with firmware 2.14.128 and 3.0.23.

## Installations:

 0. Download the archive with scripts, unpack. There are many files in the folder, we are only interested in `!Start.bat`
 1. `Reset` the router settings, go through the initial setup and set a password (for further convenience, put `12345678`
 2. Disconnect everything unnecessary from the router and from the PC, and also turn off WiFi on the PC.
 3. Run `!Start.bat` select item `11`  Follow the instructions on the window.
 4. Run `22` , a backup of your firmware will be created in the data folder. Keep it in a safe place.
 5. Run `55` - to install Keenetic. In ~5 minutes the firmware will be installed, you can log into the router:`192.168.1.1`

# FEATURES

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

  7. Media Server
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
   1. 3 WAN Ethernet 3 LAN Ethernet (custom settings)
   2. LTE/4G/3G/2G USB modem
   3. File Servers
  
</details>
