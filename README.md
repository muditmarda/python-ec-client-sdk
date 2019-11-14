# Python EC wallet client sdk

A python micro-library of ECDSA functions for generation of keypairs, signing and verification.

### Installation

Python 3 is required to install this sdk. Note: It is recommended to use a virtualenv

```shell
(venv) $ git clone https://github.com/vaultbank/python-ec-client-sdk
(venv) $ python setup.py install
```
or 
```shell
(venv) $  pip install git+https://github.com/vaultbank/python-ec-client-sdk.git
```

### Usage

Import the library
```python
FROM ec_wallet import EcWalletClient
wallet_client = EcWalletClient()
```

Following functions are available in the library:
1. **generate_keypair:** Generates a keypair and returns the public key while storing the private key in the wallet for signing (This public key is to be used as "user_id" of users during tests)
```python
wallet_client.generate_keypair()
```

2. **import_keypair:** Imports a private key in the wallet that can be used for signing
```python
wallet_client.import_keypair(priv_key)
```

3. **sign:** Takes a JSON payload and signs it using the private key corresponding to the supplied user_id. (Returns r, s of Signature)
```python
wallet_client.sign(payload, user_id)
```

4. **verify:** Verifies that a JSON payload was signed using the private key corresponding to the supplied user_id. (Takes r, s of signature and returns a boolean)
```python
wallet_client.verify(payload, user_id, r, s)
```
