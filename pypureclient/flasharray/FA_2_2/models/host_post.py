# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from typing import Set, Dict, Any

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pypureclient.flasharray.FA_2_2.models.chap import Chap
from pypureclient.flasharray.FA_2_2.models.reference import Reference


class HostPost(BaseModel):
    """
    HostPost
    """
    chap: Optional[Chap] = None
    iqns: Optional[conlist(StrictStr)] = Field(default=None, description="The iSCSI qualified name (IQN) associated with the host.")
    nqns: Optional[conlist(StrictStr)] = Field(default=None, description="The NVMe Qualified Name (NQN) associated with the host.")
    personality: Optional[StrictStr] = Field(default=None, description="Determines how the system tunes the array to ensure that it works optimally with the host. Set `personality` to the name of the host operating system or virtual memory system. Valid values are `aix`, `esxi`, `hitachi-vsp`, `hpux`, `oracle-vm-server`, `solaris`, and `vms`. If your system is not listed as one of the valid host personalities, do not set the option. By default, the personality is not set.")
    preferred_arrays: Optional[conlist(Reference)] = Field(default=None, description="For synchronous replication configurations, sets a host's preferred array to specify which array exposes active/optimized paths to that host. Enter multiple preferred arrays in comma-separated format. If a preferred array is set for a host, then the other arrays in the same pod will expose active/non-optimized paths to that host. If the host is in a host group, `preferred_arrays` cannot be set because host groups have their own preferred arrays. On a preferred array of a certain host, all the paths on all the ports (for both the primary and secondary controllers) are set up as A/O (active/optimized) paths, while on a non-preferred array, all the paths are A/N (Active/Non-optimized) paths.")
    wwns: Optional[conlist(StrictStr)] = Field(default=None, description="The Fibre Channel World Wide Name (WWN) associated with the host.")
    __properties = ["chap", "iqns", "nqns", "personality", "preferred_arrays", "wwns"]

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
            ])
        none_fields: Set[str] = set()
        for _field in self.__fields__.keys():
            if super().__getattribute__(_field) is None:
                none_fields.add(_field)

        _dict = self.dict(by_alias=True, exclude=excluded_fields, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of chap
        if _include_in_dict('chap', include_readonly, excluded_fields, none_fields):
            _dict['chap'] = self.chap.to_dict(include_readonly=include_readonly)
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_arrays (list)
        if _include_in_dict('preferred_arrays', include_readonly, excluded_fields, none_fields):
            _items = []
            for _item in self.preferred_arrays:
                if _item:
                    _items.append(_item.to_dict(include_readonly=include_readonly))
            _dict['preferred_arrays'] = _items
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
    def from_json(cls, json_str: str) -> HostPost:
        """Create an instance of HostPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> HostPost:
        """Create an instance of HostPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HostPost.parse_obj(obj)

        _obj = HostPost.construct(_fields_set=None, **{
            "chap": Chap.from_dict(obj.get("chap")) if obj.get("chap") is not None else None,
            "iqns": obj.get("iqns"),
            "nqns": obj.get("nqns"),
            "personality": obj.get("personality"),
            "preferred_arrays": [Reference.from_dict(_item) for _item in obj.get("preferred_arrays")] if obj.get("preferred_arrays") is not None else None,
            "wwns": obj.get("wwns")
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

