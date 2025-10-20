from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_csaf import AdvisoryCSAF


T = TypeVar("T", bound="AdvisoryNCSC")


@_attrs_define
class AdvisoryNCSC:
    """
    Attributes:
        csaf (Union[Unset, AdvisoryCSAF]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        summary_nl (Union[Unset, str]):
        title_nl (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    csaf: Union[Unset, "AdvisoryCSAF"] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    summary_nl: Union[Unset, str] = UNSET
    title_nl: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csaf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.csaf, Unset):
            csaf = self.csaf.to_dict()

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        id = self.id

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        summary_nl = self.summary_nl

        title_nl = self.title_nl

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csaf is not UNSET:
            field_dict["csaf"] = csaf
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if id is not UNSET:
            field_dict["id"] = id
        if references is not UNSET:
            field_dict["references"] = references
        if summary_nl is not UNSET:
            field_dict["summary_nl"] = summary_nl
        if title_nl is not UNSET:
            field_dict["title_nl"] = title_nl
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_csaf import AdvisoryCSAF

        d = dict(src_dict)
        _csaf = d.pop("csaf", UNSET)
        csaf: Union[Unset, AdvisoryCSAF]
        if isinstance(_csaf, Unset):
            csaf = UNSET
        else:
            csaf = AdvisoryCSAF.from_dict(_csaf)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        id = d.pop("id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        summary_nl = d.pop("summary_nl", UNSET)

        title_nl = d.pop("title_nl", UNSET)

        url = d.pop("url", UNSET)

        advisory_ncsc = cls(
            csaf=csaf,
            cve=cve,
            date_added=date_added,
            id=id,
            references=references,
            summary_nl=summary_nl,
            title_nl=title_nl,
            url=url,
        )

        advisory_ncsc.additional_properties = d
        return advisory_ncsc

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
