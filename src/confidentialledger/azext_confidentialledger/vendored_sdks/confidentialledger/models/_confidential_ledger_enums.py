# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CheckNameAvailabilityReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason why the given name is not available.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class LedgerRoleName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """LedgerRole associated with the Security Principal of Ledger
    """

    READER = "Reader"
    CONTRIBUTOR = "Contributor"
    ADMINISTRATOR = "Administrator"

class LedgerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the ledger. Private means transaction data is encrypted.
    """

    UNKNOWN = "Unknown"
    PUBLIC = "Public"
    PRIVATE = "Private"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Object representing ProvisioningState for Confidential Ledger.
    """

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"
