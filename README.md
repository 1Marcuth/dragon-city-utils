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

dragon_sprite.download(output="dragon_nature_sprite.png")
```

#### Dragon thumb

```py
from dcutils.static.sprites import DragonThumb

dragon_thumb = DragonThumb(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1
)

dragon_thumb.download(output="dragon_nature_thumb.png")
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

dragon_flash_animation.download(output="dragon_nature_flash_animation.swf")
```

#### Dragon Animation (Spine Animation)

```py
from dcutils.static.animations import DragonSpineAnimation

dragon_spine_animation = DragonSpineAnimation(
    image_name="1000_dragon_nature",
    phase=3,
    skin=1
)

dragon_spine_animation.download(output="dragon_spine_animation.zip")
```

### Island packages

```py
from dcutils.static.islands import IslandPackage

island_package = IslandPackage(uri="/mobile/ui/heroicraces_islands/hr_71_heroicorigins.zip")

island_package.download(output="island_package.zip")
```

### Sounds

#### Musics
```py
from dcutils.static.sounds import GeneralMusic

music = GeneralMusic(music_name="531_dc_party_planning_island")

music.download(output="531_dc_party_planning_island.mp3")
```

## Tools

### Calculators

### Calculate elements strongs

```py
from dcutils.tools.calculators import calculate_strongs

strongs = calculate_strongs(elements=["terra", "flame"])
```
**Output:**
```
['electric', 'flame', 'nature', 'ice']
```

### Calculate elements weaknesses

```py
from dcutils.tools.calculators import calculate_weaknesses

weaknesses = calculate_weaknesses(first_element="terra")
```
**Output:**
```
['metal', 'war']
```

### Calculate orb recall gain

```py
from dcutils.tools.calculators import calculate_orb_recall_gain

orb_recall_gain = calculate_orb_recall_gain(dragon_level=15, dragon_stars=2)
```
**Output:**
```
389
```

### AI (Artificial Intelligence)

#### Elements detector
```py
from dcutils.tools.ai.elements_detector import ElementsDetectorAI

elements_detector = ElementsDetectorAI()

elements_result = elements_detector.detect(image_path="ui_3110_dragon_hoardereternal_1@2x.png", limit=4)
```
**Output:**
```
[
    {
        "element": "ice",
        "confidence_score": 0.4871271550655365   
    },
    {
        "element": "nature",
        "confidence_score": 0.296091228723526
    },
    {
        "element": "flame",
        "confidence_score": 0.16774502396583557
    },
    {
        "element": "sea",
        "confidence_score": 0.03868602588772774
    }
]
```

#### Phase detector
```py 
from dcutils.tools.ai.phase_detector import PhaseDetectorAI

phase_detector = PhaseDetectorAI()

phase_result = phase_detector.detect(image_path="ui_3110_dragon_hoardereternal_1@2x.png")
```
**Output:**
```
{
    "phase": "baby",
    "confidence_score": 0.9999938011169434
}
```