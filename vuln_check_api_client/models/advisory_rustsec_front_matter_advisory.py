from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryRustsecFrontMatterAdvisory")


@_attrs_define
class AdvisoryRustsecFrontMatterAdvisory:
    """
    Attributes:
        aliases (Union[Unset, list[str]]): Vulnerability aliases, e.g. CVE IDs (optional but recommended)
            Request a CVE for your RustSec vulns: https://iwantacve.org/
        categories (Union[Unset, list[str]]): Optional: Categories this advisory falls under. Valid categories are:
            "code-execution", "crypto-failure", "denial-of-service", "file-disclosure"
            "format-injection", "memory-corruption", "memory-exposure", "privilege-escalation"
        cvss (Union[Unset, str]): Optional: a Common Vulnerability Scoring System score. More information
            can be found on the CVSS website, https://www.first.org/cvss/.
        date (Union[Unset, str]): Disclosure date of the advisory as an RFC 3339 date (mandatory)
        informational (Union[Unset, str]): Optional: Indicates the type of informational security  advisory
             - "unsound" for soundness issues
             - "unmaintained" for crates that are no longer maintained
             - "notice" for other informational notices
        keywords (Union[Unset, list[str]]): Freeform keywords which describe this vulnerability, similar to Cargo
            (optional)
        package (Union[Unset, str]): Name of the affected crate (mandatory)
        references (Union[Unset, list[str]]): URL to additional helpful references regarding the advisory (optional)
        related (Union[Unset, list[str]]): Related vulnerabilities (optional)
            e.g. CVE for a C library wrapped by a -sys crate)
        rustsec_id (Union[Unset, str]): Identifier for the advisory (mandatory). Will be assigned a "RUSTSEC-YYYY-NNNN"
            identifier e.g. RUSTSEC-2018-0001. Please use "RUSTSEC-0000-0000" in PRs.
        url (Union[Unset, str]): URL to a long-form description of this issue, e.g. a GitHub issue/PR,
            a change log entry, or a blogpost announcing the release (optional)
        withdrawn (Union[Unset, str]): Whether the advisory is withdrawn (optional)
    """

    aliases: Union[Unset, list[str]] = UNSET
    categories: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    informational: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    package: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    related: Union[Unset, list[str]] = UNSET
    rustsec_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    withdrawn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        cvss = self.cvss

        date = self.date

        informational = self.informational

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        package = self.package

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        related: Union[Unset, list[str]] = UNSET
        if not isinstance(self.related, Unset):
            related = self.related

        rustsec_id = self.rustsec_id

        url = self.url

        withdrawn = self.withdrawn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if categories is not UNSET:
            field_dict["categories"] = categories
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if date is not UNSET:
            field_dict["date"] = date
        if informational is not UNSET:
            field_dict["informational"] = informational
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if package is not UNSET:
            field_dict["package"] = package
        if references is not UNSET:
            field_dict["references"] = references
        if related is not UNSET:
            field_dict["related"] = related
        if rustsec_id is not UNSET:
            field_dict["rustsec_id"] = rustsec_id
        if url is not UNSET:
            field_dict["url"] = url
        if withdrawn is not UNSET:
            field_dict["withdrawn"] = withdrawn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aliases = cast(list[str], d.pop("aliases", UNSET))

        categories = cast(list[str], d.pop("categories", UNSET))

        cvss = d.pop("cvss", UNSET)

        date = d.pop("date", UNSET)

        informational = d.pop("informational", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        package = d.pop("package", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        related = cast(list[str], d.pop("related", UNSET))

        rustsec_id = d.pop("rustsec_id", UNSET)

        url = d.pop("url", UNSET)

        withdrawn = d.pop("withdrawn", UNSET)

        advisory_rustsec_front_matter_advisory = cls(
            aliases=aliases,
            categories=categories,
            cvss=cvss,
            date=date,
            informational=informational,
            keywords=keywords,
            package=package,
            references=references,
            related=related,
            rustsec_id=rustsec_id,
            url=url,
            withdrawn=withdrawn,
        )

        advisory_rustsec_front_matter_advisory.additional_properties = d
        return advisory_rustsec_front_matter_advisory

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
