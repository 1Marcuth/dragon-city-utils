# dragon-city-utils

Welcome to the documentation of Dragon City Utils, a collection of tools and utilities for managing static assets and performing calculations related to the game Dragon City. Below, you'll find detailed explanations and code snippets for various functionalities.

## Static Files

### Sprites

#### Dragon Sprite

You can download a dragon sprite using the following code:

```python
from dcutils.static.sprites import DragonSprite

dragon_sprite = DragonSprite(
    image_name = "1000_dragon_nature",
    phase = 3,
    skin = "skin1",
    image_quality = 2
)

dragon_sprite.download(output="dragon_nature_sprite.png")
```
#### Dragon Thumb

To download a dragon thumb:

```python
from dcutils.static.sprites import DragonThumb

dragon_thumb = DragonThumb(
    image_name = "1000_dragon_nature",
    phase = 3,
    skin = "skin1"
)

dragon_thumb.download(output="dragon_nature_thumb.png")
```

### Animations

#### Dragon Animation (Flash Animation)

To download a dragon flash animation:

```python
from dcutils.static.animations import DragonFlashAnimation

dragon_flash_animation = DragonFlashAnimation(
    image_name = "1000_dragon_nature",
    phase = 3,
    skin = "skin1"
)

dragon_flash_animation.download(output="dragon_nature_flash_animation.swf")
```

#### Dragon Animation (Spine Animation)

To download a dragon spine animation:

```python
from dcutils.static.animations import DragonSpineAnimation

dragon_spine_animation = DragonSpineAnimation(
    image_name = "1000_dragon_nature",
    phase = 3,
    skin = 1
)

dragon_spine_animation.download(output="dragon_spine_animation.zip")
```

### Island Packages

To download an island package:

```python
from dcutils.static.islands import IslandPackage

island_package = IslandPackage(uri = "/mobile/ui/heroicraces_islands/hr_71_heroicorigins.zip")

island_package.download(output = "island_package.zip")
```

### Sounds

#### Music

To download music:

```python
from dcutils.static.sounds import GeneralMusic

music = GeneralMusic(music_name = "531_dc_party_planning_island")

music.download(output = "531_dc_party_planning_island.mp3")
```

## Tools

### Calculators

#### Calculate Element Strengths

```python
from dcutils.tools.calculators import calculate_strongs

strongs = calculate_strongs(elements = ["terra", "flame"])
```
**Output:**
```
['electric', 'flame', 'nature', 'ice']
```

#### Calculate Element Weaknesses

```python
from dcutils.tools.calculators import calculate_weaknesses

weaknesses = calculate_weaknesses(first_element="terra")
```
**Output:**
```
['metal', 'war']
```

#### Calculate Orb Recall Gain

```python
from dcutils.tools.calculators import calculate_orb_recall_gain

orb_recall_gain = calculate_orb_recall_gain(dragon_level = 15, dragon_stars = 2)
```
**Output:**
```
389
```

### Calculate Attack Damage

You can calculate attack damage using the `calculate_attack_damage` function.

```python
from dcutils.tools.calculators.dragon import calculate_attack_damage

damage_info = calculate_attack_damage(
    category = 1,
    level = 50,
    attack_power=  1000,
    rank_class = 3,
    stars = 2
)
```

### Calculate

You can calculate dragon status using the `calculate_status` function.

```python
from dcutils.tools.calculators.dragon import calculate_status

status_info = calculate_status(
    category = 1,
    rarity = "R",
    level = 50,
    rank_class = 3,
    stars = 2,
    hp_runes = 5,
    damage_runes = 3,
    with_tower_bonus = True,
    extra_hp_multiplier=  0.1,
    extra_damage_multiplier = 0.05
)
```

### AI (Artificial Intelligence)

#### Elements Detector

```python
from dcutils.tools.ai.elements_detector import ElementsDetectorAI

elements_detector = ElementsDetectorAI()

elements_result = elements_detector.detect(image_path = "ui_3110_dragon_hoardereternal_1@2x.png", limit = 4)
```
**Output:**
```
[{'element': 'ice', 'confidence_score': 0.4871271550655365}, {'element': 'nature', 'confidence_score': 0.296091228723526}, {'element': 'flame', 'confidence_score': 0.16774502396583557}, {'element': 'sea', 'confidence_score': 0.03868602588772774}]
```

