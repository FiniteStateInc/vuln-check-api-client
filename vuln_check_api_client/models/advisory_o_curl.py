from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_curl_affected import AdvisoryCurlAffected
    from ..models.advisory_curl_credit import AdvisoryCurlCredit
    from ..models.advisory_db_specific import AdvisoryDBSpecific


T = TypeVar("T", bound="AdvisoryOCurl")


@_attrs_define
class AdvisoryOCurl:
    """
    Attributes:
        affected (Union[Unset, list['AdvisoryCurlAffected']]):
        aliases (Union[Unset, list[str]]):
        credits_ (Union[Unset, list['AdvisoryCurlCredit']]):
        database_specific (Union[Unset, AdvisoryDBSpecific]):
        details (Union[Unset, str]):
        id (Union[Unset, str]):
        modified (Union[Unset, str]):
        published (Union[Unset, str]):
        schema_version (Union[Unset, str]):
        summary (Union[Unset, str]):
    """

    affected: Union[Unset, list["AdvisoryCurlAffected"]] = UNSET
    aliases: Union[Unset, list[str]] = UNSET
    credits_: Union[Unset, list["AdvisoryCurlCredit"]] = UNSET
    database_specific: Union[Unset, "AdvisoryDBSpecific"] = UNSET
    details: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    modified: Union[Unset, str] = UNSET
    published: Union[Unset, str] = UNSET
    schema_version: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected, Unset):
            affected = []
            for affected_item_data in self.affected:
                affected_item = affected_item_data.to_dict()
                affected.append(affected_item)

        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        credits_: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.credits_, Unset):
            credits_ = []
            for credits_item_data in self.credits_:
                credits_item = credits_item_data.to_dict()
                credits_.append(credits_item)

        database_specific: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.database_specific, Unset):
            database_specific = self.database_specific.to_dict()

        details = self.details

        id = self.id

        modified = self.modified

        published = self.published

        schema_version = self.schema_version

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected is not UNSET:
            field_dict["affected"] = affected
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if database_specific is not UNSET:
            field_dict["database_specific"] = database_specific
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if modified is not UNSET:
            field_dict["modified"] = modified
        if published is not UNSET:
            field_dict["published"] = published
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_curl_affected import AdvisoryCurlAffected
        from ..models.advisory_curl_credit import AdvisoryCurlCredit
        from ..models.advisory_db_specific import AdvisoryDBSpecific

        d = dict(src_dict)
        affected = []
        _affected = d.pop("affected", UNSET)
        for affected_item_data in _affected or []:
            affected_item = AdvisoryCurlAffected.from_dict(affected_item_data)

            affected.append(affected_item)

        aliases = cast(list[str], d.pop("aliases", UNSET))

        credits_ = []
        _credits_ = d.pop("credits", UNSET)
        for credits_item_data in _credits_ or []:
            credits_item = AdvisoryCurlCredit.from_dict(credits_item_data)

            credits_.append(credits_item)

        _database_specific = d.pop("database_specific", UNSET)
        database_specific: Union[Unset, AdvisoryDBSpecific]
        if isinstance(_database_specific, Unset):
            database_specific = UNSET
        else:
            database_specific = AdvisoryDBSpecific.from_dict(_database_specific)

        details = d.pop("details", UNSET)

        id = d.pop("id", UNSET)

        modified = d.pop("modified", UNSET)

        published = d.pop("published", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        summary = d.pop("summary", UNSET)

        advisory_o_curl = cls(
            affected=affected,
            aliases=aliases,
            credits_=credits_,
            database_specific=database_specific,
            details=details,
            id=id,
            modified=modified,
            published=published,
            schema_version=schema_version,
            summary=summary,
        )

        advisory_o_curl.additional_properties = d
        return advisory_o_curl

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
