"""Key generation helpers for the demo service."""

from Crypto.PublicKey import RSA


def make_transport_key():
    key = RSA.generate(2048)
    return key
