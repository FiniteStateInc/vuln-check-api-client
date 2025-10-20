from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_zdi_product import AdvisoryZDIProduct
    from ..models.advisory_zdi_response import AdvisoryZDIResponse


T = TypeVar("T", bound="AdvisoryZDI")


@_attrs_define
class AdvisoryZDI:
    """
    Attributes:
        cves (Union[Unset, list[str]]):
        cvss_score (Union[Unset, str]):
        cvss_vector (Union[Unset, str]):
        cvss_version (Union[Unset, str]):
        discoverers (Union[Unset, list[str]]):
        filter_ids_dv (Union[Unset, list[str]]):
        last_updated_at (Union[Unset, str]):
        products (Union[Unset, list['AdvisoryZDIProduct']]):
        public_advisory (Union[Unset, str]):
        published_date (Union[Unset, str]):
        responses (Union[Unset, list['AdvisoryZDIResponse']]):
        title (Union[Unset, str]):
        zdi_can (Union[Unset, str]):
        zdi_public (Union[Unset, str]):
    """

    cves: Union[Unset, list[str]] = UNSET
    cvss_score: Union[Unset, str] = UNSET
    cvss_vector: Union[Unset, str] = UNSET
    cvss_version: Union[Unset, str] = UNSET
    discoverers: Union[Unset, list[str]] = UNSET
    filter_ids_dv: Union[Unset, list[str]] = UNSET
    last_updated_at: Union[Unset, str] = UNSET
    products: Union[Unset, list["AdvisoryZDIProduct"]] = UNSET
    public_advisory: Union[Unset, str] = UNSET
    published_date: Union[Unset, str] = UNSET
    responses: Union[Unset, list["AdvisoryZDIResponse"]] = UNSET
    title: Union[Unset, str] = UNSET
    zdi_can: Union[Unset, str] = UNSET
    zdi_public: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        cvss_score = self.cvss_score

        cvss_vector = self.cvss_vector

        cvss_version = self.cvss_version

        discoverers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.discoverers, Unset):
            discoverers = self.discoverers

        filter_ids_dv: Union[Unset, list[str]] = UNSET
        if not isinstance(self.filter_ids_dv, Unset):
            filter_ids_dv = self.filter_ids_dv

        last_updated_at = self.last_updated_at

        products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        public_advisory = self.public_advisory

        published_date = self.published_date

        responses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        title = self.title

        zdi_can = self.zdi_can

        zdi_public = self.zdi_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cves is not UNSET:
            field_dict["cves"] = cves
        if cvss_score is not UNSET:
            field_dict["cvss_score"] = cvss_score
        if cvss_vector is not UNSET:
            field_dict["cvss_vector"] = cvss_vector
        if cvss_version is not UNSET:
            field_dict["cvss_version"] = cvss_version
        if discoverers is not UNSET:
            field_dict["discoverers"] = discoverers
        if filter_ids_dv is not UNSET:
            field_dict["filter_ids_dv"] = filter_ids_dv
        if last_updated_at is not UNSET:
            field_dict["last_updated_at"] = last_updated_at
        if products is not UNSET:
            field_dict["products"] = products
        if public_advisory is not UNSET:
            field_dict["public_advisory"] = public_advisory
        if published_date is not UNSET:
            field_dict["published_date"] = published_date
        if responses is not UNSET:
            field_dict["responses"] = responses
        if title is not UNSET:
            field_dict["title"] = title
        if zdi_can is not UNSET:
            field_dict["zdi_can"] = zdi_can
        if zdi_public is not UNSET:
            field_dict["zdi_public"] = zdi_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_zdi_product import AdvisoryZDIProduct
        from ..models.advisory_zdi_response import AdvisoryZDIResponse

        d = dict(src_dict)
        cves = cast(list[str], d.pop("cves", UNSET))

        cvss_score = d.pop("cvss_score", UNSET)

        cvss_vector = d.pop("cvss_vector", UNSET)

        cvss_version = d.pop("cvss_version", UNSET)

        discoverers = cast(list[str], d.pop("discoverers", UNSET))

        filter_ids_dv = cast(list[str], d.pop("filter_ids_dv", UNSET))

        last_updated_at = d.pop("last_updated_at", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = AdvisoryZDIProduct.from_dict(products_item_data)

            products.append(products_item)

        public_advisory = d.pop("public_advisory", UNSET)

        published_date = d.pop("published_date", UNSET)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = AdvisoryZDIResponse.from_dict(responses_item_data)

            responses.append(responses_item)

        title = d.pop("title", UNSET)

        zdi_can = d.pop("zdi_can", UNSET)

        zdi_public = d.pop("zdi_public", UNSET)

        advisory_zdi = cls(
            cves=cves,
            cvss_score=cvss_score,
            cvss_vector=cvss_vector,
            cvss_version=cvss_version,
            discoverers=discoverers,
            filter_ids_dv=filter_ids_dv,
            last_updated_at=last_updated_at,
            products=products,
            public_advisory=public_advisory,
            published_date=published_date,
            responses=responses,
            title=title,
            zdi_can=zdi_can,
            zdi_public=zdi_public,
        )

        advisory_zdi.additional_properties = d
        return advisory_zdi

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
