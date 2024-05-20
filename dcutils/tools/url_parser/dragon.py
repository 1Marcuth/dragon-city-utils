from pydantic import validate_call
import re

class DragonUrlParser:
    @classmethod
    @validate_call
    def get_image_name(cls, url: str) -> str | None:
        match = re.search(r"\/(basic_|thumb_|ui_)?(\d+)_([\w_]+)", url)

        if match:
            id = match.group(2)
            image_name_without_id = match.group(3)
            raw_image_name = f"{id}_{image_name_without_id}"
            void_str = ""

            image_name_with_skin = re.sub(
                r"_\d+",
                void_str,
                raw_image_name
            )

            image_name_without_skin = re.sub(
                r"_skin\d+",
                void_str,
                image_name_with_skin
            )

            return image_name_without_skin

    @classmethod
    @validate_call
    def get_id(cls, url: str) -> int | None:
        match = re.search(r"\/(basic_|thumb_|ui_)?(\d+)_", url)

        if match:
            id = int(match.group(2))
            return id
    
    @classmethod
    @validate_call
    def get_phase(cls, url: str) -> int | None:
        match = re.search(r"(\d+)@2x\.(png|swf)|(\d+)\.(png|swf)|(\d+)_HD_tweened_dxt5.zip|(\d+)_HD_spine-3-8-59_dxt5.zip", url)

        if match:
            phase = int(
                match.group(1) or
                match.group(3) or
                match.group(5) or
                match.group(6))

            return phase

    @classmethod
    @validate_call
    def get_skin(cls, url: str) -> str | None:
        match = re.search(r"_skin\d+", url)

        if match:
            skin = match.group(0)[1:]
            return skin

    @classmethod
    @validate_call
    def get_image_qualitity(cls, url: str) -> str:
        match = re.search(r"@\d+x", url)

        if match:
            image_qualitity = match.group(0)
            return image_qualitity

        return ""

    @classmethod
    @validate_call
    def from_sprite(cls, url: str) -> dict:
        return dict(
            id = cls.get_id(url),
            image_name = cls.get_image_name(url),
            phase = cls.get_phase(url),
            skin = cls.get_skin(url),
            image_qualitity = cls.get_image_qualitity(url)
        )

    @classmethod
    @validate_call
    def from_thumb(cls, url: str) -> dict:
        return dict(
            id = cls.get_id(url),
            image_name = cls.get_image_name(url),
            phase = cls.get_phase(url),
            skin = cls.get_skin(url)
        )

    @classmethod
    @validate_call
    def from_flash_animation(cls, url: str) -> dict:
        return dict(
            id = cls.get_id(url),
            image_name = cls.get_image_name(url),
            phase = cls.get_phase(url),
            skin = cls.get_skin(url)
        )

    @classmethod
    @validate_call
    def from_spine_animation(cls, url: str) -> dict:
        return dict(
            id = cls.get_id(url),
            image_name = cls.get_image_name(url),
            phase = cls.get_phase(url),
            skin = cls.get_skin(url)
        )