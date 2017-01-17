#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '06/01/2017'
__author__ = 'deling.ma'
"""
import yaml


def load_settings(settings_source='./settings/app.yml'):
    with open(settings_source) as settings:
        return yaml.load(settings)
