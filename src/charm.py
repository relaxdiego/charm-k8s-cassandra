#!/usr/bin/env python3
import logging

logger = logging.getLogger()
import sys

sys.path.append('lib')

from ops.charm import (
    CharmBase,
)
from ops.main import main


# CHARM

# This charm class mainly does self-configuration via its initializer and
# contains not much logic. It also just has one-liner delegators the design
# of which is further discussed below (just before the delegator definitions)


class Charm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)


if __name__ == "__main__":
    main(Charm)
