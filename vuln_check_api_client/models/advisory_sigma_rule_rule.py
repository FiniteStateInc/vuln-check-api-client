from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_log_source import AdvisoryLogSource
    from ..models.advisory_related_rule import AdvisoryRelatedRule
    from ..models.advisory_sigma_rule_rule_detection import AdvisorySigmaRuleRuleDetection


T = TypeVar("T", bound="AdvisorySigmaRuleRule")


@_attrs_define
class AdvisorySigmaRuleRule:
    """
    Attributes:
        author (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        detection (Union[Unset, AdvisorySigmaRuleRuleDetection]):
        false_positives (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        id (Union[Unset, str]):
        level (Union[Unset, str]):
        logsource (Union[Unset, AdvisoryLogSource]):
        modified (Union[Unset, str]):
        references (Union[Unset, list[str]]):
        related (Union[Unset, list['AdvisoryRelatedRule']]):
        status (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        title (Union[Unset, str]):
    """

    author: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    detection: Union[Unset, "AdvisorySigmaRuleRuleDetection"] = UNSET
    false_positives: Union[Unset, list[str]] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    logsource: Union[Unset, "AdvisoryLogSource"] = UNSET
    modified: Union[Unset, str] = UNSET
    references: Union[Unset, list[str]] = UNSET
    related: Union[Unset, list["AdvisoryRelatedRule"]] = UNSET
    status: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        date = self.date

        description = self.description

        detection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.detection, Unset):
            detection = self.detection.to_dict()

        false_positives: Union[Unset, list[str]] = UNSET
        if not isinstance(self.false_positives, Unset):
            false_positives = self.false_positives

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        id = self.id

        level = self.level

        logsource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.logsource, Unset):
            logsource = self.logsource.to_dict()

        modified = self.modified

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        related: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related, Unset):
            related = []
            for related_item_data in self.related:
                related_item = related_item_data.to_dict()
                related.append(related_item)

        status = self.status

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if detection is not UNSET:
            field_dict["detection"] = detection
        if false_positives is not UNSET:
            field_dict["false_positives"] = false_positives
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if level is not UNSET:
            field_dict["level"] = level
        if logsource is not UNSET:
            field_dict["logsource"] = logsource
        if modified is not UNSET:
            field_dict["modified"] = modified
        if references is not UNSET:
            field_dict["references"] = references
        if related is not UNSET:
            field_dict["related"] = related
        if status is not UNSET:
            field_dict["status"] = status
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_log_source import AdvisoryLogSource
        from ..models.advisory_related_rule import AdvisoryRelatedRule
        from ..models.advisory_sigma_rule_rule_detection import AdvisorySigmaRuleRuleDetection

        d = dict(src_dict)
        author = d.pop("author", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        _detection = d.pop("detection", UNSET)
        detection: Union[Unset, AdvisorySigmaRuleRuleDetection]
        if isinstance(_detection, Unset):
            detection = UNSET
        else:
            detection = AdvisorySigmaRuleRuleDetection.from_dict(_detection)

        false_positives = cast(list[str], d.pop("false_positives", UNSET))

        fields = cast(list[str], d.pop("fields", UNSET))

        id = d.pop("id", UNSET)

        level = d.pop("level", UNSET)

        _logsource = d.pop("logsource", UNSET)
        logsource: Union[Unset, AdvisoryLogSource]
        if isinstance(_logsource, Unset):
            logsource = UNSET
        else:
            logsource = AdvisoryLogSource.from_dict(_logsource)

        modified = d.pop("modified", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        related = []
        _related = d.pop("related", UNSET)
        for related_item_data in _related or []:
            related_item = AdvisoryRelatedRule.from_dict(related_item_data)

            related.append(related_item)

        status = d.pop("status", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        title = d.pop("title", UNSET)

        advisory_sigma_rule_rule = cls(
            author=author,
            date=date,
            description=description,
            detection=detection,
            false_positives=false_positives,
            fields=fields,
            id=id,
            level=level,
            logsource=logsource,
            modified=modified,
            references=references,
            related=related,
            status=status,
            tags=tags,
            title=title,
        )

        advisory_sigma_rule_rule.additional_properties = d
        return advisory_sigma_rule_rule

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
