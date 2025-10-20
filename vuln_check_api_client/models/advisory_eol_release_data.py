from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryEOLReleaseData")


@_attrs_define
class AdvisoryEOLReleaseData:
    """
    Attributes:
        already_eol (Union[Unset, bool]):
        branch (Union[Unset, str]): Alpine Linux
        branch_url (Union[Unset, str]): Alpine Linux
        codename (Union[Unset, str]):
        cpe (Union[Unset, str]):
        eol_date (Union[Unset, str]):
        eol_date_extended_support (Union[Unset, str]): Oracle Linux, Solaris
        eol_date_premier_support (Union[Unset, str]): Oracle Linux, Solaris
        eol_elts_date (Union[Unset, str]):
        eol_lts_date (Union[Unset, str]):
        git_branch (Union[Unset, str]): Alpine Linux
        git_branch_url (Union[Unset, str]): Alpine Linux
        lts (Union[Unset, bool]): Ubuntu
        minor_releases (Union[Unset, list[str]]): Alpine Linux
        product (Union[Unset, str]):
        release_date (Union[Unset, str]):
        release_name (Union[Unset, str]):
        source_url (Union[Unset, str]):
        technology_level (Union[Unset, str]): AIX
        vendor (Union[Unset, str]):
        version (Union[Unset, str]):
        version_api (Union[Unset, str]): Android
        version_darwin (Union[Unset, str]): macOS
        version_sunos (Union[Unset, str]): Solaris
        windows_current_build (Union[Unset, str]): Microsoft Windows
        windows_display_version (Union[Unset, str]): Microsoft Windows
        windows_edition_id (Union[Unset, str]): Microsoft Windows
        windows_insider_preview (Union[Unset, bool]): Microsoft Windows
    """

    already_eol: Union[Unset, bool] = UNSET
    branch: Union[Unset, str] = UNSET
    branch_url: Union[Unset, str] = UNSET
    codename: Union[Unset, str] = UNSET
    cpe: Union[Unset, str] = UNSET
    eol_date: Union[Unset, str] = UNSET
    eol_date_extended_support: Union[Unset, str] = UNSET
    eol_date_premier_support: Union[Unset, str] = UNSET
    eol_elts_date: Union[Unset, str] = UNSET
    eol_lts_date: Union[Unset, str] = UNSET
    git_branch: Union[Unset, str] = UNSET
    git_branch_url: Union[Unset, str] = UNSET
    lts: Union[Unset, bool] = UNSET
    minor_releases: Union[Unset, list[str]] = UNSET
    product: Union[Unset, str] = UNSET
    release_date: Union[Unset, str] = UNSET
    release_name: Union[Unset, str] = UNSET
    source_url: Union[Unset, str] = UNSET
    technology_level: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    version_api: Union[Unset, str] = UNSET
    version_darwin: Union[Unset, str] = UNSET
    version_sunos: Union[Unset, str] = UNSET
    windows_current_build: Union[Unset, str] = UNSET
    windows_display_version: Union[Unset, str] = UNSET
    windows_edition_id: Union[Unset, str] = UNSET
    windows_insider_preview: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        already_eol = self.already_eol

        branch = self.branch

        branch_url = self.branch_url

        codename = self.codename

        cpe = self.cpe

        eol_date = self.eol_date

        eol_date_extended_support = self.eol_date_extended_support

        eol_date_premier_support = self.eol_date_premier_support

        eol_elts_date = self.eol_elts_date

        eol_lts_date = self.eol_lts_date

        git_branch = self.git_branch

        git_branch_url = self.git_branch_url

        lts = self.lts

        minor_releases: Union[Unset, list[str]] = UNSET
        if not isinstance(self.minor_releases, Unset):
            minor_releases = self.minor_releases

        product = self.product

        release_date = self.release_date

        release_name = self.release_name

        source_url = self.source_url

        technology_level = self.technology_level

        vendor = self.vendor

        version = self.version

        version_api = self.version_api

        version_darwin = self.version_darwin

        version_sunos = self.version_sunos

        windows_current_build = self.windows_current_build

        windows_display_version = self.windows_display_version

        windows_edition_id = self.windows_edition_id

        windows_insider_preview = self.windows_insider_preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if already_eol is not UNSET:
            field_dict["already_eol"] = already_eol
        if branch is not UNSET:
            field_dict["branch"] = branch
        if branch_url is not UNSET:
            field_dict["branch_url"] = branch_url
        if codename is not UNSET:
            field_dict["codename"] = codename
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if eol_date is not UNSET:
            field_dict["eol_date"] = eol_date
        if eol_date_extended_support is not UNSET:
            field_dict["eol_date_extended_support"] = eol_date_extended_support
        if eol_date_premier_support is not UNSET:
            field_dict["eol_date_premier_support"] = eol_date_premier_support
        if eol_elts_date is not UNSET:
            field_dict["eol_elts_date"] = eol_elts_date
        if eol_lts_date is not UNSET:
            field_dict["eol_lts_date"] = eol_lts_date
        if git_branch is not UNSET:
            field_dict["git_branch"] = git_branch
        if git_branch_url is not UNSET:
            field_dict["git_branch_url"] = git_branch_url
        if lts is not UNSET:
            field_dict["lts"] = lts
        if minor_releases is not UNSET:
            field_dict["minor_releases"] = minor_releases
        if product is not UNSET:
            field_dict["product"] = product
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if release_name is not UNSET:
            field_dict["release_name"] = release_name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if technology_level is not UNSET:
            field_dict["technology_level"] = technology_level
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if version is not UNSET:
            field_dict["version"] = version
        if version_api is not UNSET:
            field_dict["version_api"] = version_api
        if version_darwin is not UNSET:
            field_dict["version_darwin"] = version_darwin
        if version_sunos is not UNSET:
            field_dict["version_sunos"] = version_sunos
        if windows_current_build is not UNSET:
            field_dict["windows_current_build"] = windows_current_build
        if windows_display_version is not UNSET:
            field_dict["windows_display_version"] = windows_display_version
        if windows_edition_id is not UNSET:
            field_dict["windows_edition_id"] = windows_edition_id
        if windows_insider_preview is not UNSET:
            field_dict["windows_insider_preview"] = windows_insider_preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        already_eol = d.pop("already_eol", UNSET)

        branch = d.pop("branch", UNSET)

        branch_url = d.pop("branch_url", UNSET)

        codename = d.pop("codename", UNSET)

        cpe = d.pop("cpe", UNSET)

        eol_date = d.pop("eol_date", UNSET)

        eol_date_extended_support = d.pop("eol_date_extended_support", UNSET)

        eol_date_premier_support = d.pop("eol_date_premier_support", UNSET)

        eol_elts_date = d.pop("eol_elts_date", UNSET)

        eol_lts_date = d.pop("eol_lts_date", UNSET)

        git_branch = d.pop("git_branch", UNSET)

        git_branch_url = d.pop("git_branch_url", UNSET)

        lts = d.pop("lts", UNSET)

        minor_releases = cast(list[str], d.pop("minor_releases", UNSET))

        product = d.pop("product", UNSET)

        release_date = d.pop("release_date", UNSET)

        release_name = d.pop("release_name", UNSET)

        source_url = d.pop("source_url", UNSET)

        technology_level = d.pop("technology_level", UNSET)

        vendor = d.pop("vendor", UNSET)

        version = d.pop("version", UNSET)

        version_api = d.pop("version_api", UNSET)

        version_darwin = d.pop("version_darwin", UNSET)

        version_sunos = d.pop("version_sunos", UNSET)

        windows_current_build = d.pop("windows_current_build", UNSET)

        windows_display_version = d.pop("windows_display_version", UNSET)

        windows_edition_id = d.pop("windows_edition_id", UNSET)

        windows_insider_preview = d.pop("windows_insider_preview", UNSET)

        advisory_eol_release_data = cls(
            already_eol=already_eol,
            branch=branch,
            branch_url=branch_url,
            codename=codename,
            cpe=cpe,
            eol_date=eol_date,
            eol_date_extended_support=eol_date_extended_support,
            eol_date_premier_support=eol_date_premier_support,
            eol_elts_date=eol_elts_date,
            eol_lts_date=eol_lts_date,
            git_branch=git_branch,
            git_branch_url=git_branch_url,
            lts=lts,
            minor_releases=minor_releases,
            product=product,
            release_date=release_date,
            release_name=release_name,
            source_url=source_url,
            technology_level=technology_level,
            vendor=vendor,
            version=version,
            version_api=version_api,
            version_darwin=version_darwin,
            version_sunos=version_sunos,
            windows_current_build=windows_current_build,
            windows_display_version=windows_display_version,
            windows_edition_id=windows_edition_id,
            windows_insider_preview=windows_insider_preview,
        )

        advisory_eol_release_data.additional_properties = d
        return advisory_eol_release_data

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
