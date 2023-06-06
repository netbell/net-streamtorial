# net-streamtorial

## Introduction
This is a fork of [net-textorial](https://github.com/dannywade/net-textorial), originally developed by [@dannywade](https://github.com/dannywade) and [@JulioPDX](https://github.com/JulioPDX), which is a simple app showing off the power of a text-based user interface (TUI) and how it can be used with network automation. This fork has modified that code to work in a web interface using streamlit. 

With recent changes, it has evolved into a learning tool that shows network engineers the differences between raw (human-friendly) CLI output and parsed (structured) output. The tool will take any 'show' command and produce the raw and parsed outputs (using [ntc-templates](https://github.com/networktocode/ntc-templates) for parsing). This will be valuable for engineers that want to learn and see the differences between raw (unstructured) and parsed (structured) data outputs. Additionally, tabular output has been added with the pandas library. 

Under the hood, this tool is leveraging [Netmiko](https://github.com/ktbyers/netmiko) and [Streamlit](hhttps://streamlit.io/). Thank you to all involved!


## Features
- **It just works**: Set your device CLI credentials as environment variables or enter in the web interface! Device types are automagically determined using Netmiko's awesome `ssh_autodetect` module but can be set manually to increase response time.
- **Vendor agnostic**: This tool is not built for a particular vendor. With vendor-agnostic libraries being used under the hood, many different device vendors and device types are supported. See [Device Support](#device-support) section for more details.

## Get Started

```shell
git clone https://github.com/netbell/net-streamtorial.git
cd net-streamtorial
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Basic Usage

1. Set your device CLI credentials as environment variables. The variable key names are `NET_TEXT_USER` and `NET_TEXT_PASS`. This can also be accomplished by creating a .env file with the same values. If the variables are not set, the interface will request username and password. 

    ```shell
    NET_TEXT_USER=<your username>
    NET_TEXT_PASS=<your password>
    ```
2. Run the app

    ```shell
    streamlit run net.py
    ```
3. Enter the hostname/IP of the device and a valid 'show' command, hit enter or clock 'Run'

    ![screenshot2](https://github.com/netbell/net-streamtorial/assets/47117028/5a1bf32c-7627-432f-bf37-6623891a3b89)


## Supported Devices/Parsers

### Device Support

Any device that is supported by Netmiko can be used with this tool. Under the hood, all device connections are created using the Netmiko library. Here are some of the popular supported (and tested) platforms by Netmiko:
- Arista vEOS
- Cisco ASA, IOS, IOS-XE, IOS-XR, NX-OS
- HP ProCurve
- Juniper Junos
- Linux


### Parser Support

Currently, only ntc-templates is supported and used to parse all command output.


## Demo

https://github.com/netbell/net-streamtorial/assets/47117028/27df49b1-8cbf-4d23-8135-586ba0a9b7f0


