from fastecdsa import keys, curve, ecdsa, point
import json

class EcWalletClient:
    def __init__(self):
        self.keypairs = {}
        self.uncompressed_keys = {}

    def generate_keypair(self):
        priv_key, pub_key = keys.gen_keypair(curve.secp256k1)
        if (pub_key.y%2):
            compressed_pub_key = '03' + str(hex(pub_key.x))[2:]
        else:
            compressed_pub_key = '02' + str(hex(pub_key.x))[2:]
        self.keypairs[compressed_pub_key] = priv_key
        self.uncompressed_keys[str(hex(pub_key.x))] = int(pub_key.y)
        return compressed_pub_key

    def import_keypair(self, priv_key):
        pub_key = keys.get_public_key(int(priv_key, 16), curve.secp256k1)
        if (pub_key.y%2):
            compressed_pub_key = '03' + str(hex(pub_key.x))[2:]
        else:
            compressed_pub_key = '02' + str(hex(pub_key.x))[2:]
        self.keypairs[compressed_pub_key] = int(priv_key, 16)
        self.uncompressed_keys[str(hex(pub_key.x))] = int(pub_key.y)
        return compressed_pub_key

    # Takes JSON object as payload
    def sign(self, payload, user_id):
        canonical_payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))
        private_key = self.keypairs[user_id]
        r, s = ecdsa.sign(canonical_payload, private_key, curve=curve.secp256k1)
        return {"r": hex(r)[2:], "s": hex(s)[2:]}

    # Takes JSON object as payload
    def verify(self, payload, user_id, r, s):
        canonical_payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))
        pub_key_x = '0x' + user_id[2:]
        hex_int = int(pub_key_x, 16)
        return ecdsa.verify((int(r, 16), int(s, 16)), canonical_payload, point.Point(hex_int, (self.uncompressed_keys[pub_key_x]), curve.secp256k1), curve=curve.secp256k1)