# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AutoUpgradePolicyResource(Model):
    """Cosmos DB resource auto-upgrade policy.

    :param throughput_policy: Represents throughput policy which service must
     adhere to for auto-upgrade
    :type throughput_policy:
     ~azure.mgmt.cosmosdb.models.ThroughputPolicyResource
    """

    _attribute_map = {
        'throughput_policy': {'key': 'throughputPolicy', 'type': 'ThroughputPolicyResource'},
    }

    def __init__(self, **kwargs):
        super(AutoUpgradePolicyResource, self).__init__(**kwargs)
        self.throughput_policy = kwargs.get('throughput_policy', None)
