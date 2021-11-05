#!/usr/bin/python3
"""Generate names (or other strings) based on specialized templates"""

# SPDX-FileCopyrightText: 2021 Jeff Epler
#
# SPDX-License-Identifier: GPL-3.0-only

import sys
import random

symbols = {
    "'": ["'"],
    "-": ["-"],
    " ": [" "],
    "s": [
        "ach",
        "ack",
        "ad",
        "age",
        "ald",
        "ale",
        "an",
        "ang",
        "ar",
        "ard",
        "as",
        "ash",
        "at",
        "ath",
        "augh",
        "aw",
        "ban",
        "bel",
        "bur",
        "cer",
        "cha",
        "che",
        "dan",
        "dar",
        "del",
        "den",
        "dra",
        "dyn",
        "ech",
        "eld",
        "elm",
        "em",
        "en",
        "end",
        "eng",
        "enth",
        "er",
        "ess",
        "est",
        "et",
        "gar",
        "gha",
        "hat",
        "hin",
        "hon",
        "ia",
        "ight",
        "ild",
        "im",
        "ina",
        "ine",
        "ing",
        "ir",
        "is",
        "iss",
        "it",
        "kal",
        "kel",
        "kim",
        "kin",
        "ler",
        "lor",
        "lye",
        "mor",
        "mos",
        "nal",
        "ny",
        "nys",
        "old",
        "om",
        "on",
        "or",
        "orm",
        "os",
        "ough",
        "per",
        "pol",
        "qua",
        "que",
        "rad",
        "rak",
        "ran",
        "ray",
        "ril",
        "ris",
        "rod",
        "roth",
        "ryn",
        "sam",
        "say",
        "ser",
        "shy",
        "skel",
        "sul",
        "tai",
        "tan",
        "tas",
        "ther",
        "tia",
        "tin",
        "ton",
        "tor",
        "tur",
        "um",
        "und",
        "unt",
        "urn",
        "usk",
        "ust",
        "ver",
        "ves",
        "vor",
        "war",
        "wor",
        "yer",
    ],
    "v": ["a", "e", "i", "o", "u", "y"],
    "V": [
        "a",
        "e",
        "i",
        "o",
        "u",
        "y",
        "ae",
        "ai",
        "au",
        "ay",
        "ea",
        "ee",
        "ei",
        "eu",
        "ey",
        "ia",
        "ie",
        "oe",
        "oi",
        "oo",
        "ou",
        "ui",
    ],
    "c": [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ],
    "B": [
        "b",
        "bl",
        "br",
        "c",
        "ch",
        "chr",
        "cl",
        "cr",
        "d",
        "dr",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "ll",
        "m",
        "n",
        "p",
        "ph",
        "qu",
        "r",
        "rh",
        "s",
        "sch",
        "sh",
        "sl",
        "sm",
        "sn",
        "st",
        "str",
        "sw",
        "t",
        "th",
        "thr",
        "tr",
        "v",
        "w",
        "wh",
        "y",
        "z",
        "zh",
    ],
    "C": [
        "b",
        "c",
        "ch",
        "ck",
        "d",
        "f",
        "g",
        "gh",
        "h",
        "k",
        "l",
        "ld",
        "ll",
        "lt",
        "m",
        "n",
        "nd",
        "nn",
        "nt",
        "p",
        "ph",
        "q",
        "r",
        "rd",
        "rr",
        "rt",
        "s",
        "sh",
        "ss",
        "st",
        "t",
        "th",
        "v",
        "w",
        "y",
        "z",
    ],
    "i": [
        "air",
        "ankle",
        "ball",
        "beef",
        "bone",
        "bum",
        "bumble",
        "bump",
        "cheese",
        "clod",
        "clot",
        "clown",
        "corn",
        "dip",
        "dolt",
        "doof",
        "dork",
        "dumb",
        "face",
        "finger",
        "foot",
        "fumble",
        "goof",
        "grumble",
        "head",
        "knock",
        "knocker",
        "knuckle",
        "loaf",
        "lump",
        "lunk",
        "meat",
        "muck",
        "munch",
        "nit",
        "numb",
        "pin",
        "puff",
        "skull",
        "snark",
        "sneeze",
        "thimble",
        "twerp",
        "twit",
        "wad",
        "wimp",
        "wipe",
    ],
    "m": [
        "baby",
        "booble",
        "bunker",
        "cuddle",
        "cuddly",
        "cutie",
        "doodle",
        "foofie",
        "gooble",
        "honey",
        "kissie",
        "lover",
        "lovey",
        "moofie",
        "mooglie",
        "moopie",
        "moopsie",
        "nookum",
        "poochie",
        "poof",
        "poofie",
        "pookie",
        "schmoopie",
        "schnoogle",
        "schnookie",
        "schnookum",
        "smooch",
        "smoochie",
        "smoosh",
        "snoogle",
        "snoogy",
        "snookie",
        "snookum",
        "snuggy",
        "sweetie",
        "woogle",
        "woogy",
        "wookie",
        "wookum",
        "wuddle",
        "wuddly",
        "wuggy",
        "wunny",
    ],
    "M": [
        "boo",
        "bunch",
        "bunny",
        "cake",
        "cakes",
        "cute",
        "darling",
        "dumpling",
        "dumplings",
        "face",
        "foof",
        "goo",
        "head",
        "kin",
        "kins",
        "lips",
        "love",
        "mush",
        "pie",
        "poo",
        "pooh",
        "pook",
        "pums",
    ],
    "D": [
        "b",
        "bl",
        "br",
        "cl",
        "d",
        "f",
        "fl",
        "fr",
        "g",
        "gh",
        "gl",
        "gr",
        "h",
        "j",
        "k",
        "kl",
        "m",
        "n",
        "p",
        "th",
        "w",
    ],
    "d": [
        "elch",
        "idiot",
        "ob",
        "og",
        "ok",
        "olph",
        "olt",
        "omph",
        "ong",
        "onk",
        "oo",
        "oob",
        "oof",
        "oog",
        "ook",
        "ooz",
        "org",
        "ork",
        "orm",
        "oron",
        "ub",
        "uck",
        "ug",
        "ulf",
        "ult",
        "um",
        "umb",
        "ump",
        "umph",
        "un",
        "unb",
        "ung",
        "unk",
        "unph",
        "unt",
        "uzz",
    ],
    "z": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
}


