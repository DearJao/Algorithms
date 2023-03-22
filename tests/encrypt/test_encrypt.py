from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Test with key as non-positive integer
    with pytest.raises(ValueError):
        encrypt_message(-1, "hello")

    # Test with key greater than message length
    assert encrypt_message("buapau", 9) == "uapaub"

    # Test with odd key
    assert encrypt_message("buapau", 3) == "aub_uap"

    # Test with even key
    assert encrypt_message("buapau", 4) == "ua_paub"
