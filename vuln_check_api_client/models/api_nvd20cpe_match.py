from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_nvd20cpe_name import ApiNVD20CPEName


T = TypeVar("T", bound="ApiNVD20CPEMatch")


@_attrs_define
class ApiNVD20CPEMatch:
    """
    Attributes:
        cpe_last_modified (Union[Unset, str]):
        created (Union[Unset, str]):
        criteria (Union[Unset, str]):
        last_modified (Union[Unset, str]):
        match_criteria_id (Union[Unset, str]):
        matches (Union[Unset, list['ApiNVD20CPEName']]):
        status (Union[Unset, str]):
        version_end_excluding (Union[Unset, str]):
        version_end_including (Union[Unset, str]):
        version_start_excluding (Union[Unset, str]):
        version_start_including (Union[Unset, str]):
    """

    cpe_last_modified: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    criteria: Union[Unset, str] = UNSET
    last_modified: Union[Unset, str] = UNSET
    match_criteria_id: Union[Unset, str] = UNSET
    matches: Union[Unset, list["ApiNVD20CPEName"]] = UNSET
    status: Union[Unset, str] = UNSET
    version_end_excluding: Union[Unset, str] = UNSET
    version_end_including: Union[Unset, str] = UNSET
    version_start_excluding: Union[Unset, str] = UNSET
    version_start_including: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpe_last_modified = self.cpe_last_modified

        created = self.created

        criteria = self.criteria

        last_modified = self.last_modified

        match_criteria_id = self.match_criteria_id

        matches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        status = self.status

        version_end_excluding = self.version_end_excluding

        version_end_including = self.version_end_including

        version_start_excluding = self.version_start_excluding

        version_start_including = self.version_start_including

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpe_last_modified is not UNSET:
            field_dict["cpeLastModified"] = cpe_last_modified
        if created is not UNSET:
            field_dict["created"] = created
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if match_criteria_id is not UNSET:
            field_dict["matchCriteriaId"] = match_criteria_id
        if matches is not UNSET:
            field_dict["matches"] = matches
        if status is not UNSET:
            field_dict["status"] = status
        if version_end_excluding is not UNSET:
            field_dict["versionEndExcluding"] = version_end_excluding
        if version_end_including is not UNSET:
            field_dict["versionEndIncluding"] = version_end_including
        if version_start_excluding is not UNSET:
            field_dict["versionStartExcluding"] = version_start_excluding
        if version_start_including is not UNSET:
            field_dict["versionStartIncluding"] = version_start_including

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_nvd20cpe_name import ApiNVD20CPEName

        d = dict(src_dict)
        cpe_last_modified = d.pop("cpeLastModified", UNSET)

        created = d.pop("created", UNSET)

        criteria = d.pop("criteria", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        match_criteria_id = d.pop("matchCriteriaId", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = ApiNVD20CPEName.from_dict(matches_item_data)

            matches.append(matches_item)

        status = d.pop("status", UNSET)

        version_end_excluding = d.pop("versionEndExcluding", UNSET)

        version_end_including = d.pop("versionEndIncluding", UNSET)

        version_start_excluding = d.pop("versionStartExcluding", UNSET)

        version_start_including = d.pop("versionStartIncluding", UNSET)

        api_nvd20cpe_match = cls(
            cpe_last_modified=cpe_last_modified,
            created=created,
            criteria=criteria,
            last_modified=last_modified,
            match_criteria_id=match_criteria_id,
            matches=matches,
            status=status,
            version_end_excluding=version_end_excluding,
            version_end_including=version_end_including,
            version_start_excluding=version_start_excluding,
            version_start_including=version_start_including,
        )

        api_nvd20cpe_match.additional_properties = d
        return api_nvd20cpe_match

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
