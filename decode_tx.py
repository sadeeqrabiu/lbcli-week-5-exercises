import sys
import json
import urllib.request

tx_hex = sys.argv[1]

# using a public blockstream or similar api to decode is generally not allowed without token or might fail.
# Instead, parse basic segwit tx format locally
def decode(hex_data):
    pass # Wait, let me just try if bitcoin-cli is available locally
