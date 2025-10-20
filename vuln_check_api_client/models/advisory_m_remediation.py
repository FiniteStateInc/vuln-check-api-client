from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_affected_file import AdvisoryAffectedFile
    from ..models.advisory_i_val import AdvisoryIVal


T = TypeVar("T", bound="AdvisoryMRemediation")


@_attrs_define
class AdvisoryMRemediation:
    """
    Attributes:
        affected_files (Union[Unset, list['AdvisoryAffectedFile']]):
        date (Union[Unset, str]):
        date_specified (Union[Unset, bool]):
        description (Union[Unset, AdvisoryIVal]):
        fixed_build (Union[Unset, str]):
        product_id (Union[Unset, list[str]]):
        restart_required (Union[Unset, AdvisoryIVal]):
        sub_type (Union[Unset, str]):
        type_ (Union[Unset, int]): diff
        url (Union[Unset, str]):
        supercedence (Union[Unset, str]):
    """

    affected_files: Union[Unset, list["AdvisoryAffectedFile"]] = UNSET
    date: Union[Unset, str] = UNSET
    date_specified: Union[Unset, bool] = UNSET
    description: Union[Unset, "AdvisoryIVal"] = UNSET
    fixed_build: Union[Unset, str] = UNSET
    product_id: Union[Unset, list[str]] = UNSET
    restart_required: Union[Unset, "AdvisoryIVal"] = UNSET
    sub_type: Union[Unset, str] = UNSET
    type_: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    supercedence: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.affected_files, Unset):
            affected_files = []
            for affected_files_item_data in self.affected_files:
                affected_files_item = affected_files_item_data.to_dict()
                affected_files.append(affected_files_item)

        date = self.date

        date_specified = self.date_specified

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        fixed_build = self.fixed_build

        product_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = self.product_id

        restart_required: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restart_required, Unset):
            restart_required = self.restart_required.to_dict()

        sub_type = self.sub_type

        type_ = self.type_

        url = self.url

        supercedence = self.supercedence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_files is not UNSET:
            field_dict["AffectedFiles"] = affected_files
        if date is not UNSET:
            field_dict["Date"] = date
        if date_specified is not UNSET:
            field_dict["DateSpecified"] = date_specified
        if description is not UNSET:
            field_dict["Description"] = description
        if fixed_build is not UNSET:
            field_dict["FixedBuild"] = fixed_build
        if product_id is not UNSET:
            field_dict["ProductID"] = product_id
        if restart_required is not UNSET:
            field_dict["RestartRequired"] = restart_required
        if sub_type is not UNSET:
            field_dict["SubType"] = sub_type
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if url is not UNSET:
            field_dict["Url"] = url
        if supercedence is not UNSET:
            field_dict["supercedence"] = supercedence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_affected_file import AdvisoryAffectedFile
        from ..models.advisory_i_val import AdvisoryIVal

        d = dict(src_dict)
        affected_files = []
        _affected_files = d.pop("AffectedFiles", UNSET)
        for affected_files_item_data in _affected_files or []:
            affected_files_item = AdvisoryAffectedFile.from_dict(affected_files_item_data)

            affected_files.append(affected_files_item)

        date = d.pop("Date", UNSET)

        date_specified = d.pop("DateSpecified", UNSET)

        _description = d.pop("Description", UNSET)
        description: Union[Unset, AdvisoryIVal]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = AdvisoryIVal.from_dict(_description)

        fixed_build = d.pop("FixedBuild", UNSET)

        product_id = cast(list[str], d.pop("ProductID", UNSET))

        _restart_required = d.pop("RestartRequired", UNSET)
        restart_required: Union[Unset, AdvisoryIVal]
        if isinstance(_restart_required, Unset):
            restart_required = UNSET
        else:
            restart_required = AdvisoryIVal.from_dict(_restart_required)

        sub_type = d.pop("SubType", UNSET)

        type_ = d.pop("Type", UNSET)

        url = d.pop("Url", UNSET)

        supercedence = d.pop("supercedence", UNSET)

        advisory_m_remediation = cls(
            affected_files=affected_files,
            date=date,
            date_specified=date_specified,
            description=description,
            fixed_build=fixed_build,
            product_id=product_id,
            restart_required=restart_required,
            sub_type=sub_type,
            type_=type_,
            url=url,
            supercedence=supercedence,
        )

        advisory_m_remediation.additional_properties = d
        return advisory_m_remediation

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
