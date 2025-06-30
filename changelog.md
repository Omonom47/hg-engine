## Tutorials, tools, general good to knows and docs
https://www.youtube.com/watch?v=JBis6l0GQOs&list=PLxQnhmMQpMGmKz1fOalSuAyCnXz_-sS5f
DSPRE scripting commands: https://docs.google.com/spreadsheets/d/1rcrCz9Y5HXdD9vVSmkACX19I9Jid4dzFTD0PXaIDg2w/edit?gid=1273858621#gid=1273858621 
What changes are missing in hg-engine: https://docs.google.com/spreadsheets/d/1IXiiganrLLbAX6TsPSiC_RMNXuyB_Nr-HMV3W_dn8yQ/edit?gid=0#gid=0
https://ds-pokemon-hacking.github.io/getting-started/hgss/ 
https://ds-pokemon-hacking.github.io/assets/files/asm1-dfe448d0629040cb8da4ced54a0ed182.pdf 
https://ds-pokemon-hacking.github.io/docs/generation-iv/guides/hgss-new_script_commands/ 
https://drive.google.com/drive/folders/1C8rjzcJc_1x23n7rF0oK8TLYnV3YdHxL 
https://ds-pokemon-hacking.github.io/ 
https://github.com/pret/pokeheartgold/blob/c7d8718086b5ba6e27a0d04e1d284d6693239576/include/constants/vars.h 
https://github.com/pret/pokeheartgold/blob/c7d8718086b5ba6e27a0d04e1d284d6693239576/include/constants/flags.h 


If level cap variable is not set then no exp is earned

commonscript 2008 give an item determined by var 0x8004 and amount determined by var 0x8005

## Known issues:
- Using speedup during the intro causes character sprites in the overworld get corrupted after the first battle and leaving route 29 through the gate and coming back
		saving and restarting seems to fix it at least temporarily.
- Infestation not implemented properly but exists in several learnsets
- playing for a while with speedup seems to cause graphical issues

