"""Signature helpers for the demo service."""

import oqs


def make_signing_key():
    signer = oqs.Signature('ML-DSA-65')
    return signer
