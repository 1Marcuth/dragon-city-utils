# Soon to be documented, enjoy for now and install to discover the tools

## Download static files

### Sprites

#### Dragon sprite

```py
from dcutils.static.sprites import DragonSprite

dragon_sprite = DragonSprite(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1,
    image_quality=2
)

dragon_sprite.download("dragon_nature_sprite.png")
```

#### Dragon thumb

```py
from dcutils.static.sprites import DragonThumb

dragon_thumb = DragonThumb(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1
)

dragon_thumb.download("dragon_nature_thumb.png")
```

### Animations

#### Dragon Animation (Flash Animation)

```py
from dcutils.static.animations import DragonSpineAnimation

dragon_flash_animation = DragonFlashAnimation(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1
)

dragon_flash_animation.download("drago_nature_flash_animation.swf")
```

#### Dragon Animation (Spine Animation)

```py
from dcutils.static.animations import DragonSpineAnimation

dragon_spine_animation = DragonSpineAnimation(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1
)

dragon_spine_animation.download("dragon_spine_animation.zip")
```

### Island packages

```py
from dcutils.static.islands import IslandPackage

island_package = IslandPackage(uri="/mobile/ui/heroicraces_islands/hr_71_heroicorigins.zip")

island_package.download("island_package.zip")
```

### Sounds

#### Musics
```py
from dcutils.static.sounds import GeneralMusic

music = GeneralMusic(music_name="531_dc_party_planning_island")

music.download("531_dc_party_planning_island.mp3")
```