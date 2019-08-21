# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:24:05 2019

@author: Steffen 000
"""
import numpy as np

def class_description(class_name):
    if class_name == 'Artificer':
        return '''
Artificer Traits
Hit Points
Hit Dice: 1d8 per artificer level
Hit Points at 1st Level: 8 + your Constitution modifier
Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per artificer level after 1st

Proficiencies
Armor: Light armor, medium armor, shields
Weapons: Simple weapons, hand crossbows, heavy crossbows
Tools: Thieves’ tools, tinker’s tools, one type of artisan’s tools of your choice
Saving Throws: Constitution, Intelligence
Skills: Choose two from Arcana, History, Investigation, Medicine, Nature, Perception, Sleight of Hand

Equipment
You start with the following equipment, in addition to the equipment granted by your background:
any two simple weapons
a light crossbow and 20 bolts
(a) studded leather armor or (b) scale mail
thieves’ tools and a dungeoneer’s pack

Artificer Features
Magical Tinkering: At 1st level, you learn how to invest a spark of magic in objects that would otherwise be mundane. To use this ability, you must have thieves’ tools, tinker’s tools, or other artisan’s tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice:
The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.
Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.
The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.
A static visual effect appears on one of the object’s surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.
    The chosen property lasts indefinitely. As an action, you can touch the object and end the property early.
    You can give the magic of this feature to multiple objects, touching one object each time you use the feature, and a single object can bear only one of the properties at a time. The maximum number of objects you can affect with the feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.

Spellcasting: You have studied the workings of magic, how to channel it through objects, and how to awaken it within them. As a result, you have gained a limited ability to cast spells. To observers, you don’t appear to be casting spells in a conventional way; you look as if you’re producing wonders through various items.
Tools Required: You produce your artificer spell effects through your tools. You must have a spellcasting focus – specifically thieves’ tools or some kind of artisan’s tool – in hand when you cast any spell with this Spellcasting feature. You must be proficient with the tool to use it in this way. 
    After you gain the Infuse Item feature at 2nd level, you can also use any item bearing one of your infusions as a spellcasting focus.
Cantrips: At 1st level, you know two cantrips of your choice from the artificer spell list. At higher levels, you learn additional artificer cantrips of your choice, as shown in the Cantrips Known column of the Artificer table.
    When you gain a level in this class, you can replace one of the artificer cantrips you know with another cantrip from the artificer spell list.
Spell Slots: The Artificer table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell’s level or higher. You regain all expended spell slots when you finish a long rest.
Preparing and Casting Spells: The Artificer table shows how many spell slots you have to cast your artificer spells. To cast one of your artificer spells of 1st level or higher, you must expend a slot of the spell’s level or higher. You regain all expended spell slots when you finish a long rest.
    You prepare the list of artificer spells that are available for you to cast, choosing from the artificer spell list. When you do so, choose a number of artificer spells equal to your Intelligence modifier + half your artificer level, rounded down (minimum of one spell). The spells must be of a level for which you have spell slots.
    For example, if you are a 5th-level artificer, you have four 1st-level and two 2nd-level spell slots. With an Intelligence of 14, your list of prepared spells can include four spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn’t remove it from your list of prepared spells.
    You can change your list of prepared spells when you finish a long rest. Preparing a new list of artificer spells requires time spent in tinkering with your spellcasting focuses: at least 1 minute per spell level for each spell on your list.
Spellcasting Ability: Intelligence is your spellcasting ability for your artificer spells; your understanding of the theory behind magic allows you to wield these spells with superior skill. You use your Intelligence whenever an artificer spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for an artificer spell you cast and when making an attack roll with one.
Spell save DC = 8 + your proficiency bonus + your Intelligence modifier
Spell attack modifier = your proficiency bonus + your Intelligence modifier
Ritual Casting: You can cast an artificer spell as a ritual if that spell has the ritual tag and you have the spell prepared.

Infuse Item: At 2nd level, you gain the ability to imbue mundane items with certain magical infusions. The magic items you create with this feature are effectively prototypes of permanent items.
Infusions Known: When you gain this feature, pick two artificer infusions to learn. You learn additional infusions of your choice when you reach certain levels in this class, as shown in the Infusions Known column of the Artificer table.
    Whenever you gain a level in this class, you can replace one of the artificer infusions you learned with a new one.
Infusing an Item: Whenever you finish a long rest, you can touch a nonmagical object and imbue it with one of your artificer infusions, turning it into a magic item. An infusion works on only certain kinds of objects, as specified in the infusion’s description. If the item requires attunement, you can attune yourself to it the instant you infuse the item, or you can forgo attunement so that someone else can attune to the item. If you decide to attune to the item later, you must do so using the normal process for attunement.
    Your infusion remains in an item indefinitely, but when you die, the infusion vanishes after a number of days have passed equal to your Intelligence modifier (minimum of 1 day). The infusion also vanishes if you give up your knowledge of the infusion for another one.
    You can infuse more than one nonmagical object at the end of a long rest; the maximum number of objects appears in the Infused Items column of the Artificer table. You must touch each of the objects, and each of your infusions can be in only one object at a time. If you try to exceed your maximum number of infusions, the oldest infusion immediately ends, and then the new infusion applies.

Tool Expertise: Starting at 3rd level, your proficiency bonus is doubled for any ability check you make that uses your proficiency with a tool.

Arcane Armament: Starting at 5th level, you can attack twice, rather than once, whenever you take the Attack action on your turn, but one of the attacks must be made with a magic weapon, the magic of which you use to propel the attack.

The Right Cantrip for the Job: At 10th level, you gain the ability to make sure you have the right magical tool for a job. Whenever you finish a short or long rest, you can replace one of the artificer cantrips you know with another cantrip from the artificer spell list.

Spell-Storing Item: When you reach 18th level, you learn how to store a spell in an object for repeated use. Whenever you finish a long rest, you can touch one simple or martial weapon or an item that you can use as a spellcasting focus and store a spell in it, choosing one 1st- or 2nd-level spell from the artificer spell list that requires 1 action to cast (you don’t need to have the spell prepared). With the object in hand, a creature can take an action to produce the spell’s effect from it, using your spellcasting ability modifier.
    The spell stays in the object until it has been used a number of times equal to twice your Intelligence modifier (minimum of twice) or until you use this feature again.

Soul of Artifice: At 20th level, your understanding of magic items is unmatched, allowing you to mingle your soul with items linked to you. You can attune to up to six magic items at once. In addition, you gain a +1 bonus to all saving throws per magic item you are currently attuned to.


'''

    elif class_name == 'Barbarian':
        return '''
Barbarian Traits
Hit Points
Hit Dice: 1d12 per barbarian level
Hit Points at 1st Level: 12 + your Constitution modifier
Hit Points at Higher Levels: 1d12 (or 7) + your Constitution modifier per barbarian level after 1st

Proficiencies
Armor: Light armor, medium armor, shields
Weapons: Simple weapons, martial weapons
Tools: None
Saving Throws: Strength, Constitution
Skills: Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival

Equipment
You start with the following equipment, in addition to the equipment granted by your background:
(a) a greataxe or (b) any martial melee weapon
(a) two handaxes or (b) any simple weapon
An explorer's pack and four javelins

Barbarian Features
Rage: In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.
    While raging, you gain the following benefits if you aren't wearing heavy armor:
You have advantage on Strength checks and Strength saving throws.
When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
You have resistance to bludgeoning, piercing, and slashing damage.
    If you are able to cast spells, you can't cast them or concentrate on them while raging.
    Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.
    Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.

Unarmored Defense: While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.

Danger Sense: At 2nd level, you gain an uncanny sense of when things nearby aren't as they should be, giving you an edge when you dodge away from danger. You have advantage on Dexterity saving throws against effects that you can see, such as traps and spells. To gain this benefit, you can't be blinded, deafened, or incapacitated.

Reckless Attack: Starting at 2nd level, you can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.

Extra Attack: Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.

Fast Movement: Starting at 5th level, your speed increases by 10 feet while you aren't wearing heavy armor.

Feral Instinct: By 7th level, your instincts are so honed that you have advantage on initiative rolls.
    Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.

Brutal Critical: Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.
    This increases to two additional dice at 13th level and three additional dice at 17th level.

Relentless Rage: Starting at 11th level, your raage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.
    Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.

Persistent Rage: Beginning at 15th level, your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.

Indomitable Might: Beginning at 18th level, if your total for a Strength check is less than your Strength score, you can use that score in place of the total.

Primal Champion: At 20th level, you embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.

'''

    elif class_name == 'Bard':
        return '''
Bard Traits
Hit Points
Hit Dice: 1d8 per bard level
Hit Points at 1st Level: 8 + your Constitution modifier
Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per bard level after 1st

Proficiencies
Armor: Light armor
Weapons: Simple weapons, hand crossbows, longswords, rapiers, shortswords
Tools: Three musical instruments of your choice
Saving Throws: Dexterity, Charisma
Skills: Choose any three

Equipment
You start with the following equipment, in addition to the equipment granted by your background:
(a) a rapier, (b) a longsword, or (c) any simple weapon
(a) a diplomat's pack or (b) an entertainer's pack
(a) a lute or (b) any other musical instrument
Leather armor and a dagger

Bard Features
Spellcasting: You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.
Cantrips: You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table.
Spell Slots: The Bard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. For example, if you know the 1st-level spell Cure Wounds and have a 1st-level and a 2nd-level spell slot available, you can cast Cure Wounds using either slot.
Spells Known of 1st Level and Higher: You know four 1st-level spells of your choice from the bard spell list.
    The Spells Known column of the Bard table shows when you learn more bard spells of your choice. Each of these spells must be of a level for which you have spell slots, as shown on the table. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.
    Additionally, when you gain a level in this class, you can choose one of the bard spells you know and replace it with another spell from the bard spell list, which also must be of a level for which you have spell slots.
Spellcasting Ability: Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.
Spell save DC = 8 + your proficiency bonus + your Charisma modifier
Spell attack modifier = your proficiency bonus + your Charisma modifier
Ritual Casting: You can cast any bard spell you know as a ritual if that spell has the ritual tag.
Spellcasting Focus: You can use a musical instrument (found in chapter 5) as a spellcasting focus for your bard spells.

Bardic Inspiration: You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.
    Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.
    You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.
    Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.

Jack of All Trades: Starting at 2nd level, you can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus.

Song of Rest: Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance spend one or more Hit Dice to regain hit points at the end of the short rest, each of those creatures regains an extra 1d6 hit points.

Expertise: At 3rd level, choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.
At 10th level, you can choose another two skill proficiencies to gain this benefit.

Font of Inspiration: Beginning when you reach 5th level, you regain all of your expended uses of Bardic Inspiration when you finish a short or long rest.

Countercharm: At 6th level, you gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).

Magical Secrets: By 10th level, you have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any class, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.
    The chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.
    You learn two additional spells from any class at 14th level and again at 18th level.

Superior Inspiration: At 20th level, when you roll initiative and have no uses of Bardic Inspiration left, you regain one use.
'''
    elif class_name=='Cleric':
        return '''
Cleric Traits
Hit Points
Hit Dice: 1d8 per cleric level
Hit Points at 1st Level: 8 + your Constitution modifier
Hit Points at Higher Levels: 1d8 (or 5) + your Constitution modifier per cleric level after 1st

Proficiencies
Armor: Light armor, medium armor, shields
Weapons: All simple weapons
Tools: None
Saving Throws: Wisdom, Charisma
Skills: Choose two from History, Insight, Medicine, Persuasion, and Religion

Equipment
You start with the following equipment, in addition to the equipment granted by your background:
(a) a mace or (b) a warhammer (if proficient)
(a) scale mail, (b) leather armor, or (c) chain mail (if proficient)
(a) a light crossbow and 20 bolts or (b) any simple weapon
(a) a priest's pack or (b) an explorer's pack
A shield and a holy symbol

Cleric Features
Spellcasting: As a conduit for divine power, you can cast cleric spells.
Cantrips: At 1st level, you know three cantrips of your choice from the cleric spell list. You learn additional cleric cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Cleric table.
Spell Slots: The Cleric table shows how many spell slots you have to cast your spells of lst level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.
    You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list. When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level (minimum of one spell). The spells must be of a level for which you have spell slots.
    For example, if you are a 3rd-level cleric, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.
    You can change your list of prepared spells when you finish a long rest. Preparing a new list of cleric spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.
Spellcasting Ability: Wisdom is your spellcasting ability for your cleric spells. The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.
Spell save DC = 8 + your proficiency bonus + your Wisdom modifier
Spell attack modifier = your proficiency bonus + your Wisdom modifier
Ritual Casting: You can cast a cleric spell as a ritual if that spell has the ritual tag and you have the spell prepared.
Spellcasting Focus: You can use a holy symbol as a spellcasting focus for your cleric spells.

Channel Divinity: At 2nd level, you gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with two such effects: Turn Undead and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.
    When you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.
    Some Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.
    Beginning at 6th level, you can use your Channel Divinity twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses.
Channel Divinity: Turn Undead: As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.
    A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

Destroy Undead: Starting at 5th level, when an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown in the Cleric table above.

Divine Intervention: Beginning at 10th level, you can call on your deity to intervene on your behalf when your need is great.
    Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.
    At 20th level, your call for intervention succeeds automatically, no roll required.
'''

    else:
        return '''
        This class has not been added yet
        '''









      
        
class_list = ['Artificer','Barbarian','Bard','Cleric']
class_N=len(class_list)

class_dict = {}
for i in xrange(len(class_list)):
    class_dict[class_list[i]]=str(i)
#print(class_dict)



def test_classes():
    for i in xrange(len(class_list)):
        print class_description(class_list[i])
    return

#test_classes()
