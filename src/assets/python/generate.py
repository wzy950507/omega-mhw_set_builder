import os
import json
import codecs
import pickle


def load_database(database='mhw-omega.json'):
    with codecs.open(database, 'r', 'utf-8') as fin:
        return json.load(fin)


def make_armor(database):
    armors = []
    for armor_group in database['armors']:
        for armor in armor_group['contains']:
            armor['group'] = armor_group['name']
            armor['resist ']= armor_group['resist']
            if 'skill' in armor_group:
                armor['skill'] = armor_group['skill']
            armors.append(armor)
    return armors


def make_max_level(database):
    max_level = {}
    for skill in database['skills']:
        max_level[skill['name']] = skill['maxLevel']
    return max_level


def suitable(suit, max_level):
    skills = {}
    for item in suit:
        if 'skills' in suit[item]:
            for skill in suit[item]['skills']:
                skills.setdefault(skill['name'], 0)
                skills[skill['name']] += skill['level']
    for skill in skills:
        if skills[skill] > max_level[skill]:
            return False
    return True


def main():
    database = load_database()
    armors = make_armor(database)
    max_level = make_max_level(database)
    parts = {
        'head': '头',
        'chest': '胸',
        'hand': '手',
        'waist': '腰',
        'leg': '腿'
    }
    if not os.path.isfile('suits_charm.pkl'):
        suits = [{'charm':charm} for charm in database['charms']]
        with codecs.open('suits_charm.pkl', 'wb') as fout:
            pickle.dump(suits, fout)
    with codecs.open('suits_charm.pkl', 'rb') as fin:
        suits = pickle.load(fin)
    for part in parts:
        print(len(suits))
        print(part)
        filename = 'suits_%s.pkl' % part
        if not os.path.isfile(filename):
            tmp_suits = []
            for armor in armors:
                if armor['part'] == parts[part]:
                    for suit in suits:
                        new_suit = suit.copy()
                        new_suit[part] = armor
                        if suitable(new_suit, max_level):
                            tmp_suits.append(new_suit)
            with codecs.open(filename, 'wb') as fout:
                pickle.dump(tmp_suits, fout)
        with codecs.open(filename, 'rb') as fin:
            suits = pickle.load(fin)
    print(len(suits))


if __name__ == '__main__':
    main()
