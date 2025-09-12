# ESP32 Jammer
<p>The device is a multi-functional jammer designed to disrupt wireless communication across a variety of frequencies, including 2.4GHz broadband, Bluetooth, and remote control (RC) signals. It works by emitting a wide-band noise signal that interferes with the targeted frequency ranges, rendering devices operating on these frequencies ineffective. The jammer is capable of blocking common Wi-Fi networks operating in the 2.4GHz band, Bluetooth connections used for short-range communication, as well as controlling devices like RC cars, drones, and other remote-controlled gadgets. With its compact design, this jammer is highly effective in areas where wireless communication needs to be interrupted or prevented, ensuring that devices relying on these frequencies become inoperable within a radius of 30m.</p>

## Legal Disclaimer:
Please note that the use of jammers is illegal in many countries, including Poland. Jamming wireless communications can interfere with critical systems, including emergency services, and may result in significant legal consequences. Always ensure that you are in compliance with local laws and regulations before considering the use of such devices.

![Jammer2](https://github.com/Electro5218/security-engineering-lab/blob/main/esp32-jammer/assets/Jammer2.JPEG)
![Jammer1](https://github.com/Electro5218/security-engineering-lab/blob/main/esp32-jammer/assets/Jammer1.JPEG)

# Parts

  [Resistors](https://pl.aliexpress.com/item/1005007987815579.html?aff_fcid=1e343476a15f43959b9e5f1eca4ca941-1741732129651-05363-_oBV1Q1Z&tt=CPS_NORMAL&aff_fsk=_oBV1Q1Z&aff_platform=shareComponent-detail&sk=_oBV1Q1Z&aff_trace_key=1e343476a15f43959b9e5f1eca4ca941-1741732129651-05363-_oBV1Q1Z&terminal_id=5bcfda95327e49539b9b6782303a1b72&afSmartRedirect=y) 4.7k Ohm<br />
  [Status Led: 3 mm LED](https://pl.aliexpress.com/item/1005006898362384.html?spm=a2g0o.order_list.order_list_main.16.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [JST PH 2.0 Cables and Connectors](https://pl.aliexpress.com/item/32665588344.html?spm=a2g0o.order_list.order_list_main.21.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [Switch Handle length 4mm](https://pl.aliexpress.com/item/4001207529493.html?spm=a2g0o.order_list.order_list_main.26.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [Battery](https://pl.aliexpress.com/item/1005008060921977.html?spm=a2g0o.order_list.order_list_main.31.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [TP4056 Charging Module Micro-USB](https://pl.aliexpress.com/item/1005008071836461.html?spm=a2g0o.order_list.order_list_main.37.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [Optional 3rd antenna for better range](https://pl.aliexpress.com/item/1005007039901040.html?spm=a2g0o.order_list.order_list_main.42.42211c24tHlYuV&gatewayAdapt=glo2pol)<br />
  [PCB 7x9cm](https://pl.aliexpress.com/item/32888385898.html?spm=a2g0o.order_list.order_list_main.47.42211c24tHlYuV&gatewayAdapt=glo2pol) You will need to cut it down to 7x5,5cm because of the fitment to the case designed by @emensta<br />
  [10uF Capacitor](https://pl.aliexpress.com/item/1005002524973878.html?spm=a2g0o.order_list.order_list_main.52.42211c24tHlYuV&gatewayAdapt=glo2pol) (2x) (any voltage above 5V)<br />
  [NRF24L01 PA](https://pl.aliexpress.com/item/1005007142575123.html?spm=a2g0o.order_list.order_list_main.57.42211c24tHlYuV&gatewayAdapt=glo2pol) (2x)<br />
  [ESP32 Dev Module](https://pl.aliexpress.com/item/1005006613312645.html?spm=a2g0o.order_list.order_list_main.62.42211c24tHlYuV&gatewayAdapt=glo2pol) Recommended: ESP32-32U CP2102<br />
  [M3 screws&nuts kit for the case](https://pl.aliexpress.com/item/1005002855686647.html?aff_fcid=6a3cf658a8c7443480b183b7236a4a21-1741732689780-09433-_oC24YXH&tt=CPS_NORMAL&aff_fsk=_oC24YXH&aff_platform=shareComponent-detail&sk=_oC24YXH&aff_trace_key=6a3cf658a8c7443480b183b7236a4a21-1741732689780-09433-_oC24YXH&terminal_id=5bcfda95327e49539b9b6782303a1b72&afSmartRedirect=y)

# ESP32-nRF24L01+ pinout + battery mod
<p>Here are both pinouts for HSPI and VSPI. You need both nRF24L01 modules connected in order to achieve full capability of the device.</p>

[nRF24l01 + pinout](https://dwdwpld.pages.dev/nRF24L01pinout.png)

<h1>HSPI</h1>

| 1st nRF24L01 module Pin | HSPI Pin (ESP32) | 10uf capacitor |
|---------------|------------------|--------------------|
| VCC           | 3.3V             | (+) capacitor |
| GND           | GND              | (-) capacitor |
| CE            | GPIO 16          |
| CSN           | GPIO 15          |
| SCK           | GPIO 14          |
| MOSI          | GPIO 13          |
| MISO          | GPIO 12          |
| IRQ           |                  |

<h1>VSPI</h1>

| 2nd nRF24L01 module Pin | VSPI Pin (ESP32) | 10uf capacitor |
|---------------|------------------|--------------------|
| VCC           | 3.3V             | (+) capacitor |
| GND           | GND              | (-) capacitor |
| CE            | GPIO 22          |
| CSN           | GPIO 21          |
| SCK           | GPIO 18          |
| MOSI          | GPIO 23          |
| MISO          | GPIO 19          |
| IRQ           |                  |

<h1>Status LED</h1>

| ESP32 | 4.7k Ohm Resistor | 3mm Status LED (blue)|
|-------|-------------------|----------------------|
|  GND  |                   |       (-) LED        |
|       |      Resistor     |       (+) LED        |
|GPIO27 |      Resistor     |                      |

### Battery modification
| 3.7V Li-Ion battery | JST-PH2 connector    | TP4056 Charging Module | Mini Slide Switch | ESP32 |
|---------------------|----------------------|------------------------|-------------------|-------|
| (+) Battery         | (+) JST-PH2          | Bat +                  |                   |       |
| (-) Battery         | (-) JST-PH2          | Bat -                  |                   |       |
|                     |                      | OUT +                  | Switch in         |       |
|                     |                      | OUT -                  |                   |  GND  |
|                     |                      |                        | Switch out        |  3V3  |

# Section Developed by [emensta](https://github.com/EmenstaNougat/)

## Flashing the firmware
### via webflasher (Easy)  
![ESP32-BlueJammerFlasher](https://dwdwpld.pages.dev/ESP32BlueJammerFlasher.png)                                                                 
I've created a webflasher to make it super easy for you to flash your ESP32 chip with the ESP32-BlueJammer firmware of your choice!  
- Visit [ESP32-BlueJammerFlasher](https://esp32-bluejammerflasher.pages.dev)
- Connect your ESP32 via a data USB cable
- Choose your firmware, chip and connect
- Flash the firmware of your choice :D

### via BlueFlasher.exe -Windows application (Easy)  
<img src="https://dwdwpld.pages.dev/BlueFlasherMain.jpg" width="650" height="auto">

The BlueFlasher.exe lets you flash any available firmware with no more than 3 clicks! It is always the latest up-to-date firmware!  
- Download the [BlueFlasher.exe](https://github.com/EmenstaNougat/ESP32-BlueJammer/raw/refs/heads/main/BlueFlasher/BlueFlasher.exe)
- run the application [(Image)](https://dwdwpld.pages.dev/BlueFlasherMain.jpg)
- simply choose the COM port of your ESP32 [(Image)](https://dwdwpld.pages.dev/BlueFlasherCOM.jpg)
- hold the "Boot" button on your ESP32 from now on
- choose the firmware you want to flash
- release the "Boot" button on your ESP32
- wait for the firmware to be flashed (check console) :D

https://github.com/user-attachments/assets/9c6b7322-9d39-48a1-9ef4-535c6ff64681

**Developed by [9dl](https://github.com/9dl)**

### Flashing ESP32 via binary files (Advanced)  
- Download the **.bin files** available on this repository
- Use any flasher of your choice
- Flash it :D

If your ESP32 is not showing up in the device list or won't get recognized you will need to have [THESE DRIVERS INSTALLED](https://www.silabs.com/documents/public/software/CP210x_Windows_Drivers.zip) which can be found on my [Discord server](https://discord.gg/yNGhKxzqUE) too!

## 3D printed case
#### The 3D printed case fits ONLY a PCB size of 7cm x 5.5cm and you'll need to drill out 2 holes according for the M3 screws to fit through the PCB!
<h3 align="center">Access to the ESP32 micro-USB port, aswell as to both EN & Boot buttons</h3>

![ESP32MicroUSB](https://dwdwpld.pages.dev/ESP32-BlueJammerMicroUsb.jpg)

<h3 align="center">TP4056 charging port access with charging state indicator holes (red=charging - blue=fully charged)</h3>

![USB_C_chargerWithIndicators](https://dwdwpld.pages.dev/ESP32-BlueJammerUSB_C_chargerWithIndicators.jpg)

<h3 align="center">On/off switch with blue indicator LED</h3>

![OnOffSwitch](https://dwdwpld.pages.dev/ESP32-BlueJammerOnOffSwitch.jpg)



## V3-Case 3D model view [[download .stl](https://dwdwpld.pages.dev/V3-ESP32-BlueJammerBy@emensta3DCase.stl)]

<h3 align="center">Here's a look at the V3 2 antenna version itself</h3>

![3DCaseView](https://dwdwpld.pages.dev/V3-ESP32-BlueJammer3DCaseView.png)



## V4-Case 3D model view [[download .stl](https://dwdwpld.pages.dev/V4-ESP32-BlueJammerBy@emensta3DCase.stl)]

<h3 align="center">Here's a look at the V4 3 antenna version itself</h3>

![3DCaseView](https://dwdwpld.pages.dev/V4-ESP32-BlueJammer3DCaseView.png)

# Demonstration of use in a controlled enviroment

[▶️Jammer Demonstration](https://electro5218.github.io/security-engineering-lab/esp32-jammer/assets/JammerDemonstration.mp4)