def namegen(
    pattern, rng=random.randrange
):  # pylint: disable=too-many-branches, too-many-statements
    """Generate a name from the given pattern, with the given random number source"""
    depth = silent = literal = capstack = capitalize = 0
    reset = [0]
    n = [1]
    result = []

    for c in pattern:
        if c == "<":
            depth += 1
            bit = 1 << depth
            n.append(1)
            reset.append(len(result))
            literal &= ~bit
            silent &= ~bit
            silent |= (silent << 1) & bit
            capstack &= ~bit
            capstack |= capitalize << depth

        elif c == "(":
            depth += 1
            bit = 1 << depth
            n.append(1)
            reset.append(len(result))
            literal |= bit
            silent &= ~bit
            silent |= (silent << 1) & bit
            capstack &= ~bit
            capstack |= capitalize << depth

        elif c == ">":
            n.pop()
            reset.pop()
            if depth == 0:
                raise ValueError("Invalid pattern")
            bit = 1 << depth
            if literal & bit:
                raise ValueError("Invalid pattern")
            depth -= 1

        elif c == ")":
            n.pop()
            reset.pop()
            if depth == 0:
                raise ValueError("Invalid pattern")
            bit = 1 << depth
            if not (literal & bit):
                raise ValueError("Invalid pattern")
            depth -= 1

        elif c == "|":
            bit = 1 << depth
            if not (silent & (bit >> 1)):
                nd = n[depth] = n[depth] + 1
                if rng(nd) == 0:
                    del result[reset[depth] :]
                    silent &= ~bit
                    capitalize = bool(capstack & bit)
                else:
                    silent |= bit

        elif c == "!":
            capitalize = True

        else:
            bit = 1 << depth
            if not (silent & bit):
                if not (literal & bit):
                    s = symbols.get(c)
                    if s is None:
                        raise ValueError(f"Invalid metacharacter {c}")
                    c = s[rng(len(s))]
                if capitalize:
                    c = c[0].capitalize() + c[1:]
                    capitalize = 0
                result.append(c)

    if depth != 0:
        raise ValueError("Invalid pattern")
    return "".join(result)


if __name__ == "__main__":
    for template in sys.argv[1:]:
        print(end=f"{template!r}:")
        for _ in range(8):
            print(end=f" {namegen(template)!r}")
        print()
