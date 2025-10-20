from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_enisa_id_product import AdvisoryEnisaIDProduct
    from ..models.advisory_enisa_id_vendor import AdvisoryEnisaIDVendor


T = TypeVar("T", bound="AdvisoryEUVD")


@_attrs_define
class AdvisoryEUVD:
    """
    Attributes:
        aliases (Union[Unset, list[str]]):
        assigner (Union[Unset, str]):
        base_score (Union[Unset, float]):
        base_score_vector (Union[Unset, str]):
        base_score_version (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        date_updated (Union[Unset, str]):
        description (Union[Unset, str]):
        enisa_id_product (Union[Unset, list['AdvisoryEnisaIDProduct']]):
        enisa_id_vendor (Union[Unset, list['AdvisoryEnisaIDVendor']]):
        epss (Union[Unset, float]):
        exploited (Union[Unset, bool]): This field is exploited field from endpoint /api/vulnerabilities.
            apidocs : https://euvd.enisa.europa.eu/apidoc
            Note: There are records where exploited_since is populated with a valid date,
            but it still shows up under non_exploitable data set
        exploited_since (Union[Unset, str]):
        id (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        url (Union[Unset, str]):
    """

    aliases: Union[Unset, list[str]] = UNSET
    assigner: Union[Unset, str] = UNSET
    base_score: Union[Unset, float] = UNSET
    base_score_vector: Union[Unset, str] = UNSET
    base_score_version: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    date_updated: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enisa_id_product: Union[Unset, list["AdvisoryEnisaIDProduct"]] = UNSET
    enisa_id_vendor: Union[Unset, list["AdvisoryEnisaIDVendor"]] = UNSET
    epss: Union[Unset, float] = UNSET
    exploited: Union[Unset, bool] = UNSET
    exploited_since: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        assigner = self.assigner

        base_score = self.base_score

        base_score_vector = self.base_score_vector

        base_score_version = self.base_score_version

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        date_updated = self.date_updated

        description = self.description

        enisa_id_product: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enisa_id_product, Unset):
            enisa_id_product = []
            for enisa_id_product_item_data in self.enisa_id_product:
                enisa_id_product_item = enisa_id_product_item_data.to_dict()
                enisa_id_product.append(enisa_id_product_item)

        enisa_id_vendor: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.enisa_id_vendor, Unset):
            enisa_id_vendor = []
            for enisa_id_vendor_item_data in self.enisa_id_vendor:
                enisa_id_vendor_item = enisa_id_vendor_item_data.to_dict()
                enisa_id_vendor.append(enisa_id_vendor_item)

        epss = self.epss

        exploited = self.exploited

        exploited_since = self.exploited_since

        id = self.id

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if assigner is not UNSET:
            field_dict["assigner"] = assigner
        if base_score is not UNSET:
            field_dict["base_score"] = base_score
        if base_score_vector is not UNSET:
            field_dict["base_score_vector"] = base_score_vector
        if base_score_version is not UNSET:
            field_dict["base_score_version"] = base_score_version
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if description is not UNSET:
            field_dict["description"] = description
        if enisa_id_product is not UNSET:
            field_dict["enisa_id_product"] = enisa_id_product
        if enisa_id_vendor is not UNSET:
            field_dict["enisa_id_vendor"] = enisa_id_vendor
        if epss is not UNSET:
            field_dict["epss"] = epss
        if exploited is not UNSET:
            field_dict["exploited"] = exploited
        if exploited_since is not UNSET:
            field_dict["exploited_since"] = exploited_since
        if id is not UNSET:
            field_dict["id"] = id
        if references is not UNSET:
            field_dict["references"] = references
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_enisa_id_product import AdvisoryEnisaIDProduct
        from ..models.advisory_enisa_id_vendor import AdvisoryEnisaIDVendor

        d = dict(src_dict)
        aliases = cast(list[str], d.pop("aliases", UNSET))

        assigner = d.pop("assigner", UNSET)

        base_score = d.pop("base_score", UNSET)

        base_score_vector = d.pop("base_score_vector", UNSET)

        base_score_version = d.pop("base_score_version", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        description = d.pop("description", UNSET)

        enisa_id_product = []
        _enisa_id_product = d.pop("enisa_id_product", UNSET)
        for enisa_id_product_item_data in _enisa_id_product or []:
            enisa_id_product_item = AdvisoryEnisaIDProduct.from_dict(enisa_id_product_item_data)

            enisa_id_product.append(enisa_id_product_item)

        enisa_id_vendor = []
        _enisa_id_vendor = d.pop("enisa_id_vendor", UNSET)
        for enisa_id_vendor_item_data in _enisa_id_vendor or []:
            enisa_id_vendor_item = AdvisoryEnisaIDVendor.from_dict(enisa_id_vendor_item_data)

            enisa_id_vendor.append(enisa_id_vendor_item)

        epss = d.pop("epss", UNSET)

        exploited = d.pop("exploited", UNSET)

        exploited_since = d.pop("exploited_since", UNSET)

        id = d.pop("id", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        url = d.pop("url", UNSET)

        advisory_euvd = cls(
            aliases=aliases,
            assigner=assigner,
            base_score=base_score,
            base_score_vector=base_score_vector,
            base_score_version=base_score_version,
            cve=cve,
            date_added=date_added,
            date_updated=date_updated,
            description=description,
            enisa_id_product=enisa_id_product,
            enisa_id_vendor=enisa_id_vendor,
            epss=epss,
            exploited=exploited,
            exploited_since=exploited_since,
            id=id,
            references=references,
            url=url,
        )

        advisory_euvd.additional_properties = d
        return advisory_euvd

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
