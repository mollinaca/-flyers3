#!/usr/bin/env python3
import configparser
import json
import os
import pathlib
import requests
import shutil
import time

class F3:

    def get_slack_conf() -> list:
        here = pathlib.Path(__file__).resolve().parent
        # CONFIG_FILE = str(here) + "/config.ini"
        CONFIG_FILE = str(here) + "/config_dev.ini"  # for development
        cfg = configparser.ConfigParser()
        cfg.read(CONFIG_FILE)
        return ([cfg["slack"]["token"], cfg["slack"]["channel"]])

    def get_target_shops() -> dict:
        here = pathlib.Path(__file__).resolve().parent
        # CONFIG_FILE = str(here) + "/config.ini"
        CONFIG_FILE = str(here) + "/config_dev.ini"  # for development
        cfg = configparser.ConfigParser()
        cfg.read(CONFIG_FILE)
        return (json.loads(cfg["target"]["shops"]))



    def get_last_json() -> dict:
        _LAST_FLYERS_FILE = "last.json"

        if os.path.exists(_LAST_FLYERS_FILE):
            if os.path.getsize(_LAST_FLYERS_FILE) == 0:
                ret = []
            else:
                json_open = open(_LAST_FLYERS_FILE, "r")
                last = json.load(json_open)
                ret = last["flyers"]
        else:
            ret = []

        return ret


def main():
    """
    set slack token and target shops from config.ini
    """
    SLACK_BOT_TOKEN, SLACK_CHANNEL = F3.get_slack_conf()
    TARGET_SHOPS = F3.get_target_shops()

    exit (0)


