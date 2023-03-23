from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("buapau", 9) == "uapaub"

    assert encrypt_message("buapau", 3) == "aub_uap"

    assert encrypt_message("buapau", 4) == "ua_paub"

    with pytest.raises(TypeError):
        encrypt_message("hello", "1")
