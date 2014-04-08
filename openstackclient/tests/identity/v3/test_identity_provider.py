#   Copyright 2014 CERN.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import copy

from openstackclient.identity.v3 import identity_provider
from openstackclient.tests import fakes
from openstackclient.tests.identity.v3 import fakes as identity_fakes


class TestIdentityProvider(identity_fakes.TestFederatedIdentity):

        def setUp(self):
            super(TestIdentityProvider, self).setUp()

            self.identity_providers_mock = self.app.client_manager.\
                identity.identity_providers

            self.identity_providers_mock.reset_mock()


class TestIdentityProviderCreate(TestIdentityProvider):

        def setUp(self):
                super(TestIdentityProviderCreate, self).setUp()

                self.identity_providers_mock.return_value = fakes.FakeResource(
                    None,
                    copy.deepcopy(identity_fakes.IDENTITY_PROVIDER),
                    loaded=True
                )

                self.cmd = identity_provider.CreateIdentityProvider(
                    self.app, None)

        def test_create_empty_identity_provider(self):
                arglist = [
                        identity_fakes.idp_id
                ]
                verifylist = [
                        ('identity_provider', identity_fakes.idp_id)
                ]
                parsed_args = self.check_parser(self.cmd, arglist, verifylist)
                columns, data = self.cmd.take_action(parsed_args)
