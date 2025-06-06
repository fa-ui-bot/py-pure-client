# coding: utf-8

"""
    Pure1 Public REST API

    Pure1 Public REST API, developed by [Pure Storage, Inc.](https://www.purestorage.com)   The Pure1 REST API 2.0 offers one single form of authentication: OAuth 2.0 via the [Token Exchange protocol](https://datatracker.ietf.org/doc/draft-ietf-oauth-token-exchange).  OAuth 2.0 is an open protocol to allow secure authorization in a simple and standard method from web, mobile, desktop and background applications.  Note that the [Authentication](#section/Authentication) section below mentions 'API Key' as the security scheme type. This is solely for the purpose of allowing testing this API with [Swagger UI](https://static.pure1.purestorage.com/api-swagger/index.html).  [Knowledge base reference documentation](https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference)

    The version of the OpenAPI document: 1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from typing import Set, Dict, Any

from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist
from pypureclient.pure1.Pure1_1_4.models.fixed_reference import FixedReference
from pypureclient.pure1.Pure1_1_4.models.fixed_reference_fqdn import FixedReferenceFqdn


class Volume(BaseModel):
    """
    Volume
    """
    as_of: Optional[StrictInt] = Field(default=None, alias="_as_of", description="The freshness of the data (timestamp in millis since epoch).")
    id: Optional[StrictStr] = Field(default=None, description="A non-modifiable, globally unique ID chosen by the system.")
    name: Optional[StrictStr] = Field(default=None, description="A modifiable, locally unique name chosen by the user.")
    arrays: Optional[conlist(FixedReferenceFqdn)] = Field(default=None, description="The list of arrays where this resource exists. Many resources are on a single array, but some resources, such as pods, can be shared across multiple arrays.")
    created: Optional[StrictInt] = Field(default=None, description="Creation time in milliseconds since UNIX epoch.")
    destroyed: Optional[StrictBool] = Field(default=None, description="Whether this volume has been destroyed or not.")
    eradicated: Optional[StrictBool] = Field(default=None, description="Whether this volume has been eradicated or not.")
    pod: Optional[FixedReference] = Field(default=None, description="A reference to the pod this volume belongs to, if applicable.")
    provisioned: Optional[conint(strict=True, le=4503599627370496, ge=1048576)] = Field(default=None, description="Provisioned size of the volume in bytes.")
    serial: Optional[StrictStr] = Field(default=None, description="Serial number generated by Purity when the volume was created.")
    source: Optional[FixedReference] = Field(default=None, description="A reference to the volume this volume was cloned from, if applicable.")
    __properties = ["_as_of", "id", "name", "arrays", "created", "destroyed", "eradicated", "pod", "provisioned", "serial", "source"]

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
                "as_of",
                "id",
                "arrays",
                "created",
                "destroyed",
                "eradicated",
                "serial",
            ])
        none_fields: Set[str] = set()
        for _field in self.__fields__.keys():
            if super().__getattribute__(_field) is None:
                none_fields.add(_field)

        _dict = self.dict(by_alias=True, exclude=excluded_fields, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in arrays (list)
        if _include_in_dict('arrays', include_readonly, excluded_fields, none_fields):
            _items = []
            for _item in self.arrays:
                if _item:
                    _items.append(_item.to_dict(include_readonly=include_readonly))
            _dict['arrays'] = _items
        # override the default output from pydantic by calling `to_dict()` of pod
        if _include_in_dict('pod', include_readonly, excluded_fields, none_fields):
            _dict['pod'] = self.pod.to_dict(include_readonly=include_readonly)
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
    def from_json(cls, json_str: str) -> Volume:
        """Create an instance of Volume from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    @classmethod
    def from_dict(cls, obj: dict) -> Volume:
        """Create an instance of Volume from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Volume.parse_obj(obj)

        _obj = Volume.construct(_fields_set=None, **{
            "as_of": obj.get("_as_of"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "arrays": [FixedReferenceFqdn.from_dict(_item) for _item in obj.get("arrays")] if obj.get("arrays") is not None else None,
            "created": obj.get("created"),
            "destroyed": obj.get("destroyed"),
            "eradicated": obj.get("eradicated"),
            "pod": FixedReference.from_dict(obj.get("pod")) if obj.get("pod") is not None else None,
            "provisioned": obj.get("provisioned"),
            "serial": obj.get("serial"),
            "source": FixedReference.from_dict(obj.get("source")) if obj.get("source") is not None else None
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

