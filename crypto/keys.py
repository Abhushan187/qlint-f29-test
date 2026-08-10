"""Key generation helpers for the demo service."""

import oqs


def make_transport_key():
    kem = oqs.KeyEncapsulation('ML-KEM-768')
    return kem.generate_keypair()
