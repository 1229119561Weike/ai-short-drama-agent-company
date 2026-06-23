### Beat 1

**Time:** `0:00-0:15`  
**Location:** Funeral court under a black sun

**Visual**

Gold funerary dust falls toward Lyra's closed eyes while the black sun devours the sky over the necropolis.

**Dialogue Burst**

- Priest: `Seal her eyes.`
- Mourner: `The eclipse has taken her.`
(Lyra gasps awake.)
- Priest: `No--`
**Info Payload**

- Lyra was publicly declared dead
- the funeral is already underway
- her waking is impossible and witnessed

**SFX / BGM**

- Dust hiss
- Bowl crack
- `BGM_A_BLACK_SUN_LITURGY`

**Compact Consistency Prompt**

- `SCENE_ID`: `E01_B1`
- `CAST_LOCK`: `LYRA_V1{late20s|refined long-oval face|high regal cheekbones|soft-angled dark brows|large almond blue-grey eyes|straight elegant nose|soft refined jaw|medium defined bow lips|fair neutral skin|dark espresso hair|center-part sculpted wave}`
- `LOOK_LOCK`: `LYRA_L01`
- `ENV_LOCK`: `ENV_FUNERAL_COURT`
- `LOCK_CORE`: `face_shape|eye_shape|iris|nose|jaw|skin_tone|hair_color|silhouette fixed`
- `NEG_CORE`: `face drift|age drift|eye-color shift|hair-color shift|wax skin|beauty filter|plastic sci-fi|cheap costume|muddy frame|extra fingers|helmet hiding face`
- `SHOT_PROMPT`:
```text
9:16 premium cinematic opener, dead empress on white ceremonial bier over mirror-black water beneath black sun eclipse, gold funerary dust touching closed eyes, eyes snapping open at exact impact, sacred empire panic, immediate impossible hook.
```

**Mini-Hook**

A guard drives a plasma pike straight at her throat.

## Dense Short-Drama Rewrite

- Format: `YouTube-first vertical short drama`
- Ratio: `9:16`
- Episodes: `20`
- Runtime: `1 minute`
- Structure: `4 beats x 15 seconds`
- Priority: `95%+ retention logic + short-drama information density`

## Why This Version Exists

The previous version leaned too prestige-cinematic and too sparse in dialogue.

This rewrite follows strict short-drama density rules:

1. Every `15s` beat must do at least **3 jobs**:
   - visual shock
   - confrontation or power shift
   - new information or reversal
2. Every beat ends on a mini-hook, not just the episode end.
3. Dialogue is sharper, denser, and more transactional.
4. The audience should never spend more than 5 seconds without getting either:
   - a new fact
   - a new accusation
   - a new threat
   - a new reveal

## Compact Consistency System

### CAST_LOCK Library

- `LYRA_V1{late20s|refined long-oval face|high regal cheekbones|soft-angled dark brows|large almond blue-grey eyes|straight elegant nose|soft refined jaw|medium defined bow lips|fair neutral skin|dark espresso hair|center-part sculpted wave}`
- `CAEL_V1{early30s|structured oblong face|strong straight brows|narrow deep amber-brown eyes|straight clean nose|defined cheekbones|sharp noble jaw|medium-thin lips|light olive skin|near-black short textured hair}`
- `AUREN_V1{early30s|beautiful balanced face|soft expressive brows|clear grey eyes|straight aristocratic nose|medium cheekbones|refined jaw|medium lips|light neutral skin|golden-brown polished hair}`
- `SEVRA_V1{mid40s|elegant severe face|arched sculpted brows|cool dark eyes|narrow sharp nose|high sculpted cheekbones|narrow hard jaw|thin controlled lips|fair cool skin|ink-black severe hair}`
- `MOTHER_V1{ageless elder face|luminous pale skin|deep-set silver-brown eyes|smooth severe nose|noble cheek structure|ceremonial mouth line|white-metal hair halo}`
- `KID_V1{child face archive pattern|soft oval|wide blue-grey eyes|dark espresso hair}`
- `OBSERVER_V1{androgynous luminous face|impossible symmetry|silver-dark eyes|clean straight nose|calm severe mouth|pale reflective skin|black-white hair field}`

### LOOK_LOCK Library

- `LYRA_L01{imperial burial white silk shroud|gold dust|closed-eye funeral styling}`
- `LYRA_L02{desert survival veil|clean future distress|windblown dark hair}`
- `LYRA_L03{palace recovery ivory minimalism|soft controlled makeup}`
- `LYRA_L04{throne claimant black-gold tailoring|sharper queen silhouette}`
- `LYRA_L05{crisis formalwear|dust and blood continuity}`
- `LYRA_L06{solar empress regalia|clean cosmic authority}`
- `CAEL_L01{black field cloak|desert armor minimalism|war prince silhouette}`
- `CAEL_L02{palace military black|clean imperial tailoring}`
- `CAEL_L03{combat damage dark uniform|dust continuity}`
- `CAEL_L04{regent-black ceremonial powerwear}`
- `AUREN_L01{heir apparent cream-gold court tailoring}`
- `AUREN_L02{fractured public image formalwear}`
- `SEVRA_L01{regent widow couture obsidian and ivory}`
- `SEVRA_L02{ritual severity state}`
- `SEVRA_L03{collapse elegance cracking}`
- `MOTHER_L01{white-metal oracle ceremonial form}`
- `KID_L01{archive child observation uniform}`
- `OBS_L01{mirror-biological envoy form}`

### ENV_LOCK Library

- `ENV_FUNERAL_COURT{imperial open-air necropolis|white stone|mirror-black water|solar banners|high ceremonial symmetry}`
- `ENV_ECLIPSE_DESERT{vast dune moon|black sun eclipse|clean brutal horizon|monolithic future ruins|wind-carved minimalism}`
- `ENV_PALACE_SPINE{vertical imperial megastructure|ivory alloy|obsidian glass|clean sacred technology|cathedral futurism}`
- `ENV_VOID_HANGAR{colossal vertical hangar|ships suspended like cathedrals|dust-light shafts|ritual military scale}`
- `ENV_STAR_CHAMBER{circular navigation sanctum|floating stellar maps|cold gold light|precision silence}`
- `ENV_MEMORY_VAULT{clean alien archive|translucent walls|liquid light inscriptions|white-gold minimal mystery}`
- `ENV_SOLAR_THRONE{astronomical throne chamber|mechanical eclipse aperture|black-gold imperial geometry|cosmic scale}`
- `ENV_ORBIT_MIRROR{colossal orbital mirror array|blue-white vacuum light|clean extreme engineering|suspended transfer cradle|planet curve below}`
- `ENV_FIFTH_ORBIT{hidden mirror geometry|silent light architecture|alien clean stone|minimal cosmic scale}`
- `ENV_CHILD_DOME{abandoned observation dome|child-scale astronomy seats|worn white panels|ghost archive mood|small star projectors}`

### LOCK_CORE

`face_shape|eye_shape|iris|nose|jaw|skin_tone|hair_color|silhouette fixed`

### NEG_CORE

`face drift|age drift|eye-color shift|hair-color shift|wax skin|beauty filter|plastic sci-fi|cheap costume|muddy frame|extra fingers|helmet hiding face`

### BGM Library

- `BGM_A_BLACK_SUN_LITURGY`
- `BGM_B_DESERT_VELOCITY`
- `BGM_C_PALACE_GLASS`
- `BGM_D_THRONE_HUNGER`
- `BGM_E_MEMORY_KNIFE`
- `BGM_F_MIRROR_RETURN`
- `BGM_G_SOVEREIGN_BURN`

---
