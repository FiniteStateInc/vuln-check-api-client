from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_chain_guard_package import AdvisoryChainGuardPackage


T = TypeVar("T", bound="AdvisoryChainGuard")


@_attrs_define
class AdvisoryChainGuard:
    """
    Attributes:
        apkurl (Union[Unset, str]):
        archs (Union[Unset, list[str]]):
        date_added (Union[Unset, str]): un-used
        packages (Union[Unset, list['AdvisoryChainGuardPackage']]):
        reponame (Union[Unset, str]):
        urlprefix (Union[Unset, str]):
    """

    apkurl: Union[Unset, str] = UNSET
    archs: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    packages: Union[Unset, list["AdvisoryChainGuardPackage"]] = UNSET
    reponame: Union[Unset, str] = UNSET
    urlprefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apkurl = self.apkurl

        archs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.archs, Unset):
            archs = self.archs

        date_added = self.date_added

        packages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        reponame = self.reponame

        urlprefix = self.urlprefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apkurl is not UNSET:
            field_dict["apkurl"] = apkurl
        if archs is not UNSET:
            field_dict["archs"] = archs
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if packages is not UNSET:
            field_dict["packages"] = packages
        if reponame is not UNSET:
            field_dict["reponame"] = reponame
        if urlprefix is not UNSET:
            field_dict["urlprefix"] = urlprefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_chain_guard_package import AdvisoryChainGuardPackage

        d = dict(src_dict)
        apkurl = d.pop("apkurl", UNSET)

        archs = cast(list[str], d.pop("archs", UNSET))

        date_added = d.pop("date_added", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = AdvisoryChainGuardPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        reponame = d.pop("reponame", UNSET)

        urlprefix = d.pop("urlprefix", UNSET)

        advisory_chain_guard = cls(
            apkurl=apkurl,
            archs=archs,
            date_added=date_added,
            packages=packages,
            reponame=reponame,
            urlprefix=urlprefix,
        )

        advisory_chain_guard.additional_properties = d
        return advisory_chain_guard

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
