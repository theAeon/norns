from nose.tools import *
import norns
from norns.exceptions import ConfigError


def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_basic():
    cfg = norns.config(config_file="tests/data/simple.yaml")
    assert cfg["integer"] == 10
    assert cfg["path"] == "/home/simon"
    assert 3 == len(cfg.keys())


@raises(ConfigError)
def test_no_arguments():
    cfg = norns.config()
