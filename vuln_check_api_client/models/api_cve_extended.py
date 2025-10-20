from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_categorization_extended import ApiCategorizationExtended
    from ..models.api_cve_data_meta_extended import ApiCVEDataMetaExtended
    from ..models.api_description import ApiDescription
    from ..models.api_problem_type_extended import ApiProblemTypeExtended
    from ..models.api_references_extended import ApiReferencesExtended


T = TypeVar("T", bound="ApiCVEExtended")


@_attrs_define
class ApiCVEExtended:
    """
    Attributes:
        cve_data_meta (Union[Unset, ApiCVEDataMetaExtended]):
        categorization (Union[Unset, ApiCategorizationExtended]):
        data_format (Union[Unset, str]):
        data_type (Union[Unset, str]):
        data_version (Union[Unset, str]):
        description (Union[Unset, ApiDescription]):
        problemtype (Union[Unset, ApiProblemTypeExtended]):
        references (Union[Unset, ApiReferencesExtended]):
    """

    cve_data_meta: Union[Unset, "ApiCVEDataMetaExtended"] = UNSET
    categorization: Union[Unset, "ApiCategorizationExtended"] = UNSET
    data_format: Union[Unset, str] = UNSET
    data_type: Union[Unset, str] = UNSET
    data_version: Union[Unset, str] = UNSET
    description: Union[Unset, "ApiDescription"] = UNSET
    problemtype: Union[Unset, "ApiProblemTypeExtended"] = UNSET
    references: Union[Unset, "ApiReferencesExtended"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve_data_meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve_data_meta, Unset):
            cve_data_meta = self.cve_data_meta.to_dict()

        categorization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.categorization, Unset):
            categorization = self.categorization.to_dict()

        data_format = self.data_format

        data_type = self.data_type

        data_version = self.data_version

        description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        problemtype: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.problemtype, Unset):
            problemtype = self.problemtype.to_dict()

        references: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve_data_meta is not UNSET:
            field_dict["CVE_data_meta"] = cve_data_meta
        if categorization is not UNSET:
            field_dict["categorization"] = categorization
        if data_format is not UNSET:
            field_dict["data_format"] = data_format
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if data_version is not UNSET:
            field_dict["data_version"] = data_version
        if description is not UNSET:
            field_dict["description"] = description
        if problemtype is not UNSET:
            field_dict["problemtype"] = problemtype
        if references is not UNSET:
            field_dict["references"] = references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_categorization_extended import ApiCategorizationExtended
        from ..models.api_cve_data_meta_extended import ApiCVEDataMetaExtended
        from ..models.api_description import ApiDescription
        from ..models.api_problem_type_extended import ApiProblemTypeExtended
        from ..models.api_references_extended import ApiReferencesExtended

        d = dict(src_dict)
        _cve_data_meta = d.pop("CVE_data_meta", UNSET)
        cve_data_meta: Union[Unset, ApiCVEDataMetaExtended]
        if isinstance(_cve_data_meta, Unset):
            cve_data_meta = UNSET
        else:
            cve_data_meta = ApiCVEDataMetaExtended.from_dict(_cve_data_meta)

        _categorization = d.pop("categorization", UNSET)
        categorization: Union[Unset, ApiCategorizationExtended]
        if isinstance(_categorization, Unset):
            categorization = UNSET
        else:
            categorization = ApiCategorizationExtended.from_dict(_categorization)

        data_format = d.pop("data_format", UNSET)

        data_type = d.pop("data_type", UNSET)

        data_version = d.pop("data_version", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, ApiDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = ApiDescription.from_dict(_description)

        _problemtype = d.pop("problemtype", UNSET)
        problemtype: Union[Unset, ApiProblemTypeExtended]
        if isinstance(_problemtype, Unset):
            problemtype = UNSET
        else:
            problemtype = ApiProblemTypeExtended.from_dict(_problemtype)

        _references = d.pop("references", UNSET)
        references: Union[Unset, ApiReferencesExtended]
        if isinstance(_references, Unset):
            references = UNSET
        else:
            references = ApiReferencesExtended.from_dict(_references)

        api_cve_extended = cls(
            cve_data_meta=cve_data_meta,
            categorization=categorization,
            data_format=data_format,
            data_type=data_type,
            data_version=data_version,
            description=description,
            problemtype=problemtype,
            references=references,
        )

        api_cve_extended.additional_properties = d
        return api_cve_extended

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
