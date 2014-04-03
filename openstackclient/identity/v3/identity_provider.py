#   Copyright 2012-2013 OpenStack Foundation
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
#

"""Identity v3 IdentityProvider action implementations"""

import logging
import six
import sys

from cliff import command
from cliff import lister
from cliff import show

from openstackclient.common import utils


class CreateIdentityProvider(show.ShowOne):
    """Create identity_provider command"""

    log = logging.getLogger(__name__ + '.CreateIdentityProvider')

    def get_parser(self, prog_name):
        parser = super(CreateIdentityProvider, self).get_parser(prog_name)
        parser_add_argument(
            '--id',
            metavar='<identity_provider id>',
            help='New identity_provider id (must be unique)'
        )
        parser.add_argument(
            '--description',
            metavar='<description>',
            help='New identity_provider description',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        identity_client = self.app.client_manager.identity
        idp = identity_client.identity_providers.create(
            parsed_args.id, parsed_args.description
        )
        info = {}
        info.update(idp._info)
        return zip(*sorted(six.iteritems(info)))


class DeleteIdenityProvider(command.Command):
    """Delete identity_provider command"""

    log = logging.getLogger(__name__ + '.DeleteIdentityProvider')

    def get_parser(self, prog_name):
        parser = super(DeleteIdentityProvider, self).get_parser(prog_name)
        parser.add_argument(
            'identity_provider',
            metavar='<identity_provider>',
            help='ID of identity_provider to delete',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        identity_client = self.app.client_manager.identity
        identity_provider = utils.find_resource(
            identity_client.identity_providers, parsed_args.identity_provider)
        identity_client.identity_providers.delete_identity_provider(identity_provider.id)
        return


class ListIdentityProvider(lister.Lister):
    """List identity_provider command"""

    log = logging.getLogger(__name__ + '.ListIdentityProvider')

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        columns = ('ID', 'Description')
        data = self.app.client_manager.identity.identity_providers.list_identity_providers()
        return (columns,
                (utils.get_item_properties(
                    s, columns,
                    formatters={},
                ) for s in data))


class SetIdentityProvider(command.Command):
    """Set identity_provider command"""

    log = logging.getLogger(__name__ + '.SetIdentityProvider')

    def get_parser(self, prog_name):
        parser = super(SetIdentityProvider, self).get_parser(prog_name)
        parser.add_argument(
            'identity_provider',
            metavar='<identity_provider>',
            help='ID of identity_provider to change',
        )
        parser.add_argument(
            '--description',
            metavar='<new-identity_provider-description>',
            help='New identity_provider description',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        identity_client = self.app.client_manager.identity
        identity_provider = utils.find_resource(
            identity_client.identity_providers, parsed_args.identity_provider)
        kwargs = {}
        if parsed_args.description:
            kwargs['description'] = parsed_args.description

        if not len(kwargs):
            sys.stdout.write("IdentityProvider not updated, no arguments present")
            return

        identity_provider = identity_client.identity_providers.update_identity_provider(
            identity_provider.id,
            **kwargs
        )

        info = {}
        info.update(identity_provider._info)
        return zip(*sorted(six.iteritems(info)))


class ShowIdentityProvider(show.ShowOne):
    """Show identity_provider command"""

    log = logging.getLogger(__name__ + '.ShowIdentityProvider')

    def get_parser(self, prog_name):
        parser = super(ShowIdentityProvider, self).get_parser(prog_name)
        parser.add_argument(
            'identity_provider',
            metavar='<identity_provider>',
            help='ID of identity_provider to display',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)
        identity_client = self.app.client_manager.identity
        identity_provider = utils.find_resource(
            identity_client.identity_providers, parsed_args.identity_provider)

        info = {}
        info.update(identity_provider._info)
        return zip(*sorted(six.iteritems(info)))
