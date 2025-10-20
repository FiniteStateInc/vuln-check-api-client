from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cvssv2 import AdvisoryCVSSV2
    from ..models.advisory_cvssv3 import AdvisoryCVSSV3


T = TypeVar("T", bound="AdvisoryCSAFScore")


@_attrs_define
class AdvisoryCSAFScore:
    """
    Attributes:
        cvss_v2 (Union[Unset, AdvisoryCVSSV2]):
        cvss_v3 (Union[Unset, AdvisoryCVSSV3]):
        products (Union[Unset, list[str]]):
    """

    cvss_v2: Union[Unset, "AdvisoryCVSSV2"] = UNSET
    cvss_v3: Union[Unset, "AdvisoryCVSSV3"] = UNSET
    products: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cvss_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v2, Unset):
            cvss_v2 = self.cvss_v2.to_dict()

        cvss_v3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss_v3, Unset):
            cvss_v3 = self.cvss_v3.to_dict()

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cvss_v2 is not UNSET:
            field_dict["cvss_v2"] = cvss_v2
        if cvss_v3 is not UNSET:
            field_dict["cvss_v3"] = cvss_v3
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cvssv2 import AdvisoryCVSSV2
        from ..models.advisory_cvssv3 import AdvisoryCVSSV3

        d = dict(src_dict)
        _cvss_v2 = d.pop("cvss_v2", UNSET)
        cvss_v2: Union[Unset, AdvisoryCVSSV2]
        if isinstance(_cvss_v2, Unset):
            cvss_v2 = UNSET
        else:
            cvss_v2 = AdvisoryCVSSV2.from_dict(_cvss_v2)

        _cvss_v3 = d.pop("cvss_v3", UNSET)
        cvss_v3: Union[Unset, AdvisoryCVSSV3]
        if isinstance(_cvss_v3, Unset):
            cvss_v3 = UNSET
        else:
            cvss_v3 = AdvisoryCVSSV3.from_dict(_cvss_v3)

        products = cast(list[str], d.pop("products", UNSET))

        advisory_csaf_score = cls(
            cvss_v2=cvss_v2,
            cvss_v3=cvss_v3,
            products=products,
        )

        advisory_csaf_score.additional_properties = d
        return advisory_csaf_score

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
