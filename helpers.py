import ipaddress
import json
import os
import streamlit as st
from dotenv import load_dotenv
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from netmiko.ssh_autodetect import SSHDetect

load_dotenv()

class NetworkDevice:
    def __init__(self, host_id: str, credentials: dict, device_type: str):
        self.host_id = host_id
        self.credentials = credentials
        self.device_type = device_type
        self.connection = None

    def device_connection(self):
        remote_device = {
            "device_type": self.device_type,
            "host": self.host_id,
            "username": self.credentials.get("username"),
            "password": self.credentials.get("password"),
        }
        if self.device_type == "autodetect":
            try:
                guesser = SSHDetect(**remote_device)
                best_match = guesser.autodetect()
                remote_device["device_type"] = best_match
                st.caption(f"autodetect: {best_match}")
            except NetmikoTimeoutException as e:
                st.error("Connection timed out")
                self.connection = None
            except NetmikoAuthenticationException as e:
                st.error("Authentication error")
                self.connection = None
        try:
            self.connection = ConnectHandler(**remote_device)
        except NetmikoTimeoutException as e:
            st.error("Connection timed out")
            self.connection = None
        except NetmikoAuthenticationException as e:
            st.error("Authentication error")
            self.connection = None

    def get_device_info(self, command):

        raw_output = None
        parsed_output = None

        if self.connection is not None:
            try:
                if command.split()[0] != "show":
                    st.error("Only 'show' commands are supported.")
                else:
                    raw_output = self.connection.send_command(command.lower())
                    parsed_output = self.connection.send_command(command.lower(), use_textfsm=True)
            
            except Exception as e: 
                st.exception(e)

        if raw_output and ("invalid input" in raw_output.lower() or "invalid command" in raw_output.lower()):
            raw_output, parsed_output = None, None
            st.error("Invalid command sent to the device.")

        else:
            try:
                iter(parsed_output)
                parsed_output = json.dumps(parsed_output, indent=2)
            except TypeError:
                pass

        return raw_output, parsed_output
