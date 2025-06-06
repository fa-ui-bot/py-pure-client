# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.2, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    The version of the OpenAPI document: 2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from typing import Set, Dict, Any

from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from pypureclient.flashblade.FB_2_2.models.http import Http
from pypureclient.flashblade.FB_2_2.models.multi_protocol_post import MultiProtocolPost
from pypureclient.flashblade.FB_2_2.models.nfs import Nfs
from pypureclient.flashblade.FB_2_2.models.reference import Reference
from pypureclient.flashblade.FB_2_2.models.smb import Smb


class FileSystemPost(BaseModel):
    """
    FileSystemPost
    """
    default_group_quota: Optional[StrictInt] = Field(default=None, description="The default space quota for a group writing to this file system.")
    default_user_quota: Optional[StrictInt] = Field(default=None, description="The default space quota for a user writing to this file system.")
    fast_remove_directory_enabled: Optional[StrictBool] = Field(default=None, description="If set to `true`, the file system, when mounted, will contain a directory that can be used for fast removal of other directories. Directories can be moved into the fast remove directory in order to have them deleted, and their space freed, more quickly than a normal removal operation. If not specified, defaults to `false`.")
    hard_limit_enabled: Optional[StrictBool] = Field(default=None, description="If set to `true`, the file system's size, as defined by `provisioned`, is used as a hard limit quota. If not specified, defaults to `false`.")
    http: Optional[Http] = Field(default=None, description="HTTP configuration.")
    multi_protocol: Optional[MultiProtocolPost] = Field(default=None, description="Multi-protocol configuration.")
    nfs: Optional[Nfs] = Field(default=None, description="NFS configuration.")
    provisioned: Optional[StrictInt] = Field(default=None, description="The provisioned size of the file system, displayed in bytes. If set to an empty string (`\"\"`), the file system is unlimited in size. If not specified, defaults to unlimited.")
    requested_promotion_state: Optional[StrictStr] = Field(default=None, description="Possible values are `promoted` and `demoted`. The `demoted` state is used for replication targets and is only allowed to be set if the file system is in a replica-link relationship. The additional query param `discard-non-snapshotted-data` must be set to `true` when demoting a file system. The default for new file systems is `promoted`.")
    smb: Optional[Smb] = Field(default=None, description="SMB configuration.")
    snapshot_directory_enabled: Optional[StrictBool] = Field(default=None, description="If set to `true`, a hidden .snapshot directory will be present in each directory of the file system when it is mounted. The .snapshot directory allows clients read access to the contents of the snapshots that have been taken of a directory. If set to `false`, the .snapshot directory will not be present in any directories within a mounted file system. If not specified, defaults to `true`.")
    source: Optional[Reference] = Field(default=None, description="The source snapshot whose data is copied to the file system specified.")
    writable: Optional[StrictBool] = Field(default=None, description="Whether the file system is writable or not. If `false`, this overrides any protocol or file permission settings and prevents changes. If `true`, then the protocol and file permission settings are evaluated. If not specified, defaults to `true`. Modifiable.")
    __properties = ["default_group_quota", "default_user_quota", "fast_remove_directory_enabled", "hard_limit_enabled", "http", "multi_protocol", "nfs", "provisioned", "requested_promotion_state", "smb", "snapshot_directory_enabled", "source", "writable"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.to_dict(include_readonly=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.as_request_dict())

    def as_request_dict(self) -> Dict[str, Any]:
        return self.to_dict(include_readonly=False)

    def to_dict(self, include_readonly: bool=True) -> Dict[str, Any]:

        """Returns the dictionary representation of the model using alias"""
        excluded_fields: Set[str] = set()
        if not include_readonly:
            excluded_fields.update([
                "requested_promotion_state",
            ])
        none_fields: Set[str] = set()
        for _field in self.__fields__.keys():
            if super().__getattribute__(_field) is None:
                none_fields.add(_field)

        _dict = self.dict(by_alias=True, exclude=excluded_fields, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of http
        if _include_in_dict('http', include_readonly, excluded_fields, none_fields):
            _dict['http'] = self.http.to_dict(include_readonly=include_readonly)
        # override the default output from pydantic by calling `to_dict()` of multi_protocol
        if _include_in_dict('multi_protocol', include_readonly, excluded_fields, none_fields):
            _dict['multi_protocol'] = self.multi_protocol.to_dict(include_readonly=include_readonly)
        # override the default output from pydantic by calling `to_dict()` of nfs
        if _include_in_dict('nfs', include_readonly, excluded_fields, none_fields):
            _dict['nfs'] = self.nfs.to_dict(include_readonly=include_readonly)
        # override the default output from pydantic by calling `to_dict()` of smb
        if _include_in_dict('smb', include_readonly, excluded_fields, none_fields):
            _dict['smb'] = self.smb.to_dict(include_readonly=include_readonly)
        # override the default output from pydantic by calling `to_dict()` of source
        if _include_in_dict('source', include_readonly, excluded_fields, none_fields):
            _dict['source'] = self.source.to_dict(include_readonly=include_readonly)
        return _dict

    def __getitem__(self, key):
        return super().__getattribute__(key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __delitem__(self, key):
        setattr(self, key, None)

    def __getattribute__(self, name: str) -> Any:
        _value = super().__getattribute__(name)
        if _value is None and name in self.__fields__.keys() and _should_raise_on_none():
            raise AttributeError
        return _value

    def __str__(self) -> str:
        return self.to_str()

    def __repr__(self) -> str:
        return self.to_str()

    @classmethod
    def from_json(cls, json_str: str) -> FileSystemPost:
        """Create an instance of FileSystemPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> FileSystemPost:
        """Create an instance of FileSystemPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileSystemPost.parse_obj(obj)

        _obj = FileSystemPost.construct(_fields_set=None, **{
            "default_group_quota": obj.get("default_group_quota"),
            "default_user_quota": obj.get("default_user_quota"),
            "fast_remove_directory_enabled": obj.get("fast_remove_directory_enabled"),
            "hard_limit_enabled": obj.get("hard_limit_enabled"),
            "http": Http.from_dict(obj.get("http")) if obj.get("http") is not None else None,
            "multi_protocol": MultiProtocolPost.from_dict(obj.get("multi_protocol")) if obj.get("multi_protocol") is not None else None,
            "nfs": Nfs.from_dict(obj.get("nfs")) if obj.get("nfs") is not None else None,
            "provisioned": obj.get("provisioned"),
            "requested_promotion_state": obj.get("requested_promotion_state"),
            "smb": Smb.from_dict(obj.get("smb")) if obj.get("smb") is not None else None,
            "snapshot_directory_enabled": obj.get("snapshot_directory_enabled"),
            "source": Reference.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "writable": obj.get("writable")
        })
        return _obj

def _should_raise_on_none() -> bool:
    import importlib
    _package = importlib.import_module(__package__)
    return _package._attribute_error_on_none

def _include_in_dict(name: str, include_readonly: bool, excluded_fields: Set[str], none_fields: Set[str]) -> bool:
    if name in none_fields:
        return False
    return (include_readonly or name not in excluded_fields)

