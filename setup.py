#! /usr/bin/env python3

# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.


"""
Koji Smoky Dingo - a collection of Koji command-line features for
advanced users.

:author: Christopher O'Brien  <obriencj@gmail.com>
:license: GPL version 3
"""


COMMANDS = {
    "affected-targets": "kojismokydingo.cli.tags:AffectedTargets",
    "block-env-var": "kojismokydingo.cli.tags:BlockEnvVar",
    "block-rpm-macro": "kojismokydingo.cli.tags:BlockRPMMacro",
    "bulk-move-builds": "kojismokydingo.cli.builds:BulkMoveBuilds",
    "bulk-tag-builds": "kojismokydingo.cli.builds:BulkTagBuilds",
    "bulk-untag-builds": "kojismokydingo.cli.builds:BulkUntagBuilds",
    "check-hosts": "kojismokydingo.cli.hosts:CheckHosts",
    "client-config": "kojismokydingo.cli.clients:ClientConfig",
    "cginfo": "kojismokydingo.cli.users:ShowCGInfo",
    "filter-builds": "kojismokydingo.cli.builds:FilterBuilds",
    "filter-tags": "kojismokydingo.cli.tags:FilterTags",
    "latest-archives": "kojismokydingo.cli.archives:LatestArchives",
    "list-btypes": "kojismokydingo.cli.builds:ListBTypes",
    "list-build-archives": "kojismokydingo.cli.archives:ListBuildArchives",
    "list-cgs": "kojismokydingo.cli.builds:ListCGs",
    "list-component-builds": "kojismokydingo.cli.builds:ListComponents",
    "list-env-vars": "kojismokydingo.cli.tags:ListEnvVars",
    "list-rpm-macros": "kojismokydingo.cli.tags:ListRPMMacros",
    "list-tag-extras": "kojismokydingo.cli.tags:ListTagExtras",
    "open": "kojismokydingo.cli.clients:ClientOpen",
    "perminfo": "kojismokydingo.cli.users:ShowPermissionInfo",
    "remove-env-var": "kojismokydingo.cli.tags:RemoveEnvVar",
    "remove-rpm-macro": "kojismokydingo.cli.tags:RemoveRPMMacro",
    "renum-tag-inheritance": "kojismokydingo.cli.tags:RenumTagInheritance",
    "set-env-var": "kojismokydingo.cli.tags:SetEnvVar",
    "set-rpm-macro": "kojismokydingo.cli.tags:SetRPMMacro",
    "swap-tag-inheritance": "kojismokydingo.cli.tags:SwapTagInheritance",
    "userinfo": "kojismokydingo.cli.users:ShowUserInfo",
}


STANDALONE = {
    "ksd-filter-builds": "kojismokydingo.standalone.builds:ksd_filter_builds",
    "ksd-filter-tags": "kojismokydingo.standalone.tags:ksd_filter_tags",
}


def config():
    return {
        "packages": [
            "koji_cli_plugins",
            "kojismokydingo",
            "kojismokydingo.cli",
            "kojismokydingo.sift",
            "kojismokydingo.standalone",
        ],

        "package_data": {
            "kojismokydingo": ["py.typed", ],
        },

        "install_requires": [
            "appdirs",
            "koji",

            # backport requirements
            "enum34 ; python_version < '3.4'",
            "typing_extensions ; python_version < '3.8'",
        ],

        "tests_require": [
            "appdirs",
            "docutils",
            "koji",
        ],

        # The koji_cli_plugins namespace package needs to be a plain
        # directory that Koji can look through for individual plugins
        "zip_safe": False,

        "entry_points": {
            "koji_smoky_dingo": ["=".join(c) for c in COMMANDS.items()],
            "console_scripts":  ["=".join(c) for c in STANDALONE.items()],
        },
    }


def setup():
    import setuptools
    return setuptools.setup(**config())


if __name__ == "__main__":
    setup()


#
# The end.