#### Phase Detector

```python 
from dcutils.tools.ai.phase_detector import PhaseDetectorAI

phase_detector = PhaseDetectorAI()

phase_result = phase_detector.detect(image_path="ui_3110_dragon_hoardereternal_1@2x.png")
```
**Output:**
```
{'phase': 'baby', 'confidence_score': 0.9999938011169434}
```

### URL Parser

#### Dragon URL Parser

You can parse various information from Dragon URLs:

```python
from dcutils.tools.url_parser.dragon import DragonUrlParser

# Example URLs
url_flash_animation = "https://dci-static-s1.socialpointgames.com/static/dragoncity/assets/sprites/1000_dragon_nature_skin1_3.swf"
url_spine_animation = "https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/engine/version_1_1/dragons/1000_dragon_nature_3/1000_dragon_nature_skin1_3_HD_tweened_dxt5.zip"
url_sprite = "https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/ui_1000_dragon_nature_skin1_3@2x.png"
url_thumb = "https://dci-static-s1.socialpointgames.com/static/dragoncity/mobile/ui/dragons/HD/thumb_1000_dragon_nature_skin1_3.png"

# Parse from URLs
result_flash_animation = DragonUrlParser.from_flash_animation(url_flash_animation)
result_spine_animation = DragonUrlParser.from_spine_animation(url_spine_animation)
result_sprite = DragonUrlParser.from_sprite(url_sprite)
result_thumb = DragonUrlParser.from_thumb(url_thumb)

# Get specific information
dragon_id = DragonUrlParser.get_id(url_thumb)
image_name = DragonUrlParser.get_image_name(url_thumb)
image_quality = DragonUrlParser.get_image_quality(url_sprite)
phase = DragonUrlParser.get_phase(url_sprite)
skin = DragonUrlParser.get_skin(url_sprite)
```

Each function returns relevant information parsed from the given Dragon URL.

Feel free to explore these functionalities and integrate them into your projects!

## Localization

The `Localization` class allows you to handle localization data efficiently. You can load localization from files, fetch it from an endpoint, and perform various operations on the data.

```python
from dcutils.static.localization import Localization

# Example usage
loc = Localization(language = "en")
print(loc)
```

### Methods

#### load_file

Load localization data from a file.

```python
loc = Localization.load_file(file_path = "localization.json")
```

#### load_compressed_file

Load compressed localization data from a file.

```python
loc = Localization.load_compressed_file(file_path = "localization.gz")
```

#### fetch

Fetch localization data from an endpoint.

```python
loc_data = Localization.fetch(language = "en")
```

#### get_value_from_key

Get the value from a key in the localization data.

```python
value = loc.get_value_from_key("key_name")
```

#### get_key_from_value

Get the key from a value in the localization data.

```python
key = loc.get_key_from_value("value_name")
```

#### get_dragon_name

Get the name of a dragon based on its ID.

```python
name = loc.get_dragon_name(id = 1000)
```

#### get_dragon_description

Get the description of a dragon based on its ID.

```python
description = loc.get_dragon_description(id = 1000)
```

#### get_attack_name

Get the name of an attack based on its ID.

```python
name = loc.get_attack_name(id = 1)
```

#### get_skill_name

Get the name of a skill based on its ID.

```python
name = loc.get_skill_name(id = 1)
```

#### get_skill_description

Get the description of a skill based on its ID.

```python
description = loc.get_skill_description(id = 1)
```

#### search_keys

Search for keys containing a specific query.

```python
keys = loc.search_keys(query = "search_query")
```

#### search_values

Search for values containing a specific query.

```python
values = loc.search_values(query = "search_query")
```

#### compare

Compare the current localization data with old localization data.

```python
comparison = loc.compare(old_localization = old_loc)
```

### Properties

#### list

Get the localization data as a list.

```python
loc_list = loc.list
```

#### dict

Get the localization data as a dictionary.

```python
loc_dict = loc.dict
```

Feel free to explore these functionalities and integrate them into your projects!