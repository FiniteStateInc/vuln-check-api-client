from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiInitialAccessArtifact")


@_attrs_define
class ApiInitialAccessArtifact:
    """
    Attributes:
        artifact_name (Union[Unset, str]): ArtifactName is a title to associate with this artifact.
        artifacts_url (Union[Unset, list[str]]): ArtifactsURL are URLs to the available artifact.
        baidu_queries (Union[Unset, list[str]]): ...
        baidu_raw_queries (Union[Unset, list[str]]): ...
        censys_legacy_queries (Union[Unset, list[str]]): CensysLegacyQueries are legacy queries for examining potential
            Internet-exposed devices & applications with Censys in URL form.
        censys_legacy_raw_queries (Union[Unset, list[str]]): CensysLegacyRawQueries are raw legacy queries for examining
            potential Internet-exposed devices & applications with Censys.
        censys_queries (Union[Unset, list[str]]): CensysQueries are queries for examining potential Internet-exposed
            devices & applications with Censys in URL form.
        censys_raw_queries (Union[Unset, list[str]]): CensysRawQueries are raw queries for examining potential Internet-
            exposed devices & applications with Censys.
        clone_sshurl (Union[Unset, str]): CloneSSHURL is the git URL to clone the artifact with.
        date_added (Union[Unset, str]): DateAdded is when this artifact entry was first added to the InitialAccess data
            set.
        driftnet_queries (Union[Unset, list[str]]): DriftnetQueries are queries for examining Internet exposed services
            with Driftnet.
        driftnet_raw_queries (Union[Unset, list[str]]): DriftnetRawQueries are queries for examining Internet exposed
            services with Driftnet.
        exploit (Union[Unset, bool]): Exploit indicates whether or not an exploit is available in this artifact.
        fofa_queries (Union[Unset, list[str]]): FOFAQueries are raw queries for examining potential Internet-exposed
            devices & applications with FOFA.
        fofa_raw_queries (Union[Unset, list[str]]):
        google_queries (Union[Unset, list[str]]): google queries
        google_raw_queries (Union[Unset, list[str]]): raw google queries
        greynoise_queries (Union[Unset, list[str]]): GreynoiseQueries are queries for finding the vulnerability via
            honeypot data.
        mitre_attack_techniques (Union[Unset, list[str]]): MITRE ATT&CK techniques
        nmap_script (Union[Unset, bool]): NmapScript indicates whether or not an nmap script for scanning environment
            exists in this artifact.
        pcap (Union[Unset, bool]): PCAP indicates whether of not a package capture of the exploit PoC exploiting a
            vulnerable system exists in this artifact.
        product (Union[Unset, list[str]]): Product are the software that has the vulnerability.
        shodan_queries (Union[Unset, list[str]]): ShodanQueries are queries for examining potential Internet-exposed
            devices & applications with Shodan in URL form.
        shodan_raw_queries (Union[Unset, list[str]]): ShodanRawQueries are raw queries for examining potential Internet-
            exposed devices & applications with Shodan.
        sigma_rule (Union[Unset, bool]): SigmaRule indicates whether or not a Sigma rule designed to detect the
            exploitation of the vulnerability over the network exists in this artifact.
        snort_rule (Union[Unset, bool]): SnortRule indicates whether or not a Snort rule designed to detect the
            exploitation of the vulnerability over the network exists in this artifact.
        suricata_rule (Union[Unset, bool]): SuricataRule indicates whether or not a Suricata rule designed to detect the
            exploitation of the vulnerability over the network exists in this artifact.
        target_docker (Union[Unset, bool]): TargetDocker indicates whether or not there is an available docker image
            with the vulnerability.
        target_encrypted_comms (Union[Unset, str]): Encrypted communications?
        target_service (Union[Unset, str]): TargetService indicates the service (HTTP, FTP, etc) that this exploit
            targets.
        vendor (Union[Unset, str]): Vendor of the vulnerable product
        version_scanner (Union[Unset, bool]): VersionScanner indicates whether or not the exploit PoC can determine if
            target system is vulnerable without sending exploit payload in this artifact.
        yara (Union[Unset, bool]): YARA indicates whether or not a YARA rule designed to detect the exploit on an
            endpoint exists in this artifact.
        zeroday (Union[Unset, bool]): Zeroday indicates whether or not it is a VulnCheck zeroday.
        zoom_eye_queries (Union[Unset, list[str]]): ZoomEyeQueries are raw queries for examining potential Internet-
            exposed devices & applications with ZoomEye.
        zoom_eye_raw_queries (Union[Unset, list[str]]):
    """

    artifact_name: Union[Unset, str] = UNSET
    artifacts_url: Union[Unset, list[str]] = UNSET
    baidu_queries: Union[Unset, list[str]] = UNSET
    baidu_raw_queries: Union[Unset, list[str]] = UNSET
    censys_legacy_queries: Union[Unset, list[str]] = UNSET
    censys_legacy_raw_queries: Union[Unset, list[str]] = UNSET
    censys_queries: Union[Unset, list[str]] = UNSET
    censys_raw_queries: Union[Unset, list[str]] = UNSET
    clone_sshurl: Union[Unset, str] = UNSET
    date_added: Union[Unset, str] = UNSET
    driftnet_queries: Union[Unset, list[str]] = UNSET
    driftnet_raw_queries: Union[Unset, list[str]] = UNSET
    exploit: Union[Unset, bool] = UNSET
    fofa_queries: Union[Unset, list[str]] = UNSET
    fofa_raw_queries: Union[Unset, list[str]] = UNSET
    google_queries: Union[Unset, list[str]] = UNSET
    google_raw_queries: Union[Unset, list[str]] = UNSET
    greynoise_queries: Union[Unset, list[str]] = UNSET
    mitre_attack_techniques: Union[Unset, list[str]] = UNSET
    nmap_script: Union[Unset, bool] = UNSET
    pcap: Union[Unset, bool] = UNSET
    product: Union[Unset, list[str]] = UNSET
    shodan_queries: Union[Unset, list[str]] = UNSET
    shodan_raw_queries: Union[Unset, list[str]] = UNSET
    sigma_rule: Union[Unset, bool] = UNSET
    snort_rule: Union[Unset, bool] = UNSET
    suricata_rule: Union[Unset, bool] = UNSET
    target_docker: Union[Unset, bool] = UNSET
    target_encrypted_comms: Union[Unset, str] = UNSET
    target_service: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    version_scanner: Union[Unset, bool] = UNSET
    yara: Union[Unset, bool] = UNSET
    zeroday: Union[Unset, bool] = UNSET
    zoom_eye_queries: Union[Unset, list[str]] = UNSET
    zoom_eye_raw_queries: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        artifact_name = self.artifact_name

        artifacts_url: Union[Unset, list[str]] = UNSET
        if not isinstance(self.artifacts_url, Unset):
            artifacts_url = self.artifacts_url

        baidu_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.baidu_queries, Unset):
            baidu_queries = self.baidu_queries

        baidu_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.baidu_raw_queries, Unset):
            baidu_raw_queries = self.baidu_raw_queries

        censys_legacy_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.censys_legacy_queries, Unset):
            censys_legacy_queries = self.censys_legacy_queries

        censys_legacy_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.censys_legacy_raw_queries, Unset):
            censys_legacy_raw_queries = self.censys_legacy_raw_queries

        censys_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.censys_queries, Unset):
            censys_queries = self.censys_queries

        censys_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.censys_raw_queries, Unset):
            censys_raw_queries = self.censys_raw_queries

        clone_sshurl = self.clone_sshurl

        date_added = self.date_added

        driftnet_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.driftnet_queries, Unset):
            driftnet_queries = self.driftnet_queries

        driftnet_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.driftnet_raw_queries, Unset):
            driftnet_raw_queries = self.driftnet_raw_queries

        exploit = self.exploit

        fofa_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fofa_queries, Unset):
            fofa_queries = self.fofa_queries

        fofa_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fofa_raw_queries, Unset):
            fofa_raw_queries = self.fofa_raw_queries

        google_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.google_queries, Unset):
            google_queries = self.google_queries

        google_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.google_raw_queries, Unset):
            google_raw_queries = self.google_raw_queries

        greynoise_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.greynoise_queries, Unset):
            greynoise_queries = self.greynoise_queries

        mitre_attack_techniques: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mitre_attack_techniques, Unset):
            mitre_attack_techniques = self.mitre_attack_techniques

        nmap_script = self.nmap_script

        pcap = self.pcap

        product: Union[Unset, list[str]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product

        shodan_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shodan_queries, Unset):
            shodan_queries = self.shodan_queries

        shodan_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shodan_raw_queries, Unset):
            shodan_raw_queries = self.shodan_raw_queries

        sigma_rule = self.sigma_rule

        snort_rule = self.snort_rule

        suricata_rule = self.suricata_rule

        target_docker = self.target_docker

        target_encrypted_comms = self.target_encrypted_comms

        target_service = self.target_service

        vendor = self.vendor

        version_scanner = self.version_scanner

        yara = self.yara

        zeroday = self.zeroday

        zoom_eye_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.zoom_eye_queries, Unset):
            zoom_eye_queries = self.zoom_eye_queries

        zoom_eye_raw_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.zoom_eye_raw_queries, Unset):
            zoom_eye_raw_queries = self.zoom_eye_raw_queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifact_name is not UNSET:
            field_dict["artifactName"] = artifact_name
        if artifacts_url is not UNSET:
            field_dict["artifactsURL"] = artifacts_url
        if baidu_queries is not UNSET:
            field_dict["baiduQueries"] = baidu_queries
        if baidu_raw_queries is not UNSET:
            field_dict["baiduRawQueries"] = baidu_raw_queries
        if censys_legacy_queries is not UNSET:
            field_dict["censysLegacyQueries"] = censys_legacy_queries
        if censys_legacy_raw_queries is not UNSET:
            field_dict["censysLegacyRawQueries"] = censys_legacy_raw_queries
        if censys_queries is not UNSET:
            field_dict["censysQueries"] = censys_queries
        if censys_raw_queries is not UNSET:
            field_dict["censysRawQueries"] = censys_raw_queries
        if clone_sshurl is not UNSET:
            field_dict["cloneSSHURL"] = clone_sshurl
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if driftnet_queries is not UNSET:
            field_dict["driftnetQueries"] = driftnet_queries
        if driftnet_raw_queries is not UNSET:
            field_dict["driftnetRawQueries"] = driftnet_raw_queries
        if exploit is not UNSET:
            field_dict["exploit"] = exploit
        if fofa_queries is not UNSET:
            field_dict["fofaQueries"] = fofa_queries
        if fofa_raw_queries is not UNSET:
            field_dict["fofaRawQueries"] = fofa_raw_queries
        if google_queries is not UNSET:
            field_dict["googleQueries"] = google_queries
        if google_raw_queries is not UNSET:
            field_dict["googleRawQueries"] = google_raw_queries
        if greynoise_queries is not UNSET:
            field_dict["greynoiseQueries"] = greynoise_queries
        if mitre_attack_techniques is not UNSET:
            field_dict["mitreAttackTechniques"] = mitre_attack_techniques
        if nmap_script is not UNSET:
            field_dict["nmapScript"] = nmap_script
        if pcap is not UNSET:
            field_dict["pcap"] = pcap
        if product is not UNSET:
            field_dict["product"] = product
        if shodan_queries is not UNSET:
            field_dict["shodanQueries"] = shodan_queries
        if shodan_raw_queries is not UNSET:
            field_dict["shodanRawQueries"] = shodan_raw_queries
        if sigma_rule is not UNSET:
            field_dict["sigmaRule"] = sigma_rule
        if snort_rule is not UNSET:
            field_dict["snortRule"] = snort_rule
        if suricata_rule is not UNSET:
            field_dict["suricataRule"] = suricata_rule
        if target_docker is not UNSET:
            field_dict["targetDocker"] = target_docker
        if target_encrypted_comms is not UNSET:
            field_dict["targetEncryptedComms"] = target_encrypted_comms
        if target_service is not UNSET:
            field_dict["targetService"] = target_service
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if version_scanner is not UNSET:
            field_dict["versionScanner"] = version_scanner
        if yara is not UNSET:
            field_dict["yara"] = yara
        if zeroday is not UNSET:
            field_dict["zeroday"] = zeroday
        if zoom_eye_queries is not UNSET:
            field_dict["zoomEyeQueries"] = zoom_eye_queries
        if zoom_eye_raw_queries is not UNSET:
            field_dict["zoomEyeRawQueries"] = zoom_eye_raw_queries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        artifact_name = d.pop("artifactName", UNSET)

        artifacts_url = cast(list[str], d.pop("artifactsURL", UNSET))

        baidu_queries = cast(list[str], d.pop("baiduQueries", UNSET))

        baidu_raw_queries = cast(list[str], d.pop("baiduRawQueries", UNSET))

        censys_legacy_queries = cast(list[str], d.pop("censysLegacyQueries", UNSET))

        censys_legacy_raw_queries = cast(list[str], d.pop("censysLegacyRawQueries", UNSET))

        censys_queries = cast(list[str], d.pop("censysQueries", UNSET))

        censys_raw_queries = cast(list[str], d.pop("censysRawQueries", UNSET))

        clone_sshurl = d.pop("cloneSSHURL", UNSET)

        date_added = d.pop("dateAdded", UNSET)

        driftnet_queries = cast(list[str], d.pop("driftnetQueries", UNSET))

        driftnet_raw_queries = cast(list[str], d.pop("driftnetRawQueries", UNSET))

        exploit = d.pop("exploit", UNSET)

        fofa_queries = cast(list[str], d.pop("fofaQueries", UNSET))

        fofa_raw_queries = cast(list[str], d.pop("fofaRawQueries", UNSET))

        google_queries = cast(list[str], d.pop("googleQueries", UNSET))

        google_raw_queries = cast(list[str], d.pop("googleRawQueries", UNSET))

        greynoise_queries = cast(list[str], d.pop("greynoiseQueries", UNSET))

        mitre_attack_techniques = cast(list[str], d.pop("mitreAttackTechniques", UNSET))

        nmap_script = d.pop("nmapScript", UNSET)

        pcap = d.pop("pcap", UNSET)

        product = cast(list[str], d.pop("product", UNSET))

        shodan_queries = cast(list[str], d.pop("shodanQueries", UNSET))

        shodan_raw_queries = cast(list[str], d.pop("shodanRawQueries", UNSET))

        sigma_rule = d.pop("sigmaRule", UNSET)

        snort_rule = d.pop("snortRule", UNSET)

        suricata_rule = d.pop("suricataRule", UNSET)

        target_docker = d.pop("targetDocker", UNSET)

        target_encrypted_comms = d.pop("targetEncryptedComms", UNSET)

        target_service = d.pop("targetService", UNSET)

        vendor = d.pop("vendor", UNSET)

        version_scanner = d.pop("versionScanner", UNSET)

        yara = d.pop("yara", UNSET)

        zeroday = d.pop("zeroday", UNSET)

        zoom_eye_queries = cast(list[str], d.pop("zoomEyeQueries", UNSET))

        zoom_eye_raw_queries = cast(list[str], d.pop("zoomEyeRawQueries", UNSET))

        api_initial_access_artifact = cls(
            artifact_name=artifact_name,
            artifacts_url=artifacts_url,
            baidu_queries=baidu_queries,
            baidu_raw_queries=baidu_raw_queries,
            censys_legacy_queries=censys_legacy_queries,
            censys_legacy_raw_queries=censys_legacy_raw_queries,
            censys_queries=censys_queries,
            censys_raw_queries=censys_raw_queries,
            clone_sshurl=clone_sshurl,
            date_added=date_added,
            driftnet_queries=driftnet_queries,
            driftnet_raw_queries=driftnet_raw_queries,
            exploit=exploit,
            fofa_queries=fofa_queries,
            fofa_raw_queries=fofa_raw_queries,
            google_queries=google_queries,
            google_raw_queries=google_raw_queries,
            greynoise_queries=greynoise_queries,
            mitre_attack_techniques=mitre_attack_techniques,
            nmap_script=nmap_script,
            pcap=pcap,
            product=product,
            shodan_queries=shodan_queries,
            shodan_raw_queries=shodan_raw_queries,
            sigma_rule=sigma_rule,
            snort_rule=snort_rule,
            suricata_rule=suricata_rule,
            target_docker=target_docker,
            target_encrypted_comms=target_encrypted_comms,
            target_service=target_service,
            vendor=vendor,
            version_scanner=version_scanner,
            yara=yara,
            zeroday=zeroday,
            zoom_eye_queries=zoom_eye_queries,
            zoom_eye_raw_queries=zoom_eye_raw_queries,
        )

        api_initial_access_artifact.additional_properties = d
        return api_initial_access_artifact

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
