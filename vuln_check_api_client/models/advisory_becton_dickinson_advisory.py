from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_products_affected import AdvisoryProductsAffected


T = TypeVar("T", bound="AdvisoryBectonDickinsonAdvisory")


@_attrs_define
class AdvisoryBectonDickinsonAdvisory:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        products_affected (Union[Unset, list['AdvisoryProductsAffected']]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    products_affected: Union[Unset, list["AdvisoryProductsAffected"]] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        products_affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products_affected, Unset):
            products_affected = []
            for products_affected_item_data in self.products_affected:
                products_affected_item = products_affected_item_data.to_dict()
                products_affected.append(products_affected_item)

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if products_affected is not UNSET:
            field_dict["products_affected"] = products_affected
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_products_affected import AdvisoryProductsAffected

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        products_affected = []
        _products_affected = d.pop("products_affected", UNSET)
        for products_affected_item_data in _products_affected or []:
            products_affected_item = AdvisoryProductsAffected.from_dict(products_affected_item_data)

            products_affected.append(products_affected_item)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_becton_dickinson_advisory = cls(
            cve=cve,
            date_added=date_added,
            products_affected=products_affected,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_becton_dickinson_advisory.additional_properties = d
        return advisory_becton_dickinson_advisory

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
