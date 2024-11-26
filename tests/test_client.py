from flowx_sdk.client import Client

def test_init_client():
    client = Client(api_key="ab6d74b8d46d7f8952bad3f1e0388e41")
    assert client.authenticated is True
