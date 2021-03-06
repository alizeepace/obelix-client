# -*- coding: utf-8 -*-
#
# This file is part of Obelix.
# Copyright (C) 2015 CERN.
#
# Obelix is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Obelix is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Obelix; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import json
import unittest

from obelix_client.storage import RedisMock, RedisStorage, StorageProxy


class TestStorageDict(unittest.TestCase):

    def test_set_and_get(self):
        storage = StorageProxy({})
        storage.set("theKey", "theValue")
        storage.set("theKey2", "theValue2")
        assert storage.get("theKey2") == "theValue2"
        assert storage.get("theKey") == "theValue"
        assert storage.get("noKey") == None

    def test_set_and_get_with_prefix_encoder(self):
        storage = StorageProxy({}, prefix='pre::', encoder=json)
        storage.set("theKey", "theValue")
        storage.set("theKey2", "theValue2")
        assert storage.get("theKey2") == "theValue2"
        assert storage.get("theKey") == "theValue"
        assert storage.get("noKey") == None

    def test_redis_set_and_get_with_prefix_encoder(self):
        storage = RedisStorage(RedisMock(), prefix='pre::', encoder=json)
        storage.set("theKey", "theValue")
        storage.set("theKey2", "theValue2")
        assert storage.get("theKey2") == "theValue2"
        assert storage.get("theKey") == "theValue"
        assert storage.get("noKey") == None
