====================
:program:`openstack`
====================

OpenStack Command Line

SYNOPSIS
========

:program:`openstack` [<global-options>] <command> [<command-arguments>]

:program:`openstack help` <command>

:program:`openstack` --help


DESCRIPTION
===========

:program:`openstack` provides a common command-line interface to OpenStack APIs.  It is generally
equivalent to the CLIs provided by the OpenStack project client libraries, but with
a distinct and consistent command structure.

:program:`openstack` uses a similar authentication scheme as the OpenStack project CLIs, with
the credential information supplied either as environment variables or as options on the
command line.  The primary difference is the use of 'project' in the name of the options
``OS_PROJECT_NAME``/``OS_PROJECT_ID`` over the old tenant-based names.

::

    export OS_AUTH_URL=<url-to-openstack-identity>
    export OS_PROJECT_NAME=<project-name>
    export OS_USERNAME=<user-name>
    export OS_PASSWORD=<password>  # (optional)


OPTIONS
=======

:program:`openstack` takes global options that control overall behaviour and command-specific options that control the command operation.  Most global options have a corresponding environment variable that may also be used to set the value. If both are present, the command-line option takes priority. The environment variable names are derived from the option name by dropping the leading dashes ('--'), converting each embedded dash ('-') to an underscore ('_'), and converting to upper case.

:program:`openstack` recognizes the following global topions:

:option:`--os-auth-url` <auth-url>
    Authentication URL

:option:`--os-domain-name` <auth-domain-name> | :option:`--os-domain-id` <auth-domain-id>
    Domain-level authorization scope (name or ID)

:option:`--os-project-name` <auth-project-name> | :option:`--os-project-id` <auth-project-id>
    Project-level authentication scope (name or ID)

:option:`--os-project-domain-name` <auth-project-domain-name> | :option:`--os-project-domain-id` <auth-project-domain-id>
    Domain name or id containing project

:option:`--os-username` <auth-username>
    Authentication username

:option:`--os-user-domain-name` <auth-user-domain-name> | :option:`--os-user-domain-id` <auth-user-domain-id>
    Domain name or id containing user

:option:`--os-password` <auth-password>
    Authentication password

:option:`--os-region-name` <auth-region-name>
    Authentication region name

:option:`--os-default-domain` <auth-domain>
    Default domain ID (Default: 'default')

:option:`--os-use-keyring`
    Use keyring to store password (default: False)

:option:`--os-cacert` <ca-bundle-file>
    CA certificate bundle file

:option:`--verify` | :option:`--insecure`
    Verify or ignore server certificate (default: verify)

:option:`--os-identity-api-version` <identity-api-version>
    Identity API version (Default: 2.0)

:option:`--os-XXXX-api-version` <XXXX-api-version>
    Additional API version options will be available depending on the installed API libraries.


COMMANDS
========

To get a list of the available commands::

    openstack --help

To get a description of a specific command::

    openstack help <command>


:option:`complete`
    Print the bash completion functions for the current command set.

:option:`help <command>`
    Print help for an individual command


NOTES
=====

The command list displayed in help output reflects the API versions selected.  For
example, to see Identity v3 commands ``OS_IDENTITY_API_VERSION`` must be set to ``3``.


EXAMPLES
========

Show the detailed information for server ``appweb01``::

    openstack \
        --os-project-name ExampleCo \
        --os-username demo --os-password secrete \
        --os-auth-url http://localhost:5000:/v2.0 \
        server show appweb01

The same command if the auth environment variables (:envvar:`OS_AUTH_URL`, :envvar:`OS_PROJECT_NAME`,
:envvar:`OS_USERNAME`, :envvar:`OS_PASSWORD`) are set::

    openstack server show appweb01

Create a new image::

    openstack image create \
        --disk-format=qcow2 \
        --container-format=bare \
        --public \
        --copy-from http://somewhere.net/foo.img \
        foo


FILES
=====

:file:`~/.openstack`
    Placeholder for future local state directory.  This directory is intended to be shared among multiple OpenStack-related applications; contents are namespaced with an identifier for the app that owns it.  Shared contents (such as :file:`~/.openstack/cache`) have no prefix and the contents must be portable.


ENVIRONMENT VARIABLES
=====================

The following environment variables can be set to alter the behaviour of :program:`openstack`.  Most of them have corresponding command-line options that take precedence if set.

:envvar:`OS_AUTH_URL`
    Authentication URL

:envvar:`OS_DOMAIN_NAME`
    Domain-level authorization scope (name or ID)

:envvar:`OS_PROJECT_NAME`
    Project-level authentication scope (name or ID)

:envvar:`OS_PROJECT_DOMAIN_NAME`
    Domain name or id containing project

:envvar:`OS_USERNAME`
    Authentication username

:envvar:`OS_USER_DOMAIN_NAME`
    Domain name or id containing user

:envvar:`OS_PASSWORD`
    Authentication password

:envvar:`OS_REGION_NAME`
    Authentication region name

:envvar:`OS_DEFAULT_DOMAIN`
    Default domain ID (Default: ‘default’)

:envvar:`OS_USE_KEYRING`
    Use keyring to store password (default: False)

:envvar:`OS_CACERT`
    CA certificate bundle file

:envvar:`OS_IDENTITY_API_VERISON`
    Identity API version (Default: 2.0)

:envvar:`OS_XXXX_API_VERISON`
    Additional API version options will be available depending on the installed API libraries.


BUGS
====

Bug reports are accepted at the python-openstackclient LaunchPad project
"https://bugs.launchpad.net/python-openstackclient/+bugs".


AUTHORS
=======

Please refer to the AUTHORS file distributed with OpenStackClient.


COPYRIGHT
=========

Copyright 2011-2014 OpenStack Foundation and the authors listed in the AUTHORS file.


LICENSE
=======

http://www.apache.org/licenses/LICENSE-2.0


SEE ALSO
========

The `OpenStackClient page <https://wiki.openstack.org/wiki/OpenStackClient>`_
in the `OpenStack Wiki <https://wiki.openstack.org/>`_ contains further
documentation.

The individual OpenStack project CLIs, the OpenStack API references.
