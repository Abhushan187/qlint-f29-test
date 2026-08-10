"""Signature helpers for the demo service."""

from cryptography.hazmat.primitives.asymmetric import ec


def make_signing_key():
    key = ec.generate_private_key(ec.SECP256R1())
    return key
