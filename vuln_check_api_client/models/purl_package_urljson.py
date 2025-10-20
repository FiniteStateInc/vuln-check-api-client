from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.purl_qualifier_json import PurlQualifierJSON


T = TypeVar("T", bound="PurlPackageURLJSON")


@_attrs_define
class PurlPackageURLJSON:
    """
    Attributes:
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
        qualifiers (Union[Unset, list['PurlQualifierJSON']]):
        subpath (Union[Unset, str]):
        type_ (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    qualifiers: Union[Unset, list["PurlQualifierJSON"]] = UNSET
    subpath: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace = self.namespace

        qualifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.qualifiers, Unset):
            qualifiers = []
            for qualifiers_item_data in self.qualifiers:
                qualifiers_item = qualifiers_item_data.to_dict()
                qualifiers.append(qualifiers_item)

        subpath = self.subpath

        type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if qualifiers is not UNSET:
            field_dict["qualifiers"] = qualifiers
        if subpath is not UNSET:
            field_dict["subpath"] = subpath
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.purl_qualifier_json import PurlQualifierJSON

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        qualifiers = []
        _qualifiers = d.pop("qualifiers", UNSET)
        for qualifiers_item_data in _qualifiers or []:
            qualifiers_item = PurlQualifierJSON.from_dict(qualifiers_item_data)

            qualifiers.append(qualifiers_item)

        subpath = d.pop("subpath", UNSET)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        purl_package_urljson = cls(
            name=name,
            namespace=namespace,
            qualifiers=qualifiers,
            subpath=subpath,
            type_=type_,
            version=version,
        )

        purl_package_urljson.additional_properties = d
        return purl_package_urljson

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
