# monitored (300)

## Description
An attacker tried to monitor my chats...was he able to get anything?

Author - kn1gh7

## Attachment
chall.pcap

## Writeup
Get HID data using the following filter
```
(usb.transfer_type = 0x01 and frame.len == 35) and !(usb.capdata == 00:00:00:00:00:00:00:00)
```
Find a keystrokes mapping online and decode

TODO: Add a script to automate the task

## FLAG
COPS{k3l0gg3r_g03s_brrrr}
