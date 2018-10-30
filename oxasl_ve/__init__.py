"""
OXASL module for vessel-encoded ASL data

This module is designed to operate within the OXASL pipeline.
If installed, then it will be called by ``oxasl.oxford_asl.oxasl``
whenever vessel-encoded data is supplied.

The relevant processing function can also be called independently
on a ``Workspace`` object, however this will not include the
standard oxasl preprocessing or registration.
"""
from .api import model_ve, VeaslOptions

__all__ = ["model_ve", "VeaslOptions"]