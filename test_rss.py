import sys
import os
from .rss import main
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def test_rss():
    assert 1 == main()
