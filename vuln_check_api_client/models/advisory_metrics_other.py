from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_metrics_other_content import AdvisoryMetricsOtherContent


T = TypeVar("T", bound="AdvisoryMetricsOther")


@_attrs_define
class AdvisoryMetricsOther:
    """
    Attributes:
        content (Union[Unset, AdvisoryMetricsOtherContent]):
        type_ (Union[Unset, str]):
    """

    content: Union[Unset, "AdvisoryMetricsOtherContent"] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_metrics_other_content import AdvisoryMetricsOtherContent

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: Union[Unset, AdvisoryMetricsOtherContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = AdvisoryMetricsOtherContent.from_dict(_content)

        type_ = d.pop("type", UNSET)

        advisory_metrics_other = cls(
            content=content,
            type_=type_,
        )

        advisory_metrics_other.additional_properties = d
        return advisory_metrics_other

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
