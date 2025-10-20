from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_m_identification import AdvisoryMIdentification
    from ..models.advisory_r_revision import AdvisoryRRevision


T = TypeVar("T", bound="AdvisoryMDocumentTracking")


@_attrs_define
class AdvisoryMDocumentTracking:
    """
    Attributes:
        current_release_date (Union[Unset, str]):
        initial_release_date (Union[Unset, str]):
        identification (Union[Unset, AdvisoryMIdentification]):
        revisionhistory (Union[Unset, list['AdvisoryRRevision']]): diff in xml/json
        status (Union[Unset, int]): again - change in json/xml
        version (Union[Unset, str]):
    """

    current_release_date: Union[Unset, str] = UNSET
    initial_release_date: Union[Unset, str] = UNSET
    identification: Union[Unset, "AdvisoryMIdentification"] = UNSET
    revisionhistory: Union[Unset, list["AdvisoryRRevision"]] = UNSET
    status: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_release_date = self.current_release_date

        initial_release_date = self.initial_release_date

        identification: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.identification, Unset):
            identification = self.identification.to_dict()

        revisionhistory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.revisionhistory, Unset):
            revisionhistory = []
            for revisionhistory_item_data in self.revisionhistory:
                revisionhistory_item = revisionhistory_item_data.to_dict()
                revisionhistory.append(revisionhistory_item)

        status = self.status

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_release_date is not UNSET:
            field_dict["CurrentReleaseDate"] = current_release_date
        if initial_release_date is not UNSET:
            field_dict["InitialReleaseDate"] = initial_release_date
        if identification is not UNSET:
            field_dict["identification"] = identification
        if revisionhistory is not UNSET:
            field_dict["revisionhistory"] = revisionhistory
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_m_identification import AdvisoryMIdentification
        from ..models.advisory_r_revision import AdvisoryRRevision

        d = dict(src_dict)
        current_release_date = d.pop("CurrentReleaseDate", UNSET)

        initial_release_date = d.pop("InitialReleaseDate", UNSET)

        _identification = d.pop("identification", UNSET)
        identification: Union[Unset, AdvisoryMIdentification]
        if isinstance(_identification, Unset):
            identification = UNSET
        else:
            identification = AdvisoryMIdentification.from_dict(_identification)

        revisionhistory = []
        _revisionhistory = d.pop("revisionhistory", UNSET)
        for revisionhistory_item_data in _revisionhistory or []:
            revisionhistory_item = AdvisoryRRevision.from_dict(revisionhistory_item_data)

            revisionhistory.append(revisionhistory_item)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        advisory_m_document_tracking = cls(
            current_release_date=current_release_date,
            initial_release_date=initial_release_date,
            identification=identification,
            revisionhistory=revisionhistory,
            status=status,
            version=version,
        )

        advisory_m_document_tracking.additional_properties = d
        return advisory_m_document_tracking

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
