from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_prime_version import AdvisoryPrimeVersion
    from ..models.advisory_zulu_version import AdvisoryZuluVersion


T = TypeVar("T", bound="AdvisoryAzul")


@_attrs_define
class AdvisoryAzul:
    """
    Attributes:
        base_score (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        prime_version (Union[Unset, list['AdvisoryPrimeVersion']]):
        release (Union[Unset, str]):
        url (Union[Unset, str]):
        zulu_version (Union[Unset, list['AdvisoryZuluVersion']]):
    """

    base_score: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    prime_version: Union[Unset, list["AdvisoryPrimeVersion"]] = UNSET
    release: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    zulu_version: Union[Unset, list["AdvisoryZuluVersion"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_score = self.base_score

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        prime_version: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prime_version, Unset):
            prime_version = []
            for prime_version_item_data in self.prime_version:
                prime_version_item = prime_version_item_data.to_dict()
                prime_version.append(prime_version_item)

        release = self.release

        url = self.url

        zulu_version: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.zulu_version, Unset):
            zulu_version = []
            for zulu_version_item_data in self.zulu_version:
                zulu_version_item = zulu_version_item_data.to_dict()
                zulu_version.append(zulu_version_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_score is not UNSET:
            field_dict["base_score"] = base_score
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if prime_version is not UNSET:
            field_dict["prime_version"] = prime_version
        if release is not UNSET:
            field_dict["release"] = release
        if url is not UNSET:
            field_dict["url"] = url
        if zulu_version is not UNSET:
            field_dict["zulu_version"] = zulu_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_prime_version import AdvisoryPrimeVersion
        from ..models.advisory_zulu_version import AdvisoryZuluVersion

        d = dict(src_dict)
        base_score = d.pop("base_score", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        prime_version = []
        _prime_version = d.pop("prime_version", UNSET)
        for prime_version_item_data in _prime_version or []:
            prime_version_item = AdvisoryPrimeVersion.from_dict(prime_version_item_data)

            prime_version.append(prime_version_item)

        release = d.pop("release", UNSET)

        url = d.pop("url", UNSET)

        zulu_version = []
        _zulu_version = d.pop("zulu_version", UNSET)
        for zulu_version_item_data in _zulu_version or []:
            zulu_version_item = AdvisoryZuluVersion.from_dict(zulu_version_item_data)

            zulu_version.append(zulu_version_item)

        advisory_azul = cls(
            base_score=base_score,
            cve=cve,
            date_added=date_added,
            prime_version=prime_version,
            release=release,
            url=url,
            zulu_version=zulu_version,
        )

        advisory_azul.additional_properties = d
        return advisory_azul

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
