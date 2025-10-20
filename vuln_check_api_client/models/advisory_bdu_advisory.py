from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_bdu_cvss import AdvisoryBDUCvss
    from ..models.advisory_bdu_cvss_3 import AdvisoryBDUCvss3
    from ..models.advisory_bdu_environment import AdvisoryBDUEnvironment
    from ..models.advisory_bdu_vulnerable_software import AdvisoryBDUVulnerableSoftware


T = TypeVar("T", bound="AdvisoryBDUAdvisory")


@_attrs_define
class AdvisoryBDUAdvisory:
    """
    Attributes:
        bdu_id (Union[Unset, str]): BDU:2022-03833
        cve (Union[Unset, list[str]]): []string{"CVE-2022-28194"}
        cvss (Union[Unset, AdvisoryBDUCvss]):
        cvss3 (Union[Unset, AdvisoryBDUCvss3]):
        cwe (Union[Unset, str]): CWE-119
        date_added (Union[Unset, str]):
        description_ru (Union[Unset, str]): Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы,
            содержащие определенные сущности. В результате могут быть выполнены произвольные команды.
        environment (Union[Unset, AdvisoryBDUEnvironment]):
        exploit_status_en (Union[Unset, str]): Exploited
        exploit_status_ru (Union[Unset, str]): Exploited
        fix_status_en (Union[Unset, str]): Fixed
        fix_status_ru (Union[Unset, str]): Fixed
        identify_date (Union[Unset, str]): 2022-09-01
        name_ru (Union[Unset, str]): BDU:2022-03833: Уязвимость модуля Cboot (tegrabl_cbo.c) пакета драйверов
            микропрограммного обеспечения вычислительных плат NVIDIA Jetson, позволяющая нарушителю выполнить произвольный
            код или вызвать частичный отказ в обслуживании
        severity_ru (Union[Unset, str]): High
        solution_ru (Union[Unset, str]): Обновите драйверы микропрограммного обеспечения вычислительных плат NVIDIA
            Jetson до версии 32.6.1 или более поздней
        sources (Union[Unset, list[str]]): https://nvd.nist.gov/vuln/detail/CVE-2022-28194
        text_ru (Union[Unset, str]): Библиотека libxml2 до версии 2.9.12 не корректно обрабатывает XML-документы,
            содержащие определенные сущности. В результате могут быть выполнены произвольные команды.
        url (Union[Unset, str]): https://bdu.fstec.ru/vul/2022-03833
        vul_status_en (Union[Unset, str]): Exploitable
        vul_status_ru (Union[Unset, str]): Exploitable
        vulnerable_software (Union[Unset, AdvisoryBDUVulnerableSoftware]):
    """

    bdu_id: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    cvss: Union[Unset, "AdvisoryBDUCvss"] = UNSET
    cvss3: Union[Unset, "AdvisoryBDUCvss3"] = UNSET
    cwe: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    description_ru: Union[Unset, str] = UNSET
    environment: Union[Unset, "AdvisoryBDUEnvironment"] = UNSET
    exploit_status_en: Union[Unset, str] = UNSET
    exploit_status_ru: Union[Unset, str] = UNSET
    fix_status_en: Union[Unset, str] = UNSET
    fix_status_ru: Union[Unset, str] = UNSET
    identify_date: Union[Unset, str] = UNSET
    name_ru: Union[Unset, str] = UNSET
    severity_ru: Union[Unset, str] = UNSET
    solution_ru: Union[Unset, str] = UNSET
    sources: Union[Unset, list[str]] = UNSET
    text_ru: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    vul_status_en: Union[Unset, str] = UNSET
    vul_status_ru: Union[Unset, str] = UNSET
    vulnerable_software: Union[Unset, "AdvisoryBDUVulnerableSoftware"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bdu_id = self.bdu_id

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        cvss: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss, Unset):
            cvss = self.cvss.to_dict()

        cvss3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cvss3, Unset):
            cvss3 = self.cvss3.to_dict()

        cwe = self.cwe

        date_added = self.date_added

        description_ru = self.description_ru

        environment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        exploit_status_en = self.exploit_status_en

        exploit_status_ru = self.exploit_status_ru

        fix_status_en = self.fix_status_en

        fix_status_ru = self.fix_status_ru

        identify_date = self.identify_date

        name_ru = self.name_ru

        severity_ru = self.severity_ru

        solution_ru = self.solution_ru

        sources: Union[Unset, list[str]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        text_ru = self.text_ru

        url = self.url

        vul_status_en = self.vul_status_en

        vul_status_ru = self.vul_status_ru

        vulnerable_software: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vulnerable_software, Unset):
            vulnerable_software = self.vulnerable_software.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bdu_id is not UNSET:
            field_dict["bdu_id"] = bdu_id
        if cve is not UNSET:
            field_dict["cve"] = cve
        if cvss is not UNSET:
            field_dict["cvss"] = cvss
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cwe is not UNSET:
            field_dict["cwe"] = cwe
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description_ru is not UNSET:
            field_dict["description_ru"] = description_ru
        if environment is not UNSET:
            field_dict["environment"] = environment
        if exploit_status_en is not UNSET:
            field_dict["exploit_status_en"] = exploit_status_en
        if exploit_status_ru is not UNSET:
            field_dict["exploit_status_ru"] = exploit_status_ru
        if fix_status_en is not UNSET:
            field_dict["fix_status_en"] = fix_status_en
        if fix_status_ru is not UNSET:
            field_dict["fix_status_ru"] = fix_status_ru
        if identify_date is not UNSET:
            field_dict["identify_date"] = identify_date
        if name_ru is not UNSET:
            field_dict["name_ru"] = name_ru
        if severity_ru is not UNSET:
            field_dict["severity_ru"] = severity_ru
        if solution_ru is not UNSET:
            field_dict["solution_ru"] = solution_ru
        if sources is not UNSET:
            field_dict["sources"] = sources
        if text_ru is not UNSET:
            field_dict["text_ru"] = text_ru
        if url is not UNSET:
            field_dict["url"] = url
        if vul_status_en is not UNSET:
            field_dict["vul_status_en"] = vul_status_en
        if vul_status_ru is not UNSET:
            field_dict["vul_status_ru"] = vul_status_ru
        if vulnerable_software is not UNSET:
            field_dict["vulnerable_software"] = vulnerable_software

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_bdu_cvss import AdvisoryBDUCvss
        from ..models.advisory_bdu_cvss_3 import AdvisoryBDUCvss3
        from ..models.advisory_bdu_environment import AdvisoryBDUEnvironment
        from ..models.advisory_bdu_vulnerable_software import AdvisoryBDUVulnerableSoftware

        d = dict(src_dict)
        bdu_id = d.pop("bdu_id", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        _cvss = d.pop("cvss", UNSET)
        cvss: Union[Unset, AdvisoryBDUCvss]
        if isinstance(_cvss, Unset):
            cvss = UNSET
        else:
            cvss = AdvisoryBDUCvss.from_dict(_cvss)

        _cvss3 = d.pop("cvss3", UNSET)
        cvss3: Union[Unset, AdvisoryBDUCvss3]
        if isinstance(_cvss3, Unset):
            cvss3 = UNSET
        else:
            cvss3 = AdvisoryBDUCvss3.from_dict(_cvss3)

        cwe = d.pop("cwe", UNSET)

        date_added = d.pop("date_added", UNSET)

        description_ru = d.pop("description_ru", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, AdvisoryBDUEnvironment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = AdvisoryBDUEnvironment.from_dict(_environment)

        exploit_status_en = d.pop("exploit_status_en", UNSET)

        exploit_status_ru = d.pop("exploit_status_ru", UNSET)

        fix_status_en = d.pop("fix_status_en", UNSET)

        fix_status_ru = d.pop("fix_status_ru", UNSET)

        identify_date = d.pop("identify_date", UNSET)

        name_ru = d.pop("name_ru", UNSET)

        severity_ru = d.pop("severity_ru", UNSET)

        solution_ru = d.pop("solution_ru", UNSET)

        sources = cast(list[str], d.pop("sources", UNSET))

        text_ru = d.pop("text_ru", UNSET)

        url = d.pop("url", UNSET)

        vul_status_en = d.pop("vul_status_en", UNSET)

        vul_status_ru = d.pop("vul_status_ru", UNSET)

        _vulnerable_software = d.pop("vulnerable_software", UNSET)
        vulnerable_software: Union[Unset, AdvisoryBDUVulnerableSoftware]
        if isinstance(_vulnerable_software, Unset):
            vulnerable_software = UNSET
        else:
            vulnerable_software = AdvisoryBDUVulnerableSoftware.from_dict(_vulnerable_software)

        advisory_bdu_advisory = cls(
            bdu_id=bdu_id,
            cve=cve,
            cvss=cvss,
            cvss3=cvss3,
            cwe=cwe,
            date_added=date_added,
            description_ru=description_ru,
            environment=environment,
            exploit_status_en=exploit_status_en,
            exploit_status_ru=exploit_status_ru,
            fix_status_en=fix_status_en,
            fix_status_ru=fix_status_ru,
            identify_date=identify_date,
            name_ru=name_ru,
            severity_ru=severity_ru,
            solution_ru=solution_ru,
            sources=sources,
            text_ru=text_ru,
            url=url,
            vul_status_en=vul_status_en,
            vul_status_ru=vul_status_ru,
            vulnerable_software=vulnerable_software,
        )

        advisory_bdu_advisory.additional_properties = d
        return advisory_bdu_advisory

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
