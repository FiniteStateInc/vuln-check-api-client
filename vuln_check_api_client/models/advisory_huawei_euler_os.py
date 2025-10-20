from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryHuaweiEulerOS")


@_attrs_define
class AdvisoryHuaweiEulerOS:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        packages (Union[Unset, str]):
        products (Union[Unset, list[str]]):
        severity (Union[Unset, str]):
        synopsis (Union[Unset, str]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    packages: Union[Unset, str] = UNSET
    products: Union[Unset, list[str]] = UNSET
    severity: Union[Unset, str] = UNSET
    synopsis: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        id = self.id

        packages = self.packages

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        severity = self.severity

        synopsis = self.synopsis

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if packages is not UNSET:
            field_dict["packages"] = packages
        if products is not UNSET:
            field_dict["products"] = products
        if severity is not UNSET:
            field_dict["severity"] = severity
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        packages = d.pop("packages", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        severity = d.pop("severity", UNSET)

        synopsis = d.pop("synopsis", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_huawei_euler_os = cls(
            cve=cve,
            date_added=date_added,
            description=description,
            id=id,
            packages=packages,
            products=products,
            severity=severity,
            synopsis=synopsis,
            title=title,
            url=url,
        )

        advisory_huawei_euler_os.additional_properties = d
        return advisory_huawei_euler_os

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
