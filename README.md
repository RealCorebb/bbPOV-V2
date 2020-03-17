# bbPOV-V2
The 2nd Gen of Corebb's POV Display,Using ESP32.

Thanks to homemadegarbage.com for the article, the code is based on it and has undergone many optimizations.

# HardWares:
Apa102
TTGO-T8 ESP32  (16MB Flash Size,with 8MB PSRAM,and built-in SD-Card Slot and Power socket)
3.7V lithium battery

# Currently Feactures:
Just showing animations (gif)
Div up to 250
Frames up to 200


# Used Libraries:
NeopixelBus

# TODO
1.Using BLE to control it! eg.Next/Pause/Speed Control/Sendding new animation to bbPOV ....
2.Using WIFI to show some Internet's data   eg.My Bilibili's Subscribers...
3.Using SD-Card to store more data.
4.Figure out how to use PSRAM to make it possible to show different larger animation.(Currently,because of the small RAM of the esp32,all of the animations are stored in the Flash,and they are static,which means they can't be changed without re-flash or OTA.) 
