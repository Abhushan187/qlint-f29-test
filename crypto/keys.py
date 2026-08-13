"""Key generation helpers for the demo service."""

import logging

import oqs


def make_transport_key():
    kem = oqs.KeyEncapsulation('ML-KEM-768')
    public_key = kem.generate_keypair()
    return kem, public_key
