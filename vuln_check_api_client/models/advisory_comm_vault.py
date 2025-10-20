from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_comm_vault_cve_details import AdvisoryCommVaultCVEDetails
    from ..models.advisory_comm_vault_impacted_product import AdvisoryCommVaultImpactedProduct
    from ..models.advisory_comm_vault_resolution import AdvisoryCommVaultResolution


T = TypeVar("T", bound="AdvisoryCommVault")


@_attrs_define
class AdvisoryCommVault:
    """
    Attributes:
        cve (Union[Unset, list[str]]):
        cve_details (Union[Unset, list['AdvisoryCommVaultCVEDetails']]):
        cvss_range (Union[Unset, str]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        impacted_product (Union[Unset, AdvisoryCommVaultImpactedProduct]):
        references (Union[Unset, list[str]]):
        resolution (Union[Unset, AdvisoryCommVaultResolution]):
        severity (Union[Unset, str]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    cve: Union[Unset, list[str]] = UNSET
    cve_details: Union[Unset, list["AdvisoryCommVaultCVEDetails"]] = UNSET
    cvss_range: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    impacted_product: Union[Unset, "AdvisoryCommVaultImpactedProduct"] = UNSET
    references: Union[Unset, list[str]] = UNSET
    resolution: Union[Unset, "AdvisoryCommVaultResolution"] = UNSET
    severity: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cve_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cve_details, Unset):
            cve_details = []
            for cve_details_item_data in self.cve_details:
                cve_details_item = cve_details_item_data.to_dict()
                cve_details.append(cve_details_item)

        cvss_range = self.cvss_range

        date_added = self.date_added

        description = self.description

        id = self.id

        impacted_product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.impacted_product, Unset):
            impacted_product = self.impacted_product.to_dict()

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        resolution: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()

        severity = self.severity

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cve_details is not UNSET:
            field_dict["cve_details"] = cve_details
        if cvss_range is not UNSET:
            field_dict["cvss_range"] = cvss_range
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if impacted_product is not UNSET:
            field_dict["impacted_product"] = impacted_product
        if references is not UNSET:
            field_dict["references"] = references
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if severity is not UNSET:
            field_dict["severity"] = severity
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_comm_vault_cve_details import AdvisoryCommVaultCVEDetails
        from ..models.advisory_comm_vault_impacted_product import AdvisoryCommVaultImpactedProduct
        from ..models.advisory_comm_vault_resolution import AdvisoryCommVaultResolution

        d = dict(src_dict)
        cve = cast(list[str], d.pop("cve", UNSET))

        cve_details = []
        _cve_details = d.pop("cve_details", UNSET)
        for cve_details_item_data in _cve_details or []:
            cve_details_item = AdvisoryCommVaultCVEDetails.from_dict(cve_details_item_data)

            cve_details.append(cve_details_item)

        cvss_range = d.pop("cvss_range", UNSET)

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _impacted_product = d.pop("impacted_product", UNSET)
        impacted_product: Union[Unset, AdvisoryCommVaultImpactedProduct]
        if isinstance(_impacted_product, Unset):
            impacted_product = UNSET
        else:
            impacted_product = AdvisoryCommVaultImpactedProduct.from_dict(_impacted_product)

        references = cast(list[str], d.pop("references", UNSET))

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, AdvisoryCommVaultResolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = AdvisoryCommVaultResolution.from_dict(_resolution)

        severity = d.pop("severity", UNSET)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_comm_vault = cls(
            cve=cve,
            cve_details=cve_details,
            cvss_range=cvss_range,
            date_added=date_added,
            description=description,
            id=id,
            impacted_product=impacted_product,
            references=references,
            resolution=resolution,
            severity=severity,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        advisory_comm_vault.additional_properties = d
        return advisory_comm_vault

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
