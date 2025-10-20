from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryPrimeVersion")


@_attrs_define
class AdvisoryPrimeVersion:
    """
    Attributes:
        jd_k (Union[Unset, str]):
        prime (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    jd_k: Union[Unset, str] = UNSET
    prime: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jd_k = self.jd_k

        prime = self.prime

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jd_k is not UNSET:
            field_dict["jdK"] = jd_k
        if prime is not UNSET:
            field_dict["prime"] = prime
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jd_k = d.pop("jdK", UNSET)

        prime = d.pop("prime", UNSET)

        type_ = d.pop("type", UNSET)

        advisory_prime_version = cls(
            jd_k=jd_k,
            prime=prime,
            type_=type_,
        )

        advisory_prime_version.additional_properties = d
        return advisory_prime_version

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
