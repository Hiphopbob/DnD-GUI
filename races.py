# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:24:05 2019

@author: Steffen 000
"""
import numpy as np


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#print color.BOLD + 'Hello World !' + color.END   
def race_description(race_name):
    if race_name == 'Vampire':
        race_des = '''
Vampire Traits
Ability Score Increase: Your Intelligence score increases by 1, and your Charisma score increases by 2.
Speed. Your base walking speed is 30 feet.
Languages. You can speak, read, and write Common and Vampire.

Vampire Abilities
Darkvision. Thanks to your heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.
Vampiric Resistance. You have resistance to necrotic damage.
Blood Thirst. You can drain blood and life energy from a willing creature, or one that is grappled by you, incapacitated, or restrained. Make a melee attack against the target, using either Strength or Dexterity for your attack roll. If you hit, you deal 1 piercing damage and 1d6 necrotic damage. The target’s hit point maximum is reduced by an amount equal to the necrotic damage taken, and you regain hit points equal to that amount. The reduction lasts until the target finishes a long rest. The target dies if this effect reduces its hit point maximum to 0. A humanoid killed in this way becomes a null.
'''
#Age. Vampires don’t mature and age in the same way that other races do. Every living vampire is either a bloodchief, infected by the Eldrazi's influence in the distant reaches of history, or was spawned by a bloodchief from a living human. Most vampires are thus very old, but few have any memory of their earliest years.
#Alignment. Vampires have no innate tendency toward evil, but consuming the life energy of other creatures often pushes them to that end. Regardless of their moral bent, the strict hierarchies of their bloodchiefs inclines them toward a lawful alignment.
#Size. Vampires are about the same size and build as humans. Your size is Medium.
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list


    elif race_name == 'Aarakocra':
        race_des = '''
Aarakocra Traits
Ability Score Increase: Your Dexterity score increases by 2, and your Wisdom score increases by 1.
Speed: Your base walking speed is 25 feet.
Flight: You have a flying speed of 50 feet. To use this speed, you can’t be wearing medium or heavy armor.
Language: You can speak, read, and write Common, Aarakocra, and Auran

Aarakocra Abilities
Talons: You are proficient with your unarmed strikes, which deal 1d4 slashing damage on a hit.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Aasimar':
        race_des = '''
Aasimar Traits
Ability Score Increase: Your Charisma increases by 2.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Celestial.

Aasimar Abilities
Darkvision: Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

Celestial Resistance: You have resistance to necrotic damage and radiant damage

Healing Hands: As an action, you can touch a creature and cause it to regain a number of hit points equal to your level. Once you use this trait, you can't use it again until you finish a long rest.

Light Bearer: You know the light cantrip. Charisma is your spellcasting ability for it.
'''

        subrace_des = ['''
Aasimar Subraces
Protector Aasimar
Ability Score Increase: Your Wisdom score increases by 1.
Radiant Soul: Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back. Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level. Once you use this trait, you can't use it again until you finish a long rest.
''','''
Scourge Aasimar
Ability Score Increase: Your Constitution score increases by 1.
Radiant Consumption: Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you. Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level. Once you use this trait, you can't use it again until you finish a long rest.
''','''
Fallen Asimar
Ability Score Increase: Your Strength score increases by 1.
Necrotic Shroud: Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn. Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level. Once you use this trait, you can't use it again until you finish a long rest.
''']
        subrace_list = ['Protector Aasimar','Scourge Aasimar','Fallen Aasimar']
        return race_des,subrace_des,subrace_list



    elif race_name == 'Bug Bear':
        race_des= '''
Bug Bear Traits
Ability Score Increase: Your Strength score increases by 2 and your Dexterity score increases by 1.
Speed: Your base walking speed is 30 feet.
Sneaky: You are proficient in the Stealth skill.
Languages: You can speak, read, and write Common and Goblin.

Bug Bear Abilities
Darkvision: Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

Long Limbed: When you make a melee attack on your turn, your reach for it is 5 feet greater than normal.

Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.

Surprise Attack: If you surprise a creature and hit it with an attack on your first turn in combat, the attack deals an extra 2d6 damage to it. You can use this trait only once per combat.
'''
        subrace_des =   ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Changeling':
        race_des= '''
Changeling Traits
Ability Score Increase: Your Dexterity and Charisma scores increase by 1.
Speed: Your base walking speed is 30 feet.
Duplicity: You gain proficiency in the Deception skill.
Languages: You can speak, read, and write Common and two other languages of your choice.

Changeling Abilities
Shapechanger: As an action, you can polymorph into any humanoid of your size that you have seen, or back into your true form. However, your equipment does not change with you. If you die, you revert to your natural appearance.
'''
        subrace_des =   ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Dragonborn':
        race_des= '''
Dragonborn Traits
Ability Score Increase: Your Strength score increase by 2, and your Charisma score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can read, speak, and write Common and Draconic.
Draconic Ancestry: You are distantly related to a particular kind of dragon. Choose a type of dragon from the below list; this determines the damage and area of your breath weapon, and the type of resistance you gain.
Damage Resistance: You have resistance to the damage type associated with your ancestry.

Dragonborn Abilities
Breath Weapon: You can use your action to exhale destructive energy. It deals damage in an area according to your ancestry. When you use your breath weapon, all creatures in the area must make a saving throw, the type of which is determined by your ancestry. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.
'''

        subrace_des =   ['''
Black dragon
Damage Type: Acid
Breath weapon: 5' by 30' line (Dex save)
''','''
Blue dragon
Damage Type: Lightning
Breath weapon: 5' by 30' line (Dex save)
''','''
Brass dragon
Damage Type: Fire
Breath weapon: 5' by 30' line (Dex save)
''','''
Bronze dragon
Damage Type: Lightning
Breath weapon: 5' by 30' line (Dex save)
''','''
Copper dragon
Damage Type: Acid
Breath weapon: 5' by 30' line (Dex save)
''','''
Gold dragon
Damage Type: Fire
Breath weapon: 15' cone (Dex save)
''','''
Green dragon
Damage Type: Poison
Breath weapon: 15' cone (Con save)
''','''
Red dragon
Damage Type: Fire
Breath weapon: 15' cone (Dex save)
''','''
Silver dragon
Damage Type: Cold
Breath weapon: 15' cone (Con save)
''','''
White dragon
Damage Type: Cold
Breath weapon: 15' cone (Con save)
''']
        subrace_list = ['Black dragon','Blue dragon','Brass dragon','Bronze dragon','Copper dragon','Gold dragon','Green dragon','Red dragon','Silver dragon','White dragon']
        return race_des,subrace_des,subrace_list
        

    elif race_name == 'Dwarf':
        race_des= '''
Dwarf Traits
Ability Score Increase: Your Constitution score increases by 2.
Speed: Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.
Dwarven Combat Training: You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer.
Tool Proficiency: You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.
Languages: You can speak, read, and write Common and Dwarvish.

Dwarf Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim Conditions. You can see in dim light within 60 feet of you as if it were bright light, and in Darkness as if it were dim light. You can’t discern color in Darkness, only shades of gray.

Dwarven Resilience: You have advantage on Saving Throws against poison, and you have Resistance against poison damage.

Stonecunning: Whenever you make an Intelligence (History) check related to the Origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.
'''
        subrace_des=['''
Dwarf subraces
Hill Dwarf
Ability Score Increase: Your Wisdom score increases by 1.
Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.
''','''
Mountain Dwarf
Ability Score Increase: Your Strength score increases by 2.
Dwarven Armor Training: You have proficiency with light and medium armor.
''','''
Duergar (MToF)
Ability Score Increase: Your Strength score increases by 1.
Superior Darkvision: Your darkvision has a radius of 120 feet.
Extra Language: You can speak, read, and write Undercommon.
Duergar Resilience: You have advantage on saving throws against illusions and against being charmed or paralyzed.
Duergar Magic: When you reach 3rd level, you can cast the enlarge/reduce spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the invisibility spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.
Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight
''']
        subrace_list=['Hill Dwarf','Mountain Dwarf','Duergar (MToF)']
        return race_des,subrace_des,subrace_list


    elif race_name == 'Elf':
        race_des= '''
Elf Traits
Ability Score Increase: Your Dexterity score increases by 2.
Speed: Your base walking speed is 30 feet.
Keen Senses: You have proficiency in the Perception skill.
Languages: You can speak, read, and write Common and Elven.

Elf Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim Conditions. You can see in dim light within 60 feet of you as if it were bright light, and in Darkness as if it were dim light. You can’t discern color in Darkness, only shades of gray.

Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.

Trance: Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.
'''
        subrace_des=['''
Elf subraces
High Elf
Ability Score Increase: Your Intelligence score increases by 1.
Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.
Cantrip: You know one cantrip of your choice from the wizard list. Intelligence is your spellcasting ability for it.
Extra Language: You can read, speak, and write one additional language of your choice.
''','''
Wood Elf
Ability Score Increase: Your Wisdom score increases by 1.
Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.
Fleet of Foot: Your base walking speed increases to 35 feet.
Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.
''','''
Dark Elf / Drow
Ability Score Increase: Your Charisma score increases by 1.
Superior Darkvision: Your darkvision has a range of 120 feet, instead of 60.
Sunlight Sensitivity: You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight.
Drow Magic: You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.
Drow Weapon Training: You have proficiency with rapiers, shortswords, and hand crossbows.
''','''
Eladrin (MToF)
Ability Score Increase: Your Charisma score increases by 1.
Fey Step: As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest. When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 +your proficiency bonus+ your Charisma modifier:
Autumn: Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it.
Winter: When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.
Spring: When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.
Summer: Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage).
''','''
Eladrin (UA)
Ability Score Increase: Your Intelligence or Charisma score increases by 1 (your choice).
Fey Step: As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can’t do so again until you finish a short or long rest.
Shifting Seasons: At the end of each short or long rest, you can align yourself with the magic of one season, regardless of the season that is dominating your personality. Doing so allows you to cast a certain cantrip, as shown in the table below. When you align yourself with a season’s magic, you lose the cantrip associated with the previous season and gain the cantrip associated with the new season. Your spellcasting ability for these cantrips is Intelligence or Charisma, whichever is higher.
    
Autumn: Friends
Winter: Chill Touch
Spring: Minor Illusion
Summer: Firebolt
''','''
Sea Elf (MToF)
Ability Score Increase: Your Constitution score increases by 1.
Sea Elf Training: You have proficiency with the spear, trident, light crossbow, and net.
Child of the Sea: You have a swimming speed of 30 feet, and you can breathe air and water.
Friend of the Sea: Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed.
Languages: You can speak, read, and write Aquan.
''','''
Shadar-Kai (MToF)
Ability Score Increase: Your Constitution score increases by 1.
Necrotic Resistance: You have resistance to necrotic damage.
Blessing of the Raven Queen: As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest. Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.
''']
        subrace_list=['High Elf','Wood Elf','Dark Elf / Drow','Eladrin (MToF)','Eladrin (UA)','Sea Elf','Shadar-Kai (MToF)']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Firbolg':
        race_des= '''
Firbolg Traits
Ability Score Increase: Your Wisdom score increases by 2, and your Strength score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common, Elvish, and Giant.

Firbolg Abilities
Firbolg Magic: You can cast detect magic and disguise self with this trait, using Wisdom as your spellcasting ability for them. Once you cast either spell, you can't cast it again with this trait until you finish a short or long rest. When you use this version of disguise self, you can seem up to 3 feet shorter than normal, allowing you to more easily blend in with humans and elves.

Hidden Step: As a bonus action, you can magically turn invisible until the start of your next turn or until you attack, make a damage roll, or force someone to make a saving throw. Once you use this trait, you can't use it again until you finish a short or long rest.

Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.

Speech of Beast and Leaf: You have the ability to communicate in a limited manner with beasts and plants. They can understand the meaning of your words, though you have no special ability to understand them in return. You have advantage on all Charisma checks you make to influence them.
'''
        subrace_des =['None']
        subrace_list=['None']
        return race_des,subrace_des,subrace_list
    
    elif race_name == 'Genasi':
        race_des= '''
Genasi Traits
Ability Score Increase. Your Constitution score increases by 2.
Speed. Your base walking speed is 30 feet.
Languages. You can speak, read, and write Common and Primordial. Primordial is a guttural language, filled with harsh syllables and hard consonants.
'''
        subrace_des=['''
Genasi Subraces
Air Genasi
Ability Score Increase: Your Dexterity score increases by 1.
Unending Breath: You can hold your breath indefinitely while you’re not incapacitated.
Mingle with the Wind: You can cast the Levitate spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.
''','''
Earth Genasi
Ability Score Increase: Your Strength score increases by 1.
Earth Walk: You can move across difficult terrain made of earth or stone without expending extra movement.
Merge with Stone: You can cast the Pass Without Trace spell once with this trait, requiring no material components, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for this spell.
''','''
Fire Genasi
Ability Score Increase: Your Intelligence score increases by 1.
Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. Your ties to the Elemental Plane of Fire make your darkvision unusual: everything you see in darkness is in a shade of red.
Fire Resistance: You have resistance to fire damage.
Reach to the Blaze: You know the produce Flame cantrip. Once you reach 3rd level, you can cast the Burning Hands spell once with this trait as a 1st-level spell, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for these spells.
''','''
Water Genasi
Ability Score Increase: Your Wisdom score increases by 1.
Acid Resistance: You have resistance to acid damage. Amphibious. You can breathe air and water.
Swim: You have a swimming speed of 30 feet.
Call to the Wave: You know the Shape Water cantrip. When you reach 3rd level, you can cast the Create or Destroy Water spell as a 2nd-level spell once with this trait, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for these spells.
''']
        subrace_list=['Air Genasi','Earth Genasi','Fire Genasi','Water Genasi']
        return race_des,subrace_des,subrace_list
    
    elif race_name == 'Gith':
        race_des = '''
Gith Traits
Ability Score Increase: Your Intelligence score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Gith.
'''
        subrace_des = ['''
Gith Subraces
Githyanki
Ability Score Increase: Your Strength score increases by 2.
Decadent Mastery: You learn one language of your choice, and you are proficient with one skill or tool of your choice. In the timeless city of Tu'narath, githyanki have bountiful time to master odd bits of knowledge.
Martial Prodigy: You are proficient with light and medium armor and with shortswords, longswords, and greatswords.
Githyanki Psionics: You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait. When you reach 3rd level, you can cast the Jump spell once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Misty Step spell once with this trait, and you regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for these spells. When you cast them with this trait, they don't require components.
''','''
Githzerai
Ability Score Increase: Your Wisdom score increases by 2.
Mental Discipline: You have advantage on saving throws against the charmed and frightened conditions. Under the tutelage of monastic masters, githzerai learn to govern their own minds.
Githzerai Psionics: You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait. When you reach 3rd level, you can cast the Shield spell once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Detect Thoughts spell once with this trait, and you regain the ability to do so when you finish a long rest. Wisdom is your spellcasting ability for these spells. When you cast them with this trait, they don't require components.
''']
        subrace_list = ['Githyanki','Githzerai']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Goliath':
        race_des= '''
Goliath Traits
Ability Score Increase: Your Strength score increases by 2, and your Constitution score increases by 1.
Speed: Your base walking speed is 30 feet.
Natural Athlete: You have proficiency in the Athletics skill.
Languages: You can speak, read, and write Common and Giant.

Goliath Abilities
Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.

Mountain Born: You’re acclimated to high altitude, including elevations above 20,000 feet. You’re also naturally adapted to cold climates, as described in chapter 5 of the Dungeon Master’s Guide.

Stone’s Endurance: You can focus yourself to occasionally shrug off injury. When you take damage, you can use your reaction to roll a d12. Add your Constitution modifier to the number rolled, and reduce the damage by that total. After you use this trait, you can’t use it again until you finish a short or long rest.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Gnome':
        race_des = '''
Gnome Traits
Ability Score Increase: Your Intelligence score increases by 2.
Speed: Your base walking speed is 25 feet.
Languages: You can read, speak, and write Common and Gnomish

Gnome Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Gnome Cunning: You have advantage on all Intelligence, Wisdom, and Charisma saves against magic.
'''
        subrace_des = ['''
Gnome Subraces
Forest Gnome
Ability Score Increase: Your Dexterity score increases by 1.
Natural Illusionist: You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it.
Speak with Small Beasts: Through sound and gestures, you may communicate simple ideas with Small or smaller beasts.
''','''
Rock Gnome
Ability Score Increase: Your Constitution score increases by 1.
Artificer's Lore: Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply.
Tinker: You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:
Clockwork Toy: This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.
Fire Starter: The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.
Music Box: When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.
At your DM's discretion, you may make other objects with effects similar in power to these. The Prestidigitation cantrip is a good baseline for such effects.
''','''
Deep Gnome / Svirfneblin (EE)
Ability Score Increase: Your Dexterity score increases by 1.
Superior Darkvision: Your darkvision has a radius of 120 feet.
Stone Camouflage: You have advantage on Dexterity (stealth) checks to hide in rocky terrain.
Languages: You can speak, read, and write Undercommon.
''']
        subrace_list = ['Forest Gnome','Rock Gnome','Deep Gnome / Svirfneblin (EE)']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Goblin':
        race_des = '''
Goblin Traits
Ability Score Increase: Your Dexterity score increases by 2, and your Constitution score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Goblin.

Goblin Abilities
Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Fury of the Small: When you damage a creature with an attack or a spell and the creature's size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your level. Once you use this trait, you can't use it again until you finish a short or long rest.

Nimble Escape: You can take the Disengage or Hide action as a bonus action on each of your turns.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list
        
    elif race_name == 'Grung':
        race_des = '''
Grung Traits
Ability Score Increase: Your Dexterity score increasesby 2 and your Constitution score increases by 1.
Speed: Your base walking speed is 25 feet, and you have a climbing speed of 25 feet.
Languages: You can speak, read, and write Grung
Arboreal Alertness: You have proficiency in the Perception skill.

Grung Abilities
Amphibious: You can breathe air and water.

Poisonous Skin: Any creature that grapples you or otherwise comes into direct contact with your skin must succeed on a DC 12 Constitution saving throw or become poisoned for 1 minute. A poisoned creature no longer in direct contact with you can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. You can also apply this poison to any piercing weapon as part of an attack with that weapon, though when you hit the poison reacts differently. The target must succeed on a DC 12 Constitution saving throw or take 2d4 poison damage.

Standing Leap: Your long jump is up to 25 feet and your high jump is up to 15 feet, with or without a running start.

Water Dependency: If you fail to immerse yourself in water for at least 1 hour during a day, you suffer one level of exhaustion at the end of that day. You can only recover from this exhaustion through magic or by immersing yourself in water for at least 1 hour.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list        

    elif race_name == 'Half Dwarf':
        race_des= '''
Half Dwarf Traits
Ability Score Increase: Your Constitution score increases by 2, and two other ability scores of your choice each increase by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can read, speak, and write Common, Dwarven, and one language of your choice.

Half Dwarf Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Dwarven Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.

Half-Dwarf Versatility: Choose one of the following traits:
Skill Versatility (General Heritage): You gain proficiency in two skills of your choice.
Dwarven Combat Training (General Heritage): You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.
Tool Proficiency (General Heritage): You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.
Dwarven Toughness (Hill Dwarf Heritage): Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.
Duergar Resilience (Duergar Heritage): You have advantage on saving throws against illusions and against being charmed or paralyzed.
Duergar Magic (Duergar Heritage): When you reach 3rd level, you can cast the Enlarge/Reduce spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the Invisibility spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.
Dwarven Armor Training (Mountain Dwarf Heritage): You have proficiency with light and medium armor.
Powerful Build (General): You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Half Elf':
        race_des= '''
Half Elf Traits
Ability Score Increases: Your Charisma score increase by 2, and two other ability scores of your choice each increase by 1.
Speed: Your base walking speed is 30 feet.
Skill Versatility: You gain proficiency in two skills of your choice.
Languages: You can read, speak, and write Common, Elven, and one language of your choice.

Half Elf Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim Conditions. You can see in dim light within 60 feet of you as if it were bright light, and in Darkness as if it were dim light. You can’t discern color in Darkness, only shades of gray.

Fey Ancestry: You have advantage on saving throws against being charmed, and magic can't put you to sleep.

Half Elf Variant
Some half-elves take after their elven parent more than their human parent. Such half-elves may take one of the following traits in place of the Skill Versatility trait.
Elf Weapon Training (High Elf or Wood Elf): You have proficiency with the longsword, shortsword, shortbow, and longbow.
Cantrip (High Elf): You know one cantrip of your choice from the wizard list. Intelligence is your spellcasting ability for it.
Fleet of Foot (Wood Elf): Your base walking speed increases to 35 feet.
Mask of the Wild (Wood Elf): You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.
Drow Magic (Dark Elf): You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.
Swim Speed (Sea Elf): You have a swimming speed of 30 feet.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Half Orc':
        race_des = '''
Half Orc Traits
Ability Score lncreases: Your Strength score increases by 2, and your Constitution score increases by 1.
Speed: Your base walking speed is 30 feet.
Menacing: You gain proficiency in the Intimidation skill.
Languages: You can speak. read, and write Common and Orcish.

Half Orc Abilities
Relentless Endurance: When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.

Savage Attacks: When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Halfling':
        race_des= '''
Halfling Traits
Ability Score Increase: Your Dexterity score increases by 2.
Speed: Your walking speed is 25 feet.
Languages: You can speak, read, and write Common and Halfling.

Halfling Abilities
Lucky: When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.

Brave: You have advantage on saving throws against being frightened.

Nimble: You can move through the space of any creature that is of a size larger than yours.
'''
        subrace_des=['''
Halfling Subraces
Lightfoot
Ability Score Increase: Your Charisma score increases by 1.
Naturally Stealthy: You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you.
''','''
Stout
Ability Score Increase: Your Constitution score increases by 1.
Stout Resilience: You have advantage on saving throws against poison, and you have resistance to poison damage.
''']
        subrace_list=['Lightfoot','Stout']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Hobgoblin':
        race_des= '''
Hobgoblin Traits
Ability Score Increase: Your Constitution score increases by 2, and your Intelligence score increases by 1.
Speed: Your base walking speed is 30 feet.
Martial Trainin': You are proficient with two martial weapons of your choice and with light armor.
Languages: You can speak, read, and write Common and Goblin.

Hobgoblin Abilities
Darkvision: Accustomed to life underground, you have superior vision in dark and dim Conditions. You can see in dim light within 60 feet of you as if it were bright light, and in Darkness as if it were dim light. You can’t discern color in Darkness, only shades of gray.

Savin' Face: Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list
    
    elif race_name == 'Human':
        race_des= '''
Choose either Human or Variant Human.

Human Traits
Ability Score Increase: Your ability scores each increase by 1.
Speed: Your base walking speed is 30 fee!.
Languages: You can speak, read, and write Common and one extra language of your choice.

Variant Human Traits
Ability Score Increase: Two different ability scores of your choice increase by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and one extra language of your choice.
Skills: You gain proficiency in one skill of your choice.
Feat: You gain one feat of your choice.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Kalashtar':
        race_des= '''
Kalashtar Traits
Ability Score Increase: Your Wisdom and Charisma scores both increase by 1. In addition, one ability score of your choice increases by 1.
Speed: Your base walking speed is 30 feet.
Psychic Glamour: Choose one of the following skills: Insight, Intimidation, Performance, or Persuasion. You have advantage on all ability checks you make with that skill.
Languages: You can read and write Common, Quori, and one other language of your choice.

Kalashtar Abilities
Dual Mind: When you make a Wisdom saving throw, you can use your reaction to gain advantage on the roll. You can use this trait immediately before or after you roll, but before any of the roll's effects occur.

Mental Discipline: You have resistance to psychic damage.

Mind Link: You can speak telepathically to any creature you can see within 60 feet of you. You don’t need to share a language with the creature for it to understand your telepathic messages, but the creature must be able to understand at least one language or be telepathic itself.
    As a bonus action when you’re speaking telepathically to a creature, you can give that creature the ability to speak telepathically to you until the start of your next turn. To use this ability, the creature must be within 60 feet of you and be able to see you.

Severed from Dreams: Kalashtar sleep, but they don’t connect to the plane of dreams as other creatures do. Instead, their minds draw from the memories of their otherworldly spirit while they sleep. As such, you are immune to magical spells and effects that require you to dream, like the Dream spell, but not to spells and effects that put you to sleep, like the Sleep spell.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Kenku':
        race_des='''
Kenku Traits
Ability Score Increase: Your Dexterity score increases by 2, and your Wisdom score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can read and write Common and Auran, but you can speak only by using your Mimicry trait.
Kenku Training: You are proficient in your choice of two of the following skills: Acrobatics, Deception, Stealth, and Sleight of Hand.

Kenku Abilities
Expert Forgery: You can duplicate other creatures' handwriting and craftwork. You have advantage on all checks made to produce forgeries or duplicates of existing objects.

Mimicry: You can mimic sounds you have heard, including voices. A creature that hears the sounds you make can tell they are imitations with a successful Wisdom (Insight) check opposed by your Charisma (Deception) check.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Kobold':
        race_des= '''
Kobold Traits
Ability Score Increase: Your Dexterity score increases by 2, and your Strength score is reduced by 2.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Draconic.

Kobold Abilities
Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Grovel, Cower, and Beg: As an action on your turn, you can cower pathetically to distract nearby foes. Until the end of your next turn, your allies gain advantage on attack rolls against enemies within 10 feet of you that can see you. Once you use this trait, you can't use it again until you finish a short or long rest.

Pack Tactics: You have advantage on an attack roll against a creature if at least one of your allies is within 5 feet of the creature and the ally isn't incapacitated.

Sunlight Sensitivity: You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Lizardfolk':
        race_des= '''
Lizardfolk Traits
Ability Score Increase: Your Constitution score increases by 2, and your Wisdom score increases by 1.
Speed: Your base walking speed is 30 feet, and you have a swimming speed of 30 feet.
Hunter's Lore: You gain proficiency with two of the following skills of your choice: Animal Handling, Nature, Perception, Stealth, and Survival.
Languages: You can speak, read, and write Common and Draconic.

Lizardfolk Abilities
Bite: Your fanged maw is a natural weapon, which you can use to make unarmed strikes. If you hit with it, you deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

Cunning Artisan: As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size Small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan's tools, such as leatherworker's tools.

Hold Breath: You can hold your breath for up to 15 minutes at a time.

Natural Armor: You have tough, scaly skin. When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.

Hungry Jaws: In battle, you can throw yourself into a vicious feeding frenzy. As a bonus action, you can make a special attack with your bite. If the attack hits, it deals its normal damage, and you gain temporary hit points (minimum of 1) equal to your Constitution modifier, and you can't use this trait again until you finish a short or long rest.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Minotaur':
        race_des= '''
Minotaur Traits
Ability Score Increase: Your Strength score increases by 1.
Conqueror's Virtue: From a young age, you focused on one of the three virtues of strength, cunning, or intellect. Your choice of your Strength, Intelligence, or Wisdom score increases by 1.
Speed: Your base walking speed is 30 feet.
Sea Reaver: You gain proficiency with navigator’s tools and vehicles (water).
Languages: You can speak, read, and write Common.

Minotaur Abilities
Horns: You are never unarmed. You are proficient with your horns, which are a melee weapon that deals 1d10 piercing damage. Your horns grant you advantage on all checks made to shove a creature, but not to avoid being shoved yourself.

Goring Rush: When you use the Dash action during your turn, you can make a melee attack with your horns as a bonus action.

Hammering Horns: When you use the Attack action during your turn to make a melee attack, you can attempt to shove a creature with your horns as a bonus action. You cannot use this shove attempt to knock a creature prone.

Labyrinth Recall: You can perfectly recall any path you have traveled.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Orc':
        race_des= '''
Orc Traits
Ability Score Increase: Your Strength score increases by 2, your Constitution score increases by 1, and your Intelligence score is reduced by 2.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Orc.
Menacing: You are trained in the Intimidation skill.

Orc Abilities
Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Aggressive: As a bonus action, you can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.

Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Shifter':
        race_des= '''
Shifter Traits
Ability Score Increase: Your Wisdom score increases by 1.
Speed: Your base speed is 30 feet
Languages: You can speak, read, and write Common and one other language of your choice.

Shifter Abilities
Darkvision: Thanks to your lycanthrope heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

Keen Smell: You have advantage on Wisdom (Perception) checks that rely on smell.

Shifting Nature: Shifting allows you to tap into your wilder side, and gain temporal bonuses depending on your heritage. As a reaction after receiving damage, you may shift, entering your more bestial state for one minute. You can end the shift at any moment as a bonus action. While you are in this state, you cannot cast spells that require concentration. You can’t shift again until you finish a long rest. At 5th level, you have achieved more control of your shifting. You can shift a second time before taking a long rest, and can shift at will as a bonus action.
'''
        subrace_des=['''
Shifter Subraces
Longtooth
Ability Score Increase: Your Strength score increases by 1.
Wild Fortitude: You gain proficiency in the Athletics skill.
Longtooth Shifting: While shifting, you regenerate hit points at the start of your turns equal to your Proficiency Bonus. 
In addition, you grow long fangs which allow you to use your bite as a light melee weapon which deals 1d6 piercing damage. 
You also add 1d4 to the damage of the first Strength-based attack that you perform after shifting. 
At 5th level, if your bite attacks hit a creature that is your size or smaller, that creature is grappled.
''','''
Razorclaw
Ability Score Increase: Your Dexterity score increases by 1.
Feral: You gain proficiency in the Stealth skill.
Razorclaw Shifting: When you shift, your speed increases to 35 feet.
You also have advantage on Dexterity saving throws while on this state, as long as you are not wearing heavy armor.
In addition, you grow a pair of claws which can function as light, finesse, melee weapons which deal 1d6 slashing damage.
At 5th level, you can now make an attack with your claws as a bonus action while in your shift state.
''']
        subrace_list = ['Longtooth','Razorclaw']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Tabaxi':
        race_des= '''
Tabaxi Traits
Ability Score Increase: Your Dexterity increases by 2, and your charisma increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and one other language of your choice.
Cat's Talent: You have proficiency in the Perception and Stealth skills.

Tabaxi Abilities
Darkvision: You have a cat’s keen senses especially in the dark. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness only shades of gray.

Feline Agility: your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can't use it again until you move 0 feet on one of your turns.

Cat's Claws: Because of your claws, you have a climbing speed of 20 feet. In addition, your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Tiefling':
        race_des= '''
Tiefling Traits
Ability Score Increase: Your Charisma score increases by 2.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common and Infernal.

Tiefling Abilities
Darkvision: Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

Hellish Resistance: You have resistance to fire damage.
'''
        subrace_des=['''
Tiefling Subraces
Bloodline of Asmodeus
Ability Score Increase: Your Intelligence score increases by 1.
Infernal Legacy: You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Baalzebul
Ability Score Increase: Your Intelligence score increases by 1.
Legacy of Maladomini: You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Ray of Sickness spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Crown of Madness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Devil's Tongue Bloodline
Ability Score Increase: Your Intelligence score increases by 1.
Devil's Tongue: You know the Vicious Mockery cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Enthrall spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Dispater
Ability Score Increase: Your Dexterity score increases by 1.
Legacy of Dis: You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Detect Thoughts spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Fierna
Ability Score Increase: Your Wisdom score increases by 1.
Legacy of Phlegethos: You know the Friends cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Suggestion spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Glasya
Ability Score Increase: Your Dexterity score increases by 1.
Legacy of Malbolge: You know the Minor Illusion cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Invisibility spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Levistus
Ability Score Increase: Your Constitution score increases by 1.
Legacy of Stygia: You know the Ray of Frost cantrip. Once you reach 3rd level, you can cast the Armor of Agathys spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Mammon
Ability Score Increase: Your Intelligence score increases by 1.
Legacy of Minauros: You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Tenser's Floating Disk spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Arcane Lock spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Bloodline of Mephistopheles
Ability Score Increase: Your Intelligence score increases by 1.
Legacy of Cania: You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''','''
Winged Bloodline
Ability Score Increase: Your Intelligence score increases by 1.
Winged: You have bat-like wings sprouting from your shoulders. You have a flying speed of 30 feet while you aren’t wearing heavy armor.
''','''
Bloodline of Zariel
Ability Score Increase: Your Strength score increases by 1.
Legacy of Avernus: You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Searing Smite spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.
''']
        subrace_list=['Bloodline of Baalzebul',"Devil's Tongue Bloodline",'Bloodline of Dispater','Bloodline of Fierna','Bloodline og Glasya','Bloodline og Levistus','Bloodline of Mammon','Bloodline of Mephistopheles','Winged Bloodline','Bloodline of Zariel']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Tortle':
        race_des= '''
Tortle Traits
Ability Score Increase: Your Strength score increases by 2, and your Wisdom score increases by 1.
Speed: Your base walking speed is 30 feet.
Natural Armor: Due to your shell and the shape of your body, you are ill-suited to wearing armor. Your shell provides ample protection, however; it gives you a base AC of 17 (your Dexterity modifier doesn't affect this number). You gain no benefit from wearing armor, but if you are using a shield, you can apply the shield's bonus as normal.
Survival Instinct: You gain proficiency in the Survival skill. Tortles have finely honed survival instincts.
Languages: You can speak, read, and write Common and Aquan.

Tortle Abilities
Claws: Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

Hold Breath: You can hold your breath for up to 1 hour at a time. Tortles aren't natural swimmers, but they can remain underwater for some time before needing to come up for air.

Shell Defense: You can withdraw into your shell as an action. Until you emerge, you gain a +4 bonus to AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can't increase, you have disadvantage on Dexterity saving throws, you can't take reactions, and the only action you can take is a bonus action to emerge from your shell.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Triton':
        race_des= '''
Triton Traits
Ability Score Increase: Your Strength, Constitution, and Charisma scores each increase by 1.
Speed: Your base walking speed is 30 feet, and you have a swimming speed of 30 feet.
Languages: You can speak, read, and write Common and Primordial.

Triton Abilities
Control Air and Water: A child of the sea, you can call on the magic of elemental air and water. You can cast fog cloud* with this trait. Starting at 3rd level, you can cast gust of wind* with it, and starting at 5th level, you can also cast wall of water* with it (see the spell at the bottom). Once you cast a spell with this trait, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.

Emissary of the Sea: Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.

Guardian of the Depths: Adapted to even the most extreme ocean depths, you have resistance to cold damage, and you ignore any of the drawbacks caused by a deep, underwater environment.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Warforged':
        race_des= '''
Warforged Traits
Ability Score Increase: Your Constitution score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common.

Warforged Abilities
Warforged Resilience: You were created to have remarkable fortitude, represented by the following benefits.
You have advantage on saving throws against being poisoned, and you have resistance to poison damage.
You are immune to disease.
You don’t need to eat, drink, or breathe.
You don't need to sleep and don't suffer the effects of exhaustion due to lack of rest, and magic can’t put you to sleep.

Sentry's Rest: When you take a long rest, you must spend at least six hours in an inactive, motionless state, rather than sleeping. In this state, you appear inert, but it doesn’t render you unconscious, and you can see and hear as normal.

Integrated Protection: Your body has built-in defensive layers, which determine your armor class. You gain no benefit from wearing armor, but if you are using a shield, you apply its bonus as normal. 
    You can alter your body to enter different defensive modes; each time you finish a long rest, choose one mode to adopt from the Integrated Protection table below, provided you meet the mode’s prerequisite.

Mode
Prerequisite
Effect
Darkwood Core (unarmored)
None
AC = 11 + your Dexterity modifier (add proficiency bonus if proficient with light armor).
Composite Plating (armored)
Medium armor proficiency
AC = 13 + your Dexterity modifier (maximum of 2) + your proficiency bonus.
Heavy Plating (armored)
Heavy armor proficiency
AC = 16 + your proficiency bonus; disadvantage on Dexterity (Stealth) checks.
'''
        subrace_des=['''
Warforged Subraces
Envoy
Ability Score Increase: Two different ability scores of your choice increase by 1.
Specialized Design: You gain one skill proficiency of your choice, one tool proficiency of your choice, and fluency in one language of your choice.
Integrated Tool: Choose one tool you’re proficient with. This tool is integrated into your body, and you double your proficiency bonus for any ability checks you make with it. You must have your hands free to use this integrated tool.
''','''
Juggernaut
Ability Score Increase: Your Strength score increases by 2.
Iron Fists: When you make an unarmed strike, you can deal 1d4 + your Strength modifier bludgeoning damage instead of the normal damage.
Powerful Build: You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.
''','''
Skirmisher
Ability Score Increase: Your Dexterity score increases by 2.
Swift: Your walking speed is increased by 5 feet.
Light Step: When you are traveling alone for an extended period of time (one hour or more), you can move stealthily at a normal pace.
''']
        subrace_list=['Envoy','Juggernaut','Skirmisher']
        return race_des,subrace_des,subrace_list

    elif race_name == 'Yuan-Ti Pureblood':
        race_des= '''
Yuan-Ti Traits
Ability Score Increase: Your Charisma score increases by 2, and your Intelligence score increases by 1.
Speed: Your base walking speed is 30 feet.
Languages: You can speak, read, and write Common, Abyssal, and Draconic

Yuan-Ti Abilities
Darkvision: You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

Innate Spellcasting: You know the poison spray cantrip. You can cast animal friendship an unlimited number of times with this trait, but you can target only snakes with it. Starting at 3rd level, you can also cast suggestion with this trait. Once you cast it, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.

Magic Resistance: You have advantage on saving throws against spells and other magical effects.

Poison Immunity: You are immune to poison damage and the poisoned condition.
'''
        subrace_des = ['None']
        subrace_list = ['None']
        return race_des,subrace_des,subrace_list



    else:
        return '''
        This race has not been added yet
        '''









      
        
race_list = ['Aarakocra','Aasimar','Bug Bear','Changeling','Dragonborn','Dwarf','Elf','Firbolg','Genasi','Gith','Goliath','Gnome','Goblin','Grung','Half Dwarf','Half Elf','Half Orc','Halfling','Hobgoblin','Human','Kalashtar','Kenku','Kobold','Lizardfolk','Minotaur','Orc','Shifter','Tabaxi','Tiefling','Tortle','Triton','Warforged','Yuan-Ti Pureblood']
race_N=len(race_list)

race_dict = {}
for i in xrange(len(race_list)):
    race_dict[race_list[i]]=str(i)
#print(race_dict)

def subrace_dict(race_name):
    subrace_dict = {}
    race_des, subrace_des,subrace_list = race_description(race_name)
    N = len(subrace_list)
    if N>0:
        for i in xrange(N):
            subrace_dict[subrace_list[i]]=str(i)
    return subrace_dict
#print subrace_dict('Aasimar')
#print subrace_dict('Aarakocra')



def test_races():
    for i in xrange(len(race_list)):
        print race_description(race_list[i])
    return

#test_races()
