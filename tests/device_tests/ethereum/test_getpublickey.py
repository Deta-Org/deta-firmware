# This file is part of the detahard project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from detahardlib import ethereum
from detahardlib.debuglink import detahardClientDebugLink as Client
from detahardlib.exceptions import detahardFailure
from detahardlib.tools import parse_path

from ...common import parametrize_using_common_fixtures

pytestmark = [pytest.mark.altcoin, pytest.mark.ethereum]


@parametrize_using_common_fixtures("ethereum/getpublickey.json")
def test_ethereum_getpublickey(client: Client, parameters, result):
    path = parse_path(parameters["path"])
    res = ethereum.get_public_node(client, path)
    assert res.node.depth == len(path)
    assert res.node.fingerprint == result["fingerprint"]
    assert res.node.child_num == result["child_num"]
    assert res.node.chain_code.hex() == result["chain_code"]
    assert res.node.public_key.hex() == result["public_key"]
    assert res.xpub == result["xpub"]


def test_slip25_disallowed(client: Client):
    path = parse_path("m/10025'/60'/0'/0/0")
    with pytest.raises(detahardFailure):
        ethereum.get_public_node(client, path)


@pytest.mark.skip_t2
def test_legacy_restrictions(client: Client):
    path = parse_path("m/46'")
    with pytest.raises(detahardFailure, match="Invalid path for EthereumGetPublicKey"):
        ethereum.get_public_node(client, path)