## TO DO
- ?update safari zone encounters?
- Replace dialogue of npc on route 32 that originally gave roar tm
- ?Make game corner pokemon maybe/always have hidden ability?
- ?make lvl cap be more granular in Kanto?
- change item given by Janine after defeating her (script 809, function #7)
- change item given by Blue after defeating him (script 743, function #3)
- change item given by Brock after defeating him (script 752, function #3)
- Make fishing rods available earlier
- ?replace flash with item?

## RIVAL FIGHTS:
 - CHERRYGROVE: lvl 5 only starters available
 - Azalea: lvl 14, 16 & 18
 - Burned Tower: lvl 18, 20, 20, 22
 - Goldenrod tunnel: lvl 30, 32, 32, 34, 34 (for some reason the lvls are 2 lower if you choose cyndaquil)
 - Victory road: lvl 38, 39, 39, 39, 40, 42

## TRAINERS: 
lvl boosts are relative to previous major battle

- KANTO GYM LEADERS: adjust lvls, movesets and maybe team comps a bit
		

## ITEMS: 
https://www.serebii.net/heartgoldsoulsilver/items.shtml

https://bulbapedia.bulbagarden.net/wiki/List_of_items_by_index_number_in_Generation_IV

https://www.serebii.net/heartgoldsoulsilver/tmhm.shtml 

https://github.com/msikma/pokesprite/blob/master/items/tm/flying.png 

ground item script x is script x+1 in file 141 in DSPRE
### replaceable items

- potion on route 30 with some oran berries
- potion on route 31 with something
- x-attack in union cave with something 
- awakening in union cave with something
- potion in union cave with something
- x-attack in ilex forest with something 
- antidote in ilex forest with something
- ether in ilex forest with something
- parlyz heal on route 35 with something
- max repel on route 44 with something
- ultra ball on route 44 with something
- revive on route 45 with something
- x-speed on route 46 with something   
- ?tm77 in viridian forest? 
- ?tm29 in Saffron city? 
- ?TRICK ROOM given by leader blue to other tm/item?
- ?POISON JAB given by leader Janine to other tm/item?
- ?Flamethrower tm on route 28(before mt.silver) to other item? 
- ?rock slide tm given by Brock to other item? 
- Potion in ruins of alph
- ?Oran berry in ruins of alph Upper right (requires 1 escape rope)?
- ?heal powder in ruins of alph lower right 2 (requires surf and flash)?
- ?energy root in ruins of alph lower right 2 (requires surf and flash)?
- ?charcoal in ruins of alph upper left 2 (requires surf and Ho-oh)?
- ?mystic water in ruins of alph lower left 2 (requires surf, strength and water stone)?
- ?Stardust in ruins of alph lower left 2 (requires surf, strength and water stone)?
- ?Star piece in ruins of alph lower left 2 (requires surf, strength and water stone)?


### make available earlier
    - Stone edge tm71
    - x-scissor tm81
    - Giga drain tm19
    - Gyro ball tm74
    - Super Rod
- make available without pokewalker:
	- ?LIGH BALL?

    

## Moves

infestation is not yet implemented, either remove it from learnsets or implement it

## Encounters
most surf and fishing encounters will be rebalanced/changed

most headbutt encounters will be rebalanced/changed

## Shops and marts

- Goldenrod gamecorner prices will be lowered
- Pokeathlon dome prize redeem prices for evolution items will be lowered
- Pokeathlon dome evolution items will be made available all days of the week
- Safari Zone Gate: maybe change vitamin shop into something else
- Tentative: Mahogany town shop now sells: toxic orb, flame orb, leftovers, black sludge, tm13, tm24, tm35, tm29

## Pokemons to change: 

Give more mons trick room by level up/make the tm availbe earlier

https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Johto_Pok%C3%A9dex_number

https://bulbapedia.bulbagarden.net/wiki/Ability#List_of_Abilities 
- Qwilfish: maybe implement TOXIC DEBRIS

Generally look at encounter rates/locations + learnsets,

some pokemon would be more interresting with hidden ability being standard ability:
- Butterfree line currently no ability2 but has hidden ability
- Beedrill line currently no ability2 but has hidden ability
- Spearow/Fearow no ability2 but has hidden ability
- Raichu currently no ability2 but has hidden ability
- Zubat-line currently no ability2 but has hidden ability
- Magikarp-line currently no ability2 but has hidden ability
- Sandslash currently no ability2 but has hidden ability
- Victreebel currently no ability2 but has hidden ability, but ha sucks
- Vileplume currently no ability2 but has hidden ability
- Bellossom currently no ability2 but has hidden ability
- Dugtrio line currently has sand veil as ability1, prefer to not have evasion stuff
- Ditto currently no ability2 but has hidden ability
- Exeggcutor currently no ability2 but has hidden ability
- Wobbuffet currently no ability2 but has hidden ability
- Ampharos line curremntly no ability2 but has hidden ability, hidden ability might not really work
- Magmortar currently no ability2 but has hidden ability
- Electivire currently no ability2 but has hidden ability
- Quagsire has DAMP as ability1 and more interresting hidden ability
- Farfetch has a more interresting hidden ability than both base abilities
- Mamoswine has a more interresting hidden ability than both base abilities
- Poliwrath has a more interresting hidden ability than both base ability
- Corsola has a more interresting hidden ability than one base abilitiy

Make it possible for wild encounters to have hidden ability, 20% chance

all tm- and tutorlearnsets may need revisions 

## Implemented changes:

- EVO METHODS: trade with held item is now stone evo with said item instead
- Goldenrod game corner prices now lowered
- Makes all pokemon sold in Goldenrod game corner available regardles of game version 


### Level caps
- 13, set after recieving starter
- 17, set after beating Falkner
- 20, set after beating Bugsy
- 25, set after beating Whitney
- 30, set after beating Morty
- 33, after beating 5th gym leader
    - set after beating Chuck 
    - Set after beating Price as the 5th gym
    - Set after beating Jasmine as the 5th gym
- 35, after beating 6th gym leader
    - set after beating Chuck 
    - Set after beating Price as the 6th gym
    - set after beating Jasmine
- 43, after beating 7th gym leader
    - set after beating Chuck 
    - Set after beating Price
    - set after beating Jasmine
- 56, set after beating Clair
- 100, after beating lance first time

### Moves
- Wild charge:
    - power 90 -> 100
    - RECOIL_THIRD -> RECOIL_QUARTER
- Brutal swing
    - power: 60 -> 90
    - pp: 20 -> 15
- Fire, ice, & thunder fang
    - acc: 95 -> 100

### Items

- Full heal: price: 600 -> 475
- LUCKY EGG: price: 200 -> 3000
- KINGs ROCK: 
    - price: 100 -> 2100
    - evolves Slowpoke into Slowking on use
- METAL COAT:
    - Price: 100 -> 2100
    - evolves Scyther into Scizor on use
- SILVER POWDER: price: 100 -> 1000
- MAGMARIZER: evolves Magmar into Magmortar on use
- ELECTIRIZER: evolves Electabuzz into Electivire on use
- PROTECTOR: evolves Rhydon into Rhyperior on use
- DRAGON SCALE: evolves Seadra into Kingdra on use
- UP-GRADE: evolves Porygon into Porygon2 on use
- DUBIOUS DISC: evolves Porygon2 into Porygon Z on use
- DAMP ROCK, HEAT ROCK, 2nd store clerk Ecruteak 
- ICY ROCK, SMOOTH ROCK, 2nd store clerk Violet

#### TMs
- TM05: ROAR -> DEFOG
- TM20: SAFEQUARD -> FIRE FANG
- TM21: FRUSTRATION -> PLAY ROUGH
- TM27: RETURN -> DAZZLING GLEAM
- TM32: DOUBLE TEAM -> ELECTROWEB
- TM41 Torment -> HURRICANE
    sold in Goldenrod dept store
- TM43: SECRET POWER -> HYPER VOICE
- TM45: ATTRACT -> BUG BUZZ
    Sold in Goldenrod game corner
- TM49: SNATCH -> POWER GEM
- TM58: ENDURE -> ICE FANG
- TM63: Embargo  -> CURSE
- TM77: PSYCH UP -> BRUTAL SWING
    sold in goldenrod dept store
- TM78: CAPTIVATE -> THUNDER FANG
- TM83: Natural Gift -> TAILWIND
- TM87: SWAGGER -> WILD CHARGE

- reward from Whitney: TM45 -> TM54
- Goldenrod game corner: TM44 -> TM32 
- Goldenrod game corner: TM13 -> TM58 
- Goldenrod game corner: TM24 -> TM78
- Goldenrod game corner: TM35 -> TM20
- TM13: now sold in mahogany town after radio tower takeover
- TM19: replaces bright powder in goldenrod radio tower 4f (given by npc after rocket)
- TM24: now sold in mahogany town after radio tower takeover
- TM29: now sold in mahogany town after radio tower takeover
- TM31: replaces tm57 in olivine city (reuires surf)
- TM35: now sold in mahogany town after radio tower takeover
- TM53: replaces tm54 in dark cave
- TM61: replaces TM12 in burned tower
- TM71: replaces heal powder in ruins of alph Upper right (requires 1 escape rope)
- TM73: replaces energy powder in ruins of alph Upper right (requires 1 escape rope)
- TM78: replaces energy powder in ruins of alph Upper right (requires 1 escape rope)
- TM80: replaces tm60 on route 39
- TM84: replaces TM65 on route 42

#### Pokemarts
- All marts
    - Full heals replace all rtatus restore items
    - Ether & Elixirs are now available replacing status restoration items
    - Max revives are now available
- Goldenrod Dept Store
    - All evolution stones/items
    - Lucky egg
    - Heart scale
    - Everstone
    - Nature mints
    - Ability capsules
    - Pixie plate
    - Silver Powder
    - TM70 -> TM92
    - TM54 ->TM77
    - TM83 ->TM41
    - Lottery now more generous odds of first place

### Major Trainer battles

- rocket hq highest lvl is 30
- trainers in Goldenrod radio tower + tunnel
- All kimono girls now have lvl 43

#### RIVAL FIGHTS:
 - Burned Tower: 
    - mon1:Gastly: lvl 20
    - mon2:Magnemite: lvl 18 -> 20
    - mon3:Zubat:lvl 20 -> 21
    - mon4:Starter: lvl 22
 - Goldenrod tunnel: lvl 30, 32, 32, 34, 34 (for some reason the lvls are 2 lower if you choose cyndaquil)
 - Victory road: lvl 38, 39, 39, 39, 40, 42
 - Mt. Moon:
    - mon1: Sneasel -> Weavile, lvl 46 -> 63
        - QUICK ATTACK -> ICE SHARD
    - mon2: lvl 47 -> 64
        - AIR CUTTER -> AIR SLASH
    - mon3: Magneton -> Magnezone, lvl 46 -> 63
        - MAGNET BOMB -> FLASH CANNON
    - mon4: lvl 48 -> 65
    - mon5: lvl 48 -> 65
    - mon6: lvl 50 -> 67
        - MEGANIUM
            - LIGHT SCREEN -> MOONBLAST
        - TYPHLOSION
            - QUICK ATTACK -> SCORCHING SANDS
        - FERALIGATR

#### Johto gymleaders

- Falkner: ace lvl 13
    - mon1: Pidgey -> Spearow
        - ivs: 15, 15, 0, 10, 0, 0
        - nature: Impish
    - mon2:
        - ivs: 15, 10, 10, 0, 10, 0
        - nature: Relaxed
- Bugsy: ace lvl 17
    - mon1: (ace)
        - ability: technician
        - ivs: 15, 15, 15, 15, 0, 0
        - evs: 0, 40, 0, 0, 0, 0 
        - nature: Adamant
    - mon2: Kakuna -> Ledyba
        - ability: Swarm
        - ivs: 15, 15, 0, 15, 0, 5
        - nature: Jolly
    - mon3: Metapod -> Spinarak
        - ability: adaptibility
        - ivs: 15, 15, 0, 10, 0, 10
        - nature: Impish
        
- Whitney: ace lvl 20
    - mon1: Clefairy -> Jigglypuff
        - ability: Competitive
        - ivs: 15, 0, 15, 15, 15, 15
        - nature: Timid
    - mon2: Miltank -> Clefairy
        - ability: Cute charm
        - ivs: 10, 15, 10, 15, 15, 10
        - nature: Hardy
    - mon3: NONE -> Miltank (ace)
        - ability: Scrappy
        - ivs: 20, 15, 25, 15, 0, 15
        - evs: 20, 0, 0, 0, 0, 0 
        - nature: Hasty


- Morty: ace lvl 25
    - mon1: Gastly -> Misdreavus
        - ability: Levitate
        - ivs: 15, 15, 15, 15, 15, 15
        - nature: Timid
    - mon2: Haunter -> Noctowl
        - ability: Tinted lens
        - ivs: 15, 15, 15, 15, 15, 15
        - nature: Bold
    - Mon3: Gengar (ace): replaces HYPNOSIS with FOCUS BLAST
        - ability: Cursed body
        - ivs: 25, 0, 20, 15, 20, 15
        - nature: Hardy
    - Mon4: Haunter: replaces NIGHT SHADE with SHADOW BALL
        - ability: Levitate
        - ivs: 15, 15, 15, 15, 15, 15
        - nature: Timid

- Chuck: 
    - As 5th gym: ace lvl 30, trainerdata 34
        - mon1: Primeape: moveset changed
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Careful
        - mon2: Poliwrath -> Hitmontop
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Impish
        - mon3: NONE -> Poliwrath (ace): moveset changed
            - ivs: 31, 20, 20, 20, 20, 20
            - nature: Careful
    - As 6th gym: ace lvl 33, trainerdata 11
        - mon1: Primeape: lvl 31
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Careful
        - mon2: Hitmontop: lvl 31
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Impish
        - mon3: Poliwrath (ace): replaces HYPNOSIS with SUBSTITUTE 
            - ivs: 31, 31, 25, 25, 25, 15
            - nature: Careful
    - As 7th gym: ace lvl 35, trainerdata 19
        - mon1: Primeape: lvl 33, replaces ASSURANCE with BRUTAL SWING
        - mon2: Hitmontop: lvl 33
        - mon3: Poliwrath (ace): replaces BODY SLAM with BRUTAL SWING 
- Jasmine:
    - as 5th gym, ace lvl 30, trainerdata 40
        - mon1: Magnemite: lvl 28
            - ability: Sturdy
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Modest
        - mon2: Forretress: lvl 28
            - ability: Sturdy
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Careful
        - mon3: Steelix (ace)
            - ability: Sturdy
            - ivs: 20, 31, 20, 20, 20, 20
            - nature: Adamant
    - As 6th gym, ace lvl 33, trainerdata 33
        - mon1: Magnemite -> Magneton: lvl 30 -> 31 
            - SONIC BOOM -> TRI ATTACK
            - ability: Sturdy
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Modest
        - mon2: Magnemite -> Forretress: lvl 31
            - ability: Sturdy
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Careful
        - mon3: Steelix (ace): 
            - SCREECH -> THUNDER FANG 
            - ROCK THROW -> EARTHQUAKE
            - ability: Sturdy
            - ivs: 25, 31, 31, 25, 25, 15
            - nature: Adamant
    - As 7th gym, ace lvl 35, trainerdata 63
        - mon1: Magneton: lvl 33, replaces SUPERSONIC with FLASH CANNON
        - mon2: Forretress: lvl 33
        - mon3: Steelix (ace): Replaces SANDSTORM with ICE FANG
- Pryce: 
    - as 5th gym, ace lvl 30, trainerdata 87
        - mon1: Delibird: lvl 28
            - ability: Snow warning
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Modest
        - mon2: Seel: lvl 28
            - ability: Ice body
            - ivs: 20, 20, 20, 20, 20, 20
            - nature: Bold
        - mon3: Piloswine (ace): 
            - ability: Thick fat
            - ivs: 31, 20, 20, 20, 20, 20
            - evs: 0, 0, 0, 0, 0, 48
            - nature: careful
    - as 6th gym, ace lvl 33, trainerdata 88
        - mon1: Delibird: lvl 30
            - ability: Snow warning
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Modest
        - mon2: Dewgong: lvl 32
            - ability: Ice body
            - ivs: 25, 25, 25, 25, 25, 25
            - nature: Bold
        - mon3: Piloswine (ace):
            - ability: Thick fat
            - ivs: 31, 25, 25, 25, 25, 25
            - evs: 0, 0, 0, 0, 0, 48
            - nature: Careful
    - as 7th gym, ace now lvl 35, trainerdata 32
        - mon1: Seel -> Delibird: lvl 33
        - mon2: Dewgong: lvl 32 -> 33, Replaces ICE SHARD with SURF and AURORA BEAM with BLIZZARD
        - mon3: Piloswine -> Mamoswine (ace): lvl 34 -> 35, better moves
- Clair: ace lvl 43
    - mon1: Gyarados: moveset changed
    - rest unchanged

#### ELITE FOUR (first battle): 

All levels increased by 2 or 3

- Will:
    - mon1: lvl 40 -> 43
    - mon2: lvl 41 -> 44
    - mon3: lvl 41 -> 44
    - mon4: lvl 41 -> 44
    - mon5: lvl 42 -> 46
- Koga:
    - mon1: lvl 40 -> 44
    - mon2: Venomoth -> Nidoking, lvl 41 -> 45
        - POISON JAB
        - EARTHQUAKE
        - ICE BEAM
        - THUNDERBOLT
    - mon3: Forretress -> Weezing, lvl 43 -> 45
        - PROTECT
        - SLUDGE BOMB
        - EXPLOSION
        - FLAMETHROWER
    - mon4: lvl 42 -> 45
        - MINIMIZE -> CURSE
        - SCREECH -> DRAIN PUNCH
    - mon5: lvl 44 -> 48
        - DOUBLE TEAM -> SHADOW BALL
        - QUICK ATTACK -> HEAT WAVE
        - POISON FANG -> SLUDGE BOMB
- Bruno:
    - mon1: lvl 42 -> 46
    - mon2: lvl 42 -> 46
    - mon3: lvl 42 -> 46
    - mon4: Onix -> Heracross, lvl 43 -> 47
        - MEGAHORN
        - EARTHQUAKE
        - BRICK BREAK
        - ROCK SLIDE
    - mon5: lvl 46 -> 50
- Karen:
    - mon1: lvl 42 -> 46
        - DOUBLE TEAM -> MOONLIGHT
        - FEINT ATTACK -> DARK PULSE
        - PAYBACK -> PSYCHIC
    - mon2: Vileplume -> Victreebel, lvl 42 -> 46
        - CRUNCH
        - SLEEP POWDER
        - SWORDS DANCE
        - LEAF BLADE
    - mon3: lvl 45 -> 49
        - SPITE -> SHADOW BALL
        - LICK -> SLUDGE BOMB
    - mon4: Murkrow -> Honchkrow, lvl 44 -> 48
        - PLUCK
        - TAILWIND
        - SUCKER PUNCH
        - NIGHT SLASH
    - mon5: lvl 47 -> 52
- Lance: ?change mons? (now ace lvl 56)
    - mon1: lvl 46 -> 50
        - FLAIL -> IRON HEAD
    - mon2: lvl 49 -> 53
    - mon3: lvl 40 -> 53
    - mon4: lvl 48 -> 52
    - mon5: lvl 48 -> 52
    - mon6: lvl 50 -> 56

#### Kanto Gym leaders
now have their rematch teams with modifications

- Brock: lvl total 338 -> 392
    - mon1: lvl 55 -> 64
    - mon2: Relicanth -> Cradily, lvl 54 -> 65
        - GIGA DRAIN
        - STOCKPILE
        - SLUDGE BOMB
        - ROCK SLIDE
    - mon3: lvl 56 -> 64
        - BRINE -> SURF
        - SANDSTORM -> ICE BEAM
    - mon4: MIGHT BE CHANGED LATER, lvl 61 -> 68
        
    - mon5: lvl 55 -> 65
        - ENDURE -> NIGHT SLASH
        - GIGA DRAIN -> LEECH LIFE
    - mon6: lvl 57 -> 66

- Misty: lvl total 340 -> 356
    - mon1: lvl 60 -> 62
    - mon2: lvl 56 -> 57
        - WATER PULSE -> SCALD 
        - AMNESIA -> SLUDGE BOMB
    - mon3: lvl 56 -> 59
    - mon4: lvl 54 -> 58
    - mon5: lvl 54 -> 58
    - mon6: lvl 60 -> 62

- Lt. Surge: lvl total 330 -> 344
    - mon1: lvl 60
    - mon2: lvl 52 -> 55
    - mon3: lvl 52 -> 58
        - DOUBLE TEAM -> TRI ATTACK
        - MIRROR SHOT -> FLASH CANNON
    - mon4: lvl 52 -> 55
        - DOUBLE TEAM -> MAGNET RISE
    - mon5: lvl 58
        - QUICK ATTACK -> U-TURN
        - SWEET KISS -> NUZZLE
    - mon6: lvl 56 -> 58

- Erika: lvl total 334 -> 356
    - mon1: lvl 54 -> 57
        - LEAF STORM -> LEAF BLADE
        - EXPLOSION -> ROCK SLIDE
    - mon2: lvl 53 -> 59
        - MEMENTO -> TAILWIND
    - mon3: lvl 56 -> 60
        - NATURAL GIFT -> THUNDER FANG
        - SLUDGE BOMB -> POISON JAB
        - LEAF STORM -> CRUNCH
    - mon4: lvl 56 -> 60
        - ATTRACT -> QUIVER DANCE
    - mon5: lvl 60 -> 62
    - mon6: lvl 55 -> 58

- Janine: lvl total 332 -> 368
    - mon1: lvl 52 -> 60
        - CONFUSE RAY -> TAILWIND
    - mon2: lvl 56 -> 59
    - mon3: lvl 52 -> 60
        - CROSS CHOP -> BRICK BREAK
        - ATTRACT -> SUCKER PUNCH
    - mon4: lvl 58 -> 63
        - TOXIC -> STICKY WEB
        - BOUNCE -> X-SCIZOR
        - SWAGGER -> PROTECT
        - NIGHT SHADE -> NIGHT SLASH
    - mon5: lvl 59 -> 64
        - DOUBLE TEAM -> ENERGY BALL
    - mon6: lvl 55 -> 62
        - CONFUSE RAY -> EARTHQUAKE

- Sabrina: lvl total 334 -> 380
    - mon1: lvl 60 -> 66
        - GRAVITY -> SHADOW BALL
    - mon2: lvl 58 -> 64
    - mon3: lvl 56 -> 64
        - THUNDER -> DAZZLING GLEAM
    - mon4: lvl 54 -> 61
    - mon5: lvl 53 -> 61
    - mon6: lvl 53 -> 64

- Blaine: lvl total 346 -> 404
    - mon1: lvl 54 -> 67
        - Ability: White smoke -> drought
        - SUNNY DAY -> EARTHQUAKE
        - BODY SLAM -> SOLAR BEAM
    - mon2: lvl 57 -> 67
    - mon3: lvl 60 -> 68
        - QUICK ATTACK -> PLAY ROUGH
    - mon4: lvl 58 -> 65
        - STONE EDGE -> POWER GEM
        - GYRO BALL -> EARTH POWER
        - CURSE -> RECOVER
    - mon5: lvl 54 -> 67
    - mon6: lvl 62 -> 70
        - LOW KICK -> FOCUS BLAST
    
- Blue: currentl lvl total 416
    - mon1: lvl 67
        - PSYCHIC -> PSYSCHOCK
        - EXPLOSION -> ANCIENT POWER
    - mon2: lvl 69
        - ATTRACT -> POISON JAB
    - mon3: lvl 70
        - THUNDER FANG -> WILD CHARGE
    - mon4: lvl 68
    - mon5: lvl 70
        - LOW KICK -> CRUNCH
    - mon6: lvl 72
        - DOUBLE TEAM -> ROOST


#### ELITE FOUR (after 16 badges)
- Will: lvl total 360 -> 426
    - mon1: lvl 58 -> 69
        - GRAVITY -> GYRO BALL
    - mon2: lvl 60 -> 71
    - mon3: lvl 59 -> 70
    - mon4: lvl 60 -> 71
        - CURSE -> CALM MIND
        - AMNESIA -> FLAMETHROWER
        - BODY SLAM -> SURF
    - mon5: lvl 61 -> 72
        - CHARGE BEAM -> MOONBLAST
    - mon6: lvl 62 -> 73
        - QUICK ATTACK -> AIR SLASH

- Koga: lvl total 372 -> 438
    - mon1: lvl 61 -> 72
        - EXPLOSION -> POSION JAB
    - mon2: lvl 63 -> 74
        - DOUBLE TEAM -> ENERGY BALL
        - SILVER WIND -> QUIVER DANCE
    - mon3: lvl 60 -> 71
    - mon4: lvl 62 -> 73
        - ability: STICKY HOLD -> POISON TOUCH
        - MINIMIZE -> POISON JAB
        - SCREECH -> CURSE
        - SWAGGER -> DRAIN PUNCH
        - TOXIC -> BRUTAL SWING
    - mon5: lvl 64 -> 75
        - MEAN LOOK -> ROOST
        - FLY -> AIR SLASH
        - CROSS POISON -> SLUDGE BOMB
    - mon6: lvl 62 -> 73

- Bruno: lvl total 374 -> 446
    - mon1: lvl 62 -> 74
        - QUICK ATTACK -> BRUTAL SWING
    - mon2: lvl 61 -> 73
        - SWAGGER -> ROCK SLIDE
        - REVERSAL -> POISON JAB
    - mon3: lvl 61 -> 73
    - mon4: lvl 62 -> 74
        - LOW KICK -> VACUUM WAVE
        - PAYBACK -> FAKE OUT
        - BULK UP -> BELLY DRUM
    - mon5: lvl 64 -> 76
        - FORESIGHT -> BRUTAL SWING
    - mon6: lvl 64 -> 76
        - CLOSE COMBAT -> AURA SPHERE
        - COUNTER -> EARTHQUAKE
        - IRON TAIL -> FLASH CANNON

- Karen: lvl total 377 -> 454
    - mon1: lvl 62 -> 76
        - ability: pressure -> technician
        - NIGHT SLASH -> PAYBACK
        - ICE PUNCH -> AVALANCHE
    - mon2: lvl 62 -> 74
    - mon3: lvl 62 -> 75
    - mon4: lvl 64 -> 77
        - WHIRLWIND -> STEEL WING
        - SUCKER PUNCH -> NIGHT SLASH
    - mon5: lvl 63 -> 75
    - mon6: lvl 64 -> 77

- Lance: lvl total 428 -> 468
    - mon1: lvl 72 -> 78
    - mon2: lvl 68 -> 76
        - THUNDER WAVE -> CRUNCH
    - mon3: lvl 72 -> 78
        - ROAR -> IRON HEAD
    - mon4: lvl 73 -> 79
        - DRAGON BREATH -> DRAGON PULSE
        - DOUBLE TEAM -> FLAMETHROWER
        - HYPER BEAM -> HYPER VOICE
    - mon5: lvl 68 -> 76
    - mon6: lvl 75 -> 81
        - FIRE BLAST -> IRON HEAD
        - SAFEGUARD -> DRAGON DANCE
        - DRACO METEOR -> DRAGON CLAW
        - HYPER BEAM -> EARTHQUAKE

### Updated wild Encounters and regular trainers battles
Walking enounter rates per slot are: 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1

Surf enounter rates per slot are: 60, 30, 5, 4, 1

Fishing enounter rates per slot are: 40, 40, 15, 4, 1

Rock smash encounter rates per slot are : 90, 10

(headbutt encounters unchanged unless noted)
#### Johto
- Vcitory road: lvls increased
- route 26: grass + surf, trainers + rematches
- route 27: grass encounter table, trainers + remathces
- Tohjo falls: +4 lvls to walking encounters, replaces Rattata with Tyrogue
- route 28:
- New Bark Town: increased rate of Shellder, now encounterable with old rod
- Cherrygrove city: Replace Corsola with Qwilfish, make Qwilfish & Kinlger more likely to, Qwilfish available with old rod
- route 30: grass and surf
- route 31: grass and surf
- violet city: surf lvls
- route 32: grass
- Union cave: walking, Phanpy replaces zubat on b1f in the two 10% slots
- route 33: grass
- ilex forest: walking and headbutt
- route 34: grass and headbutt
- route 35: grass
- route 36: grass
- route 37: grass
- burned tower B1F: Slugma added to encounters
- bell tower: lvls increased, adds raticate, haunter & misdreavus
- route 38: grass, trainer lvls
- route 39: grass
- Olivine: Make Corsola & Kingler more likely to appear by fishing
- route 40: fishing & surf, trainer lvls
- route 41: fishing & surf, trainer lvls
- whirl islands: All lvls increased. Golbat more likely on 1f & b1f, and completely replaces zubat on b2f & b3f. Kingler now appears as walking encounter on b2f and b3f 
- route 42: grass, trainer lvls, adds Murkrow to morning & night
- Mt. Mortar: walking encountertable and surf
- Mahogany rocket hideout: TODO trainer lvls
- Mahogany gym: trainer lvls
- route 43: grass and surf lvls, replaces Mareep with Teddiursa at night, trainers
- Lake of Rage: surf lvls
- route 44: grass lvls, Bellsprout -> Teddiursa, trainers
- Ice path: lvls increased, Delibird added to encounters
- Blackthorn city: surf lvls increased, Remoraid added to encounters
- Dragons den: slight increase in lvls, Dratini more likely to appear
- route 45: grass lvls increased, Skarmory added, trainers
- Dark cave: both sides lvls & encounter rates
- Cliff cave: increased encounter rate of Misdreavus, Graveller, and Machoke, removes Zubat, Krabby, Wooper, and Quagsire from walking encounters
- route 47: surf
- route 48: grass encountertable

#### Kanto
- route 1: trainers
- route 2: trainers + rematches
- Viridian forest: trainers
- route 4: trainers (some teamcomp alterations)
- route 6: trainers
- route 8: trainers
- route 9: trainers
- route 10: trainers
- route 11: trainers (some teamcomp alterations)
- route 12: trainers (some teamcomp alterations) + rematches
- route 13: trainers (some teamcomp alterations) + rematches
- route 14: trainers (some teamcomp alterations) + rematches
- route 15: trainers (some teamcomp alterations) + rematches
- route 17: trainers
- route 18: trainers
- route 19: trainers (some teamcomp alterations)
- route 20: trainers (some teamcomp alterations)
- route 21: trainers (some teamcomp alterations)
- route 24: trainers
- route 25: trainers


### Pokemon

Several pokemon have been made available earlier in the game

all starters 85/15 -> 50/50 gender ratio

    Cloyster:
        ability1: SHELL ARMOR -> WATER ABSORB
    Bayleef:
        GRASS/GRASS -> GRASS/FAIRY
    Meganium: 
        GRASS/GRASS -> GRASS/FAIRY
        hp: 80 -> 100
        atk: 82 -> 54
        spa: 83 -> 95
        new learnset
    Feraligatr: 
        WATER/WATER -> WATER/DRAGON
        atk: 105 -> 109
        new learnset
    Typhlosion: 
        FIRE/FIRE -> FIRE/GROUND
        new learnset
	Sentret: 
		ability1: RUN AWAY -> SAND RUSH
	Furret: 
		hp: 85 -> 80
		atk: 76 -> 96
		ability1:RUN AWAY -> SAND RUSH
    Ledyba: 
        BUG/FLYING -> BUG/BUG
        hp: 40 -> 45
        atk: 20 -> 45
        spa: 40 -> 25
        spdef: 80 -> 60
        spe: 55 -> 60 
        hidden ability: IRON FIST -> NONE
        learnset
    Ledian:
        BUG/FLYING -> BUG/FIGHTING
        hp: 55 -> 61
        atk: 35 -> 90
        spa: 55 -> 35
        spdef: 110 -> 80
        spe: 85 -> 94 
        ability2: EARLY BIRD -> IRON FIST
        hidden ability: IRON FIST -> NONE
        learnset
	Hoothoot:
		spdef: 56 -> 66
	Noctowl: 
		NORMAL/FLYING -> GHOST/FLYING
		hp: 100 -> 105
		atk: 50 -> 40
		spdef: 96 -> 124
		spe: 70 -> 67
		ability2: KEEN EYE -> REGENERATOR
        notable new moves: TRICK ROOM, SHADOW BALL
    Spinarak:
        atk: 60 -> 70
        spa: 40 -> 30
        spe: 40 -> 20
        ability1:  SWARM -> ADAPTABILITY
    Ariados: 
        BUG/POISON -> BUG/DARK
        hp: 70 -> 85
        atk: 90 -> 125
        spa: 60 -> 40
        spe: 40 -> 35
        ability1:  SWARM -> ADAPTABILITY
    Shuckle:
        hp: 20 -> 60
        def: 230 -> 210
        spdef: 230 -> 210
        ability2: GLUTTONY -> FILTER
    Delibird: 
        hp: 45 -> 65
        atk: 55 -> 40
        spa: 65 -> 115
        spdef: 45 -> 55
        spe: 75 -> 120
        ability2: HUSTLE -> SNOW WARNING
    Qwilfish:
        hp: 65 -> 95
        atk: 95 -> 95
        def: 85 -> 100
        spa: 55 -> 30
        spdef: 55 -> 60
        spe: 85 -> 90
        notable new moves: RAPID SPIN
    Yanmega: 
        BUG/FLYING -> BUG/DRAGON
    Houndour: 
        can be found on route 34
    Phanpy:
        ability2: NONE -> SAND FORCE
    Donphan: 
        hp: 90 -> 120
        spa: 60 -> 50
        spe: 50 -> 40
        ability2: NONE -> SAND FORCE
    Corsola: 
        hp:65 -> 75
        atk: 55 -> 40
        def: 95 -> 100
        spa: 65 -> 85
        spdef: 95 -> 100
        spe: 35 -> 25
        abilities1: HUSTLE -> SOLID ROCK
        notable new moves: trick room
    Girafarig: 
        NORMAL/PSYCHIC -> DARK/PSYCHIC
        hp: hp 70 -> 65
        atk: 80 -> 90
        spa: 90 -> 100
        spe: 85 -> 90
        ability2: EARLY BIRD -> SHEER FORCE
    Stantler:
        NORMAL/NORMAL -> NORMAL/PSYCHIC
        hp: 73 -> 90
        atk: 95 -> 100
        def: 62 -> 60
        spa: 85 -> 80
        ability2: FRISK -> RECKLESS
    Chinchou:
        hp: 75 -> 95
        atk: 32 -> 20
        spa: 56 -> 69
        spe: 67 -> 62
        ability2: ILLUMINATE-> WATER ABSORB
        hidden ability: WATER ABSORB -> LIGHTNING ROD
    Lanturn:
        hp: 125 -> 170
        atk: 58 -> 30
        spa: 76 -> 94
        spe: 67 -> 62
        ability2: ILLUMINATE-> WATER ABSORB
        hidden ability: WATER ABSORB -> LIGHTNING ROD
    Mantine: 
        atk: 30 -> 40
        spa: 80 -> 85
        spe 70 -> 95
        notable new moves: defog
    Sunflora: 
        GRASS/GRASS -> GRASS/FIRE
        hp: 75 -> 80
        atk: 75 -> 60
        def: 55 -> 75
        spe: 30 -> 45
        notable new moves: FIERY DANCE, OVERHEAT
    Jumpluff:
        hp: 75 -> 85
        ability2: LEAF GUARD -> FUR COAT
        notable new moves: TAILWIND
    Slugma:
        hp: 40 -> 55
        def: 40 -> 65
        spdef: 40 -> 50
    Magcargo:
        hp: 60 -> 107
        spa: 90 -> 97
        spdef: 70 -> 96
        ability1: MAGMA ARMOR -> SOLID ROCK
    Octillery:
        hp: 75 -> 80
        spe: 45 -> 40
        notable new moves: SNIPE SHOT, AQUA CUTTER
    Sudowoodo:
        hp: 70 -> 77
        atk: 115 -> 125
        spdef: 65 -> 73
    Xatu:
        hp: 65 -> 68
        atk: 75 -> 70
        spe: 95 -> 102
    Flaafy:
        atk: 55 -> 50
        spa: 80 -> 85
        spdef: 60 -> 70
        ability2: NONE -> MOLD BREAKER
    Ampharos: 
        ELECTRIC/ELECTRIC -> ELECTRIC/DRAGON
        atk: 75 -> 60
        spa: 115 -> 125
        spdef: 90 -> 105
        ability2: NONE -> MOLD BREAKER
    Leafeon:
        ability1: LEAF GUARD -> GUTS
    Glaceon:
        ability1: SNOW CLOAK -> SLUSH RUSH
    Forretress:
        hp: 75 -> 85
        ability2: NONE -> FULL METAL BODY
    Weavile:
        ability2: NONE -> TECHNICIAN