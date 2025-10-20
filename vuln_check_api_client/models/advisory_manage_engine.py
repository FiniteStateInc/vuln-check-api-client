from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_cve_details_link import AdvisoryCVEDetailsLink
    from ..models.advisory_me_product import AdvisoryMEProduct
    from ..models.advisory_product_specific_detail import AdvisoryProductSpecificDetail


T = TypeVar("T", bound="AdvisoryManageEngine")


@_attrs_define
class AdvisoryManageEngine:
    """
    Attributes:
        advisory (Union[Unset, str]):
        added_time (Union[Unset, str]):
        cve_details_link (Union[Unset, AdvisoryCVEDetailsLink]):
        cve_id (Union[Unset, str]):
        cvss_severity_rating (Union[Unset, str]):
        fixed (Union[Unset, str]):
        for_product_search (Union[Unset, str]):
        id (Union[Unset, str]):
        product (Union[Unset, AdvisoryMEProduct]):
        product_list (Union[Unset, list['AdvisoryMEProduct']]):
        product_specific_details (Union[Unset, list['AdvisoryProductSpecificDetail']]):
        summary (Union[Unset, str]):
        version (Union[Unset, str]):
        index_field (Union[Unset, str]):
    """

    advisory: Union[Unset, str] = UNSET
    added_time: Union[Unset, str] = UNSET
    cve_details_link: Union[Unset, "AdvisoryCVEDetailsLink"] = UNSET
    cve_id: Union[Unset, str] = UNSET
    cvss_severity_rating: Union[Unset, str] = UNSET
    fixed: Union[Unset, str] = UNSET
    for_product_search: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    product: Union[Unset, "AdvisoryMEProduct"] = UNSET
    product_list: Union[Unset, list["AdvisoryMEProduct"]] = UNSET
    product_specific_details: Union[Unset, list["AdvisoryProductSpecificDetail"]] = UNSET
    summary: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    index_field: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advisory = self.advisory

        added_time = self.added_time

        cve_details_link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cve_details_link, Unset):
            cve_details_link = self.cve_details_link.to_dict()

        cve_id = self.cve_id

        cvss_severity_rating = self.cvss_severity_rating

        fixed = self.fixed

        for_product_search = self.for_product_search

        id = self.id

        product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        product_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_list, Unset):
            product_list = []
            for product_list_item_data in self.product_list:
                product_list_item = product_list_item_data.to_dict()
                product_list.append(product_list_item)

        product_specific_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.product_specific_details, Unset):
            product_specific_details = []
            for product_specific_details_item_data in self.product_specific_details:
                product_specific_details_item = product_specific_details_item_data.to_dict()
                product_specific_details.append(product_specific_details_item)

        summary = self.summary

        version = self.version

        index_field = self.index_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advisory is not UNSET:
            field_dict["ADVISORY"] = advisory
        if added_time is not UNSET:
            field_dict["Added_Time"] = added_time
        if cve_details_link is not UNSET:
            field_dict["CVE_Details_Link"] = cve_details_link
        if cve_id is not UNSET:
            field_dict["CVE_ID"] = cve_id
        if cvss_severity_rating is not UNSET:
            field_dict["CVSS_Severity_Rating"] = cvss_severity_rating
        if fixed is not UNSET:
            field_dict["Fixed"] = fixed
        if for_product_search is not UNSET:
            field_dict["For_product_search"] = for_product_search
        if id is not UNSET:
            field_dict["ID"] = id
        if product is not UNSET:
            field_dict["Product"] = product
        if product_list is not UNSET:
            field_dict["Product_list"] = product_list
        if product_specific_details is not UNSET:
            field_dict["Product_specific_details"] = product_specific_details
        if summary is not UNSET:
            field_dict["Summary"] = summary
        if version is not UNSET:
            field_dict["Version"] = version
        if index_field is not UNSET:
            field_dict["index_field"] = index_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_cve_details_link import AdvisoryCVEDetailsLink
        from ..models.advisory_me_product import AdvisoryMEProduct
        from ..models.advisory_product_specific_detail import AdvisoryProductSpecificDetail

        d = dict(src_dict)
        advisory = d.pop("ADVISORY", UNSET)

        added_time = d.pop("Added_Time", UNSET)

        _cve_details_link = d.pop("CVE_Details_Link", UNSET)
        cve_details_link: Union[Unset, AdvisoryCVEDetailsLink]
        if isinstance(_cve_details_link, Unset):
            cve_details_link = UNSET
        else:
            cve_details_link = AdvisoryCVEDetailsLink.from_dict(_cve_details_link)

        cve_id = d.pop("CVE_ID", UNSET)

        cvss_severity_rating = d.pop("CVSS_Severity_Rating", UNSET)

        fixed = d.pop("Fixed", UNSET)

        for_product_search = d.pop("For_product_search", UNSET)

        id = d.pop("ID", UNSET)

        _product = d.pop("Product", UNSET)
        product: Union[Unset, AdvisoryMEProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AdvisoryMEProduct.from_dict(_product)

        product_list = []
        _product_list = d.pop("Product_list", UNSET)
        for product_list_item_data in _product_list or []:
            product_list_item = AdvisoryMEProduct.from_dict(product_list_item_data)

            product_list.append(product_list_item)

        product_specific_details = []
        _product_specific_details = d.pop("Product_specific_details", UNSET)
        for product_specific_details_item_data in _product_specific_details or []:
            product_specific_details_item = AdvisoryProductSpecificDetail.from_dict(product_specific_details_item_data)

            product_specific_details.append(product_specific_details_item)

        summary = d.pop("Summary", UNSET)

        version = d.pop("Version", UNSET)

        index_field = d.pop("index_field", UNSET)

        advisory_manage_engine = cls(
            advisory=advisory,
            added_time=added_time,
            cve_details_link=cve_details_link,
            cve_id=cve_id,
            cvss_severity_rating=cvss_severity_rating,
            fixed=fixed,
            for_product_search=for_product_search,
            id=id,
            product=product,
            product_list=product_list,
            product_specific_details=product_specific_details,
            summary=summary,
            version=version,
            index_field=index_field,
        )

        advisory_manage_engine.additional_properties = d
        return advisory_manage_engine

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
