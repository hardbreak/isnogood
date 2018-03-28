#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice


list_of_lotr_characters = [
    "Ælfwine of England", "Tar-Ardamin", "Túrin Turambar", "Adanel", "Adrahil",
    "Adrahil II", "Ar-Adûnakhôr", "Aegnor", "Aerin", "Agarwaen", "Aikanáro",
    "Aiwendil", "Alatar", "Alatáriel", "Tar-Alcarin", "Aldamir",
    "Tar-Aldarion", "Aldaron", "Aldor ", "Amandil", "Tar-Amandil", "Amdír",
    "Amlaith", "Amras", "Amrod", "Amroth ", "Amrothos", "Anairë", "Anardil",
    "Anárion", "Tar-Anárion", "Anborn", "Dragon ", "Tar-Ancalimë",
    "Tar-Ancalimon", "Andrast", "Tar-Anducal", "Anfauglir", "Andreth",
    "Andróg", "Angbor", "Angrod", "Annatar", "Arador", "Araglas", "Aragorn I",
    "Aragorn", "Aragost", "Arahad I", "Arahad II", "Arahael", "Aranarth",
    "Arantar", "Aranuir", "Araphant", "Araphor", "Arassuil", "Aratan",
    "Aratar", "Arathorn I", "Arathorn II", "Araval", "Aravir", "Aravorn",
    "Aredhel", "Tar-Ardamin", "Aredhel", "Argeleb I", "Argeleb II", "Argon",
    "Argonui", "Arien", "Aros", "Arthedain", "Arvedui", "Arvegil", "Arveleg I",
    "Arveleg II", "Arwen", "Asfaloth", "Tar-Atanamir", "Atanatar I",
    "Atanatar II", "Aulë", "Dior ", "Avranc", "Azaghâl", "Balbo Baggins",
    "Bilbo Baggins", "Bungo Baggins", "Frodo Baggins", "Baldor ", "Balin ",
    "Baragund ", "Barahir", "Baran (House of Bëor) ", "Bard the Bowman",
    "Bauglir", "Belecthor I", "Belecthor II", "Beleg", "Beleg of Arnor",
    "Belegorn", "Belegund ", "Belemir", "Bëor", "Beorn", "House of Bëor ",
    "Beregond", "Beren", "Bergil", "Berúthiel", "Bifur", "Bill Ferny",
    "Bill the Pony", "Troll ", "Boldog", "Berylla Boffin", "Bofur", "Bolg",
    "Fredegar Bolger", "Tom Bombadil", "Bombur ", "Boromir", "Boron  ",
    "Borondir", "Brand ", "Brand II", "Brandir", "Gormadoc Brandybuck",
    "Meriadoc Brandybuck", "Primula Brandybuck", "Brego", "Bregolas",
    "Bregor", "Brodda", "Brytta Léofa", "Bucca of the Marish",
    "Barliman Butterbur", "Calembel", "Calimehtar", "Tar-Calion", "Calmacil",
    "Tar-Calmacil", "Captain of the Haven", "Caranthir", "Carcharoth",
    "Castamir the Usurper", "Cemendur", "Celeborn", "Celebrían", "Celebrimbor",
    "Celebrindor", "Celegorm", "Celepharn", "Círdan", "Cirion", "Ciryaher",
    "Ciryandil", "Tar-Ciryatan", "Ciryon", "Rosie Cotton", "Curufin",
    "Curunír", "Daeron", "Dáin I", "Dáin II Ironfoot", "Daughters of Finwë",
    "Déagol", "Denethor", "Déor", "Rohan ", "Dernhelm",
    "Diamond of Long Cleeve", "Dior ", "Dís ", "Dori ", "Dorlas", "Draugluin",
    "Duilin", "Durin", "Durin II", "Durin III", "Durin IV", "Durin V",
    "Durin VI", "Durin VII", "Durin's Bane", "Dwalin", "Eärendil",
    "Eärendil of Gondor", "Eärendur of Andúnië", "Eärendur of Arnor",
    "Eärendur son of Tar-Amandil", "Eärnil I", "Eärnil II", "Eärnur", "Eärwen",
    "Ecthelion of the Fountain", "Ecthelion I", "Ecthelion II", "Egalmoth",
    "Eilinel ", "Elanor the Fair", "Elbereth", "Eldacar of Arnor",
    "Eldacar of Gondor", "Eldarion", "Elemmakil", "Elendil", "Tar-Elendil",
    "Elendor", "Elendur of Arnor", "Elendur son of Isildur", "Elenna",
    "Elenwë", "Aragorn", "Elfhelm", "Elfhild", "Elfwine ", "Elladan", "Elmo ",
    "Elrohir", "Elrond", "Elros", "Thingol", "Eluréd and Elurín", "Elwë",
    "Elwing", "Elven-king", "Emeldir ", "Emerië", "Awakening of the Elves",
    "Enelyë", "Eöl", "Éomer", "Éomund", "Eönwë", "Eorl the Young", "Éothain",
    "Éothéod", "Éowyn", "Eradan", "Erendis", "Erestor", "Erkenbrand",
    "Eru Ilúvatar", "Estel", "Estelmo", "Estë", "Tar-Falassion", "Faniel",
    "Faramir", "Fastred of Greenholm", "Fëanor", "Felaróf", "Female hobbits",
    "Fengel", "Bill Ferny", "Fíli and Kíli", "Finarfin", "Findis", "Finduilas",
    "Finduilas of Dol Amroth", "Fingolfin", "Fingon", "Finrod Felagund",
    "Finvain", "Finwë", "Fíriel", "Folcwine", "Forlong the Fat", "Fréa",
    "Fréaláf Hildeson", "Fréawine", "Freca", "Frerin", "Frór", "Fuinur",
    "Fundin ", "Galador", "Galadriel", "Galdor of Gondolin", "Galdor the Tall",
    "Galdor of the Havens", "Hamfast Gamgee", "Samwise Gamgee", "Gamil Zirak",
    "Gamling", "Gandalf", "Ghân-buri-Ghân", "Gil-galad", "Gildor Inglorion",
    "Gilrain", "Gimilkhâd", "Ar-Gimilzôr", "Gimli ", "Ginglith", "Girion",
    "Glanhír", "Glaurung", "Glóin", "Glóredhel ", "Glorfindel", "Goldberry",
    "Goldwine", "Golfimbul", "Gollum", "Gorbag", "Gorlim", "Gorthaur",
    "Gothmog", "Gram ", "Gríma", "Grimbold", "Grishnákh", "Grór", "Gwaihir",
    "Gwathir", "Gwindor", "Hador ", "Halbarad", "Haldad", "Haldar",
    "Haldir of Lórien", "Haleth", "Hallas", "Halmir", "Háma ", "Handir",
    "Hardang", "Hareth ", "Helm Hammerhand", "Herion", "Herucalmo", "Herumor",
    "Tar-Herunúmen", "Hiril (House of Bëor) ", "Hiril (House of Haleth)",
    "Tar-Hostamir", "Huan ", "Huor", "Húrin I", "Húrin II", "Húrin the Tall",
    "Hyarmendacil I", "Hyarmendacil II", "Ibûn", "Idril", "Ilmarë",
    "Ilúvatar", "Imbar", "Imin", "Iminyë", "Imrahil", "Indis", "Inglor",
    "Ingwë", "Ar-Inziladûn", "Inzilbêth", "Írildë", "Irimë", "Lórien (Vala)",
    "Isildur", "Isilmë", "Isilmo", "Ivriniel", "Khamûl", "Khîm", "Fíli",
    "Kíli", "Lagduf", "Lalaith", "Legolas", "Lenwë", "Léod", "Lindir",
    "Lugdush", "Lúthien", "Lurtz", "Mablung", "Maedhros", "Maeglin",
    "Farmer Maggot", "Maglor", "Magor", "Mahtan", "Malach", "Malbeth the Seer",
    "Mallor", "Malvegil", "Manthor", "Manwë", "Marach", "Mardil Voronwë",
    "Mauhúr", "Melian", "Meriadoc Brandybuck", "Meleth", "Meneldil",
    "Tar-Meneldur", "Mîm", "Minalcar", "Minardil", "Tar-Minastir",
    "Tar-Minyatur", "Míriel Ar-Zimraphel", "Míriel Serindë", "Mithrandir",
    "Morgoth", "Morwen", "Morwen Steelsheen", "Muzgash", "Nahar",
    "Náin, son of Grór", "Náin I", "Náin II", "Mandos", "Narmacil I",
    "Narmacil II", "Narvi ", "Nerdanel", "Nessa ", "Nienna", "Nienor",
    "Nimloth", "Nimrodel", "Níniel", "Nóm", "Nori ", "Ohtar",
    "Óin, son of Glóin", "Óin, son of Gróin", "Olórin", "Olwë", "Ondoher",
    "Ori", "Ornendil", "Orodreth", "Oromë", "Oropher", "Orophin", "Ossë",
    "Ostoher", "Pallando", "Tar-Palantir", "Pelendur", "Pengolodh",
    "Ar-Pharazôn", "Peregrin Took", "Queen Berúthiel", "Bregalad", "Radagast",
    "Rían", "Rómendacil I", "Rómendacil II", "Rúmil",
    "Lobelia Sackville-Baggins", "Lotho Sackville-Baggins", "Sador", "Saeros",
    "Ar-Sakalthôr", "Salgant", "Salmar", "Saruman", "Sauron",
    "Scatha the Worm", "Shagrat ", "Shelob", "Silmariën", "Singollo",
    "Siriondil", "Smaug", "Sméagol", "Snowmane", "Soronto", "Aragorn",
    "Tar-Súrion", "Tal-Elmar", "Tarcil", "Tarannon Falastur", "Tata ", "Tatië",
    "Telchar", "Tar-Telemmaitë", "Telemnar", "Tar-Telemnar", "Tar-Telperiën",
    "Telumehtar", "Thengel", "Théoden", "Théodred", "Théodwyn", "Thingol",
    "Thorin I", "Thorin Oakenshield", "Thorin III Stonehelm", "Thorondir",
    "Thorondor", "Thráin I", "Thráin II", "Thranduil", "Thrór", "Tilion",
    "Tindomiel", "Tinúviel", "Tom Bombadil", "Adalgrim Took",
    "Belladonna Took", "Bullroarer Took", "Faramir Took", "Ferumbras III Took",
    "Fortinbras Took II", "Gerontius Took", "Isumbras Took", "Paladin Took",
    "Paladin Took II", "Pearl Took", "Peregrin Took", "Pervinca Took",
    "Pimpernel Took", "Treebeard", "Aragorn", "Tulkas", "Tuor", "Turgon",
    "Turambar", "Túrin Turambar", "Túrin I", "Túrin II", "Ufthak", "Uglúk",
    "Uinen", "Uldor", "Ulfang", "Ulfast", "Ulwarth", "Ulmo", "Umbardacil",
    "Undómiel", "Ungoliant", "Uolë Kúvion", "Urwen", "Vairë", "Valacar",
    "Valandil of Andúnië", "Valandil of Arnor", "Valandur", "Vána",
    "Tar-Vanimeldë", "Varda", "Vardamir Nólimon", "Vidugavia", "Vidumavi",
    "Vinyarion", "Vorondil the Hunter", "Voronwë", "Walda",
    "Watcher in the Water", "Witch-king of Angmar", "Gríma Wormtongue",
    "Will Whitfoot", "Yavanna", "Yávien", "Ar-Zimraphel", "Ar-Zimrathôn"
]


def get_lotr_name():
    """
    Get a random name from character list

    :return: a random name from character list (stripped)
    :rtype: str
    """
    return choice(get_lotr_names(sorted=False))


def get_lotr_names(sorted=True):
    """
    Get all unique names from character list

    :param sorted: sort names before returning them
    :type sorted: bool
    :return: all unique names from character list (stripped)
    :rtype: list
    """
    names = list(set([name.strip() for name in list_of_lotr_characters]))
    if sorted:
        names.sort()
    return names


if __name__ == "__main__":
    print(get_lotr_name())
