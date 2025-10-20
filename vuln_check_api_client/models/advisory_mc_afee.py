from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_mc_afee_score import AdvisoryMcAfeeScore


T = TypeVar("T", bound="AdvisoryMcAfee")


@_attrs_define
class AdvisoryMcAfee:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        mcafee_score (Union[Unset, list['AdvisoryMcAfeeScore']]):
        summary (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    mcafee_score: Union[Unset, list["AdvisoryMcAfeeScore"]] = UNSET
    summary: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        mcafee_score: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mcafee_score, Unset):
            mcafee_score = []
            for mcafee_score_item_data in self.mcafee_score:
                mcafee_score_item = mcafee_score_item_data.to_dict()
                mcafee_score.append(mcafee_score_item)

        summary = self.summary

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
        if mcafee_score is not UNSET:
            field_dict["mcafee_score"] = mcafee_score
        if summary is not UNSET:
            field_dict["summary"] = summary
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_mc_afee_score import AdvisoryMcAfeeScore

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        mcafee_score = []
        _mcafee_score = d.pop("mcafee_score", UNSET)
        for mcafee_score_item_data in _mcafee_score or []:
            mcafee_score_item = AdvisoryMcAfeeScore.from_dict(mcafee_score_item_data)

            mcafee_score.append(mcafee_score_item)

        summary = d.pop("summary", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_mc_afee = cls(
            cve=cve,
            date_added=date_added,
            mcafee_score=mcafee_score,
            summary=summary,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_mc_afee.additional_properties = d
        return advisory_mc_afee

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
