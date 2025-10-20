from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_ssa_source import AdvisorySSASource


T = TypeVar("T", bound="AdvisorySiemensAdvisory")


@_attrs_define
class AdvisorySiemensAdvisory:
    """
    Attributes:
        csaf_url (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        cvrf_url (Union[Unset, str]):
        date_added (Union[Unset, str]):
        html_url (Union[Unset, str]):
        id (Union[Unset, str]):
        last_update (Union[Unset, str]): could potentially kill this in the future as it's a dupe
        pdf_url (Union[Unset, str]):
        products (Union[Unset, list[str]]):
        ssa (Union[Unset, AdvisorySSASource]):
        tags (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        txt_url (Union[Unset, str]):
        updated_at (Union[Unset, str]):
    """

    csaf_url: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvrf_url: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    html_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_update: Union[Unset, str] = UNSET
    pdf_url: Union[Unset, str] = UNSET
    products: Union[Unset, list[str]] = UNSET
    ssa: Union[Unset, "AdvisorySSASource"] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    txt_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        csaf_url = self.csaf_url

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvrf_url = self.cvrf_url

        date_added = self.date_added

        html_url = self.html_url

        id = self.id

        last_update = self.last_update

        pdf_url = self.pdf_url

        products: Union[Unset, list[str]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products

        ssa: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ssa, Unset):
            ssa = self.ssa.to_dict()

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title

        txt_url = self.txt_url

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csaf_url is not UNSET:
            field_dict["csaf_url"] = csaf_url
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvrf_url is not UNSET:
            field_dict["cvrf_url"] = cvrf_url
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if html_url is not UNSET:
            field_dict["html_url"] = html_url
        if id is not UNSET:
            field_dict["id"] = id
        if last_update is not UNSET:
            field_dict["last_update"] = last_update
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if products is not UNSET:
            field_dict["products"] = products
        if ssa is not UNSET:
            field_dict["ssa"] = ssa
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if txt_url is not UNSET:
            field_dict["txt_url"] = txt_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_ssa_source import AdvisorySSASource

        d = dict(src_dict)
        csaf_url = d.pop("csaf_url", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        cvrf_url = d.pop("cvrf_url", UNSET)

        date_added = d.pop("date_added", UNSET)

        html_url = d.pop("html_url", UNSET)

        id = d.pop("id", UNSET)

        last_update = d.pop("last_update", UNSET)

        pdf_url = d.pop("pdf_url", UNSET)

        products = cast(list[str], d.pop("products", UNSET))

        _ssa = d.pop("ssa", UNSET)
        ssa: Union[Unset, AdvisorySSASource]
        if isinstance(_ssa, Unset):
            ssa = UNSET
        else:
            ssa = AdvisorySSASource.from_dict(_ssa)

        tags = cast(list[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        txt_url = d.pop("txt_url", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        advisory_siemens_advisory = cls(
            csaf_url=csaf_url,
            cve=cve,
            cvrf_url=cvrf_url,
            date_added=date_added,
            html_url=html_url,
            id=id,
            last_update=last_update,
            pdf_url=pdf_url,
            products=products,
            ssa=ssa,
            tags=tags,
            title=title,
            txt_url=txt_url,
            updated_at=updated_at,
        )

        advisory_siemens_advisory.additional_properties = d
        return advisory_siemens_advisory

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
