# -*- coding: utf-8 -*-
# Copyright 2014-2016 OpenMarket Ltd
# Copyright 2018-9 New Vector Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" This is a reference implementation of a Matrix homeserver.
"""

import os
import sys

# Check that we're not running on an unsupported Python version.
if sys.version_info < (3, 5):
    print("Synapse requires Python 3.5 or above.")
    sys.exit(1)

try:
    from twisted.internet import protocol
    from twisted.internet.protocol import Factory
    from twisted.names.dns import DNSDatagramProtocol

    protocol.Factory.noisy = False
    Factory.noisy = False
    DNSDatagramProtocol.noisy = False
except ImportError:
    pass

__version__ = "1.7.0rc1"

if bool(os.environ.get("SYNAPSE_TEST_PATCH_LOG_CONTEXTS", False)):
    # We import here so that we don't have to install a bunch of deps when
    # running the packaging tox test.
    from synapse.util.patch_inline_callbacks import do_patch

    do_patch()
