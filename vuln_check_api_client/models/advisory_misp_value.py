from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_misp_meta import AdvisoryMispMeta
    from ..models.advisory_misp_related_item import AdvisoryMispRelatedItem


T = TypeVar("T", bound="AdvisoryMispValue")


@_attrs_define
class AdvisoryMispValue:
    """
    Attributes:
        description (Union[Unset, str]):
        meta (Union[Unset, AdvisoryMispMeta]):
        related (Union[Unset, list['AdvisoryMispRelatedItem']]):
        uuid (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    meta: Union[Unset, "AdvisoryMispMeta"] = UNSET
    related: Union[Unset, list["AdvisoryMispRelatedItem"]] = UNSET
    uuid: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        related: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related, Unset):
            related = []
            for related_item_data in self.related:
                related_item = related_item_data.to_dict()
                related.append(related_item)

        uuid = self.uuid

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if meta is not UNSET:
            field_dict["meta"] = meta
        if related is not UNSET:
            field_dict["related"] = related
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_misp_meta import AdvisoryMispMeta
        from ..models.advisory_misp_related_item import AdvisoryMispRelatedItem

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, AdvisoryMispMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = AdvisoryMispMeta.from_dict(_meta)

        related = []
        _related = d.pop("related", UNSET)
        for related_item_data in _related or []:
            related_item = AdvisoryMispRelatedItem.from_dict(related_item_data)

            related.append(related_item)

        uuid = d.pop("uuid", UNSET)

        value = d.pop("value", UNSET)

        advisory_misp_value = cls(
            description=description,
            meta=meta,
            related=related,
            uuid=uuid,
            value=value,
        )

        advisory_misp_value.additional_properties = d
        return advisory_misp_value

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
