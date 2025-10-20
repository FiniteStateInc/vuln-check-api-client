from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_oss_package_artifacts import ApiOSSPackageArtifacts
    from ..models.api_oss_package_research_attributes import ApiOSSPackageResearchAttributes
    from ..models.api_oss_package_vulnerability import ApiOSSPackageVulnerability


T = TypeVar("T", bound="ApiOSSPackage")


@_attrs_define
class ApiOSSPackage:
    """
    Attributes:
        artifacts (Union[Unset, ApiOSSPackageArtifacts]):
        cves (Union[Unset, list[str]]):
        licenses (Union[Unset, list[str]]):
        name (Union[Unset, str]):
        published_date (Union[Unset, str]):
        purl (Union[Unset, list[str]]):
        research_attributes (Union[Unset, ApiOSSPackageResearchAttributes]):
        version (Union[Unset, str]):
        vulnerabilities (Union[Unset, list['ApiOSSPackageVulnerability']]):
    """

    artifacts: Union[Unset, "ApiOSSPackageArtifacts"] = UNSET
    cves: Union[Unset, list[str]] = UNSET
    licenses: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    published_date: Union[Unset, str] = UNSET
    purl: Union[Unset, list[str]] = UNSET
    research_attributes: Union[Unset, "ApiOSSPackageResearchAttributes"] = UNSET
    version: Union[Unset, str] = UNSET
    vulnerabilities: Union[Unset, list["ApiOSSPackageVulnerability"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifacts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artifacts, Unset):
            artifacts = self.artifacts.to_dict()

        cves: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cves, Unset):
            cves = self.cves

        licenses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = self.licenses

        name = self.name

        published_date = self.published_date

        purl: Union[Unset, list[str]] = UNSET
        if not isinstance(self.purl, Unset):
            purl = self.purl

        research_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.research_attributes, Unset):
            research_attributes = self.research_attributes.to_dict()

        version = self.version

        vulnerabilities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = vulnerabilities_item_data.to_dict()
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifacts is not UNSET:
            field_dict["artifacts"] = artifacts
        if cves is not UNSET:
            field_dict["cves"] = cves
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if name is not UNSET:
            field_dict["name"] = name
        if published_date is not UNSET:
            field_dict["published_date"] = published_date
        if purl is not UNSET:
            field_dict["purl"] = purl
        if research_attributes is not UNSET:
            field_dict["research_attributes"] = research_attributes
        if version is not UNSET:
            field_dict["version"] = version
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_oss_package_artifacts import ApiOSSPackageArtifacts
        from ..models.api_oss_package_research_attributes import ApiOSSPackageResearchAttributes
        from ..models.api_oss_package_vulnerability import ApiOSSPackageVulnerability

        d = dict(src_dict)
        _artifacts = d.pop("artifacts", UNSET)
        artifacts: Union[Unset, ApiOSSPackageArtifacts]
        if isinstance(_artifacts, Unset):
            artifacts = UNSET
        else:
            artifacts = ApiOSSPackageArtifacts.from_dict(_artifacts)

        cves = cast(list[str], d.pop("cves", UNSET))

        licenses = cast(list[str], d.pop("licenses", UNSET))

        name = d.pop("name", UNSET)

        published_date = d.pop("published_date", UNSET)

        purl = cast(list[str], d.pop("purl", UNSET))

        _research_attributes = d.pop("research_attributes", UNSET)
        research_attributes: Union[Unset, ApiOSSPackageResearchAttributes]
        if isinstance(_research_attributes, Unset):
            research_attributes = UNSET
        else:
            research_attributes = ApiOSSPackageResearchAttributes.from_dict(_research_attributes)

        version = d.pop("version", UNSET)

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = ApiOSSPackageVulnerability.from_dict(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        api_oss_package = cls(
            artifacts=artifacts,
            cves=cves,
            licenses=licenses,
            name=name,
            published_date=published_date,
            purl=purl,
            research_attributes=research_attributes,
            version=version,
            vulnerabilities=vulnerabilities,
        )

        api_oss_package.additional_properties = d
        return api_oss_package

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
