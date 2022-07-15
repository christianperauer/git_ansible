# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the nxos_bgp_address_family module
"""


class Bgp_address_familyArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_bgp_address_family module
    """

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "type": "dict",
            "options": {
                "as_number": {"type": "str"},
                "address_family": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "afi": {
                            "type": "str",
                            "choices": [
                                "ipv4",
                                "ipv6",
                                "link-state",
                                "vpnv4",
                                "vpnv6",
                                "l2vpn",
                            ],
                            "required": True,
                        },
                        "safi": {
                            "type": "str",
                            "choices": [
                                "unicast",
                                "multicast",
                                "mvpn",
                                "evpn",
                            ],
                        },
                        "additional_paths": {
                            "type": "dict",
                            "options": {
                                "install_backup": {"type": "bool"},
                                "receive": {"type": "bool"},
                                "selection": {
                                    "type": "dict",
                                    "options": {"route_map": {"type": "str"}},
                                },
                                "send": {"type": "bool"},
                            },
                        },
                        "advertise_l2vpn_evpn": {"type": "bool"},
                        "advertise_pip": {"type": "bool"},
                        "advertise_system_mac": {"type": "bool"},
                        "allow_vni_in_ethertag": {"type": "bool"},
                        "aggregate_address": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "prefix": {"type": "str"},
                                "advertise_map": {"type": "str"},
                                "as_set": {"type": "bool"},
                                "attribute_map": {"type": "str"},
                                "summary_only": {"type": "bool"},
                                "suppress_map": {"type": "str"},
                            },
                        },
                        "client_to_client": {
                            "type": "dict",
                            "options": {"no_reflection": {"type": "bool"}},
                        },
                        "dampen_igp_metric": {"type": "int"},
                        "dampening": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "decay_half_life": {"type": "int"},
                                "start_reuse_route": {"type": "int"},
                                "start_suppress_route": {"type": "int"},
                                "max_suppress_time": {"type": "int"},
                                "route_map": {"type": "str"},
                            },
                        },
                        "default_information": {
                            "type": "dict",
                            "options": {"originate": {"type": "bool"}},
                        },
                        "default_metric": {"type": "int"},
                        "distance": {
                            "type": "dict",
                            "options": {
                                "ebgp_routes": {"type": "int"},
                                "ibgp_routes": {"type": "int"},
                                "local_routes": {"type": "int"},
                            },
                        },
                        "export_gateway_ip": {"type": "bool"},
                        "inject_map": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "route_map": {"type": "str"},
                                "exist_map": {"type": "str"},
                                "copy_attributes": {"type": "bool"},
                            },
                        },
                        "maximum_paths": {
                            "type": "dict",
                            "options": {
                                "parallel_paths": {"type": "int"},
                                "ibgp": {
                                    "type": "dict",
                                    "options": {
                                        "parallel_paths": {"type": "int"}
                                    },
                                },
                                "eibgp": {
                                    "type": "dict",
                                    "options": {
                                        "parallel_paths": {"type": "int"}
                                    },
                                },
                                "local": {
                                    "type": "dict",
                                    "options": {
                                        "parallel_paths": {"type": "int"}
                                    },
                                },
                                "mixed": {
                                    "type": "dict",
                                    "options": {
                                        "parallel_paths": {"type": "int"}
                                    },
                                },
                            },
                        },
                        "networks": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "prefix": {"type": "str"},
                                "route_map": {"type": "str"},
                            },
                        },
                        "nexthop": {
                            "type": "dict",
                            "options": {
                                "route_map": {"type": "str"},
                                "trigger_delay": {
                                    "type": "dict",
                                    "options": {
                                        "critical_delay": {"type": "int"},
                                        "non_critical_delay": {"type": "int"},
                                    },
                                },
                            },
                        },
                        "redistribute": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "protocol": {
                                    "type": "str",
                                    "choices": [
                                        "am",
                                        "direct",
                                        "eigrp",
                                        "isis",
                                        "lisp",
                                        "ospf",
                                        "ospfv3",
                                        "rip",
                                        "static",
                                    ],
                                    "required": True,
                                },
                                "id": {"type": "str"},
                                "route_map": {"type": "str", "required": True},
                            },
                        },
                        "retain": {
                            "type": "dict",
                            "options": {
                                "route_target": {
                                    "type": "dict",
                                    "options": {
                                        "retain_all": {"type": "bool"},
                                        "route_map": {"type": "str"},
                                    },
                                }
                            },
                        },
                        "suppress_inactive": {"type": "bool"},
                        "table_map": {
                            "type": "dict",
                            "options": {
                                "name": {"type": "str", "required": True},
                                "filter": {"type": "bool"},
                            },
                        },
                        "timers": {
                            "type": "dict",
                            "options": {
                                "bestpath_defer": {
                                    "type": "dict",
                                    "options": {
                                        "defer_time": {"type": "int"},
                                        "maximum_defer_time": {"type": "int"},
                                    },
                                }
                            },
                        },
                        "wait_igp_convergence": {"type": "bool"},
                        "vrf": {"type": "str"},
                    },
                },
            },
        },
        "state": {
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
