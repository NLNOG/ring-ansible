# vim: set ft=python:

"""Deterministic "random" numbers jinja filter for ansible.

Place in filter_plugins/ to use.
"""

import random

def determrand(high, seed, low=0):
    """{{60|determrand(ansible_fqdn)}}"""
    return random.Random(seed).randint(low, high-1)

class FilterModule(object):
    """Hook filter up to ansible template processing."""
    def filters(self):
        """Return list of filters provided by module."""
        return {'determrand': determrand}
