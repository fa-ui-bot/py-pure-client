# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.14
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from typing import Set, Dict, Any

from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from pypureclient.flasharray.FA_2_14.models.fixed_reference_with_type import FixedReferenceWithType


class PolicyRuleNfsClient(BaseModel):
    """
    PolicyRuleNfsClient
    """
    access: Optional[StrictStr] = Field(default=None, description="Specifies access control for the export. Valid values are `root-squash` and `no-root-squash`. The default is `root-squash` if not specified.")
    client: Optional[StrictStr] = Field(default=None, description="Specifies the clients that will be permitted to access the export. Accepted notation includes IP, IP mask, or hostname. The default is `*` if not specified.")
    name: Optional[StrictStr] = Field(default=None, description="Name of this rule. The name is automatically generated by the system.")
    permission: Optional[StrictStr] = Field(default=None, description="Specifies which read-write client access permissions are allowed for the export. Valid values are `rw` and `ro`. The default is `rw` if not specified.")
    policy: Optional[FixedReferenceWithType] = Field(default=None, description="The policy to which this rule belongs.")
    __properties = ["access", "client", "name", "permission", "policy"]

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
                "access",
                "client",
                "name",
                "permission",
            ])
        none_fields: Set[str] = set()
        for _field in self.__fields__.keys():
            if super().__getattribute__(_field) is None:
                none_fields.add(_field)

        _dict = self.dict(by_alias=True, exclude=excluded_fields, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy
        if _include_in_dict('policy', include_readonly, excluded_fields, none_fields):
            _dict['policy'] = self.policy.to_dict(include_readonly=include_readonly)
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
    def from_json(cls, json_str: str) -> PolicyRuleNfsClient:
        """Create an instance of PolicyRuleNfsClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyRuleNfsClient:
        """Create an instance of PolicyRuleNfsClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyRuleNfsClient.parse_obj(obj)

        _obj = PolicyRuleNfsClient.construct(_fields_set=None, **{
            "access": obj.get("access"),
            "client": obj.get("client"),
            "name": obj.get("name"),
            "permission": obj.get("permission"),
            "policy": FixedReferenceWithType.from_dict(obj.get("policy")) if obj.get("policy") is not None else None
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

