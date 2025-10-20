from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_correction import AdvisoryCorrection


T = TypeVar("T", bound="AdvisoryAdvisory")


@_attrs_define
class AdvisoryAdvisory:
    """
    Attributes:
        affects (Union[Unset, str]):
        announced (Union[Unset, str]):
        category (Union[Unset, str]):
        corrections (Union[Unset, list['AdvisoryCorrection']]):
        credits_ (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        module (Union[Unset, str]):
        name (Union[Unset, str]):
        topic (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    affects: Union[Unset, str] = UNSET
    announced: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    corrections: Union[Unset, list["AdvisoryCorrection"]] = UNSET
    credits_: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    module: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affects = self.affects

        announced = self.announced

        category = self.category

        corrections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.corrections, Unset):
            corrections = []
            for corrections_item_data in self.corrections:
                corrections_item = corrections_item_data.to_dict()
                corrections.append(corrections_item)

        credits_ = self.credits_

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        module = self.module

        name = self.name

        topic = self.topic

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affects is not UNSET:
            field_dict["affects"] = affects
        if announced is not UNSET:
            field_dict["announced"] = announced
        if category is not UNSET:
            field_dict["category"] = category
        if corrections is not UNSET:
            field_dict["corrections"] = corrections
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
        if topic is not UNSET:
            field_dict["topic"] = topic
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_correction import AdvisoryCorrection

        d = dict(src_dict)
        affects = d.pop("affects", UNSET)

        announced = d.pop("announced", UNSET)

        category = d.pop("category", UNSET)

        corrections = []
        _corrections = d.pop("corrections", UNSET)
        for corrections_item_data in _corrections or []:
            corrections_item = AdvisoryCorrection.from_dict(corrections_item_data)

            corrections.append(corrections_item)

        credits_ = d.pop("credits", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        module = d.pop("module", UNSET)

        name = d.pop("name", UNSET)

        topic = d.pop("topic", UNSET)

        url = d.pop("url", UNSET)

        advisory_advisory = cls(
            affects=affects,
            announced=announced,
            category=category,
            corrections=corrections,
            credits_=credits_,
            cve=cve,
            date_added=date_added,
            module=module,
            name=name,
            topic=topic,
            url=url,
        )

        advisory_advisory.additional_properties = d
        return advisory_advisory

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
