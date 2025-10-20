from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_itw import AdvisoryITW
    from ..models.advisory_mscvrf import AdvisoryMSCVRF


T = TypeVar("T", bound="AdvisoryMicrosoftCVRF")


@_attrs_define
class AdvisoryMicrosoftCVRF:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cvrf (Union[Unset, AdvisoryMSCVRF]):
        date_added (Union[Unset, str]):
        exploited_list (Union[Unset, list['AdvisoryITW']]):
        title (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cvrf: Union[Unset, "AdvisoryMSCVRF"] = UNSET
    date_added: Union[Unset, str] = UNSET
    exploited_list: Union[Unset, list["AdvisoryITW"]] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvrf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvrf, Unset):
            cvrf = self.cvrf.to_dict()

        date_added = self.date_added

        exploited_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exploited_list, Unset):
            exploited_list = []
            for exploited_list_item_data in self.exploited_list:
                exploited_list_item = exploited_list_item_data.to_dict()
                exploited_list.append(exploited_list_item)

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvrf is not UNSET:
            field_dict["cvrf"] = cvrf
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if exploited_list is not UNSET:
            field_dict["exploited_list"] = exploited_list
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_itw import AdvisoryITW
        from ..models.advisory_mscvrf import AdvisoryMSCVRF

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        _cvrf = d.pop("cvrf", UNSET)
        cvrf: Union[Unset, AdvisoryMSCVRF]
        if isinstance(_cvrf, Unset):
            cvrf = UNSET
        else:
            cvrf = AdvisoryMSCVRF.from_dict(_cvrf)

        date_added = d.pop("date_added", UNSET)

        exploited_list = []
        _exploited_list = d.pop("exploited_list", UNSET)
        for exploited_list_item_data in _exploited_list or []:
            exploited_list_item = AdvisoryITW.from_dict(exploited_list_item_data)

            exploited_list.append(exploited_list_item)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        advisory_microsoft_cvrf = cls(
            cve=cve,
            cvrf=cvrf,
            date_added=date_added,
            exploited_list=exploited_list,
            title=title,
            url=url,
        )

        advisory_microsoft_cvrf.additional_properties = d
        return advisory_microsoft_cvrf

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
