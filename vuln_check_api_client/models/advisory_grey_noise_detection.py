from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_grey_noise_tags import AdvisoryGreyNoiseTags


T = TypeVar("T", bound="AdvisoryGreyNoiseDetection")


@_attrs_define
class AdvisoryGreyNoiseDetection:
    """
    Attributes:
        category (Union[Unset, str]):
        cve (Union[Unset, list[str]]):
        date_added (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        intention (Union[Unset, str]):
        label (Union[Unset, str]):
        name (Union[Unset, str]):
        recommend_block (Union[Unset, bool]):
        references (Union[Unset, list[str]]):
        related_tags (Union[Unset, list['AdvisoryGreyNoiseTags']]):
        slug (Union[Unset, str]):
        updated_at (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    category: Union[Unset, str] = UNSET
    cve: Union[Unset, list[str]] = UNSET
    date_added: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    intention: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recommend_block: Union[Unset, bool] = UNSET
    references: Union[Unset, list[str]] = UNSET
    related_tags: Union[Unset, list["AdvisoryGreyNoiseTags"]] = UNSET
    slug: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        cve: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cve, Unset):
            cve = self.cve

        date_added = self.date_added

        description = self.description

        id = self.id

        intention = self.intention

        label = self.label

        name = self.name

        recommend_block = self.recommend_block

        references: Union[Unset, list[str]] = UNSET
        if not isinstance(self.references, Unset):
            references = self.references

        related_tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related_tags, Unset):
            related_tags = []
            for related_tags_item_data in self.related_tags:
                related_tags_item = related_tags_item_data.to_dict()
                related_tags.append(related_tags_item)

        slug = self.slug

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if cve is not UNSET:
            field_dict["cve"] = cve
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if intention is not UNSET:
            field_dict["intention"] = intention
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if recommend_block is not UNSET:
            field_dict["recommend_block"] = recommend_block
        if references is not UNSET:
            field_dict["references"] = references
        if related_tags is not UNSET:
            field_dict["related_tags"] = related_tags
        if slug is not UNSET:
            field_dict["slug"] = slug
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_grey_noise_tags import AdvisoryGreyNoiseTags

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        cve = cast(list[str], d.pop("cve", UNSET))

        date_added = d.pop("date_added", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        intention = d.pop("intention", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        recommend_block = d.pop("recommend_block", UNSET)

        references = cast(list[str], d.pop("references", UNSET))

        related_tags = []
        _related_tags = d.pop("related_tags", UNSET)
        for related_tags_item_data in _related_tags or []:
            related_tags_item = AdvisoryGreyNoiseTags.from_dict(related_tags_item_data)

            related_tags.append(related_tags_item)

        slug = d.pop("slug", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        advisory_grey_noise_detection = cls(
            category=category,
            cve=cve,
            date_added=date_added,
            description=description,
            id=id,
            intention=intention,
            label=label,
            name=name,
            recommend_block=recommend_block,
            references=references,
            related_tags=related_tags,
            slug=slug,
            updated_at=updated_at,
            url=url,
        )

        advisory_grey_noise_detection.additional_properties = d
        return advisory_grey_noise_detection

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
