import os
import json
import codecs
import pickle

database = {}


def load_database(source='src/assets/database/mhw-omega.json'):
    global database
    with codecs.open(source, 'r', 'utf-8') as fin:
        database = json.load(fin)


def make_armor():
    armors = []
    for armor_group in database['armors']:
        for armor in armor_group['contains']:
            armor['group'] = armor_group['name']
            armor['resist ']= armor_group['resist']
            if 'skill' in armor_group:
                armor['skill'] = armor_group['skill']
            armors.append(armor)
    return armors


def make_max_level():
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


def check_skills(armors, max_level):
    checked = True
    for armor in armors:
        if 'skills' in armor:
            for skill in armor['skills']:
                if skill['name'] not in max_level:
                    print(armor['name'], skill['name'])
                    checked = False
    return checked


def make_suits(armors, max_level):
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


def make_armor_list(armors):
    parts = {
        'head': '头',
        'chest': '胸',
        'hand': '手',
        'waist': '腰',
        'leg': '腿'
    }
    armor_list = {}
    for part in parts:
        for armor in armors:
            if armor['part'] == parts[part]:
                armor_list.setdefault(part, [])
                armor_list[part].append(armor)
    return armor_list
    

def count_items(armor_list):
    print('charms', len(database['charms']))
    for part in armor_list:
        print(part, len(armor_list[part]))


jewels = {}


def make_jewels_dict():
    for jewel in database['jewels']:
        jewels[jewel['skill']] = jewel.copy()


def can_trans(a, b):
    a_slots = a['slots'].copy()
    b_slots = b['slots'].copy()
    for i in range(3):
        for j in range(i, 3):
            if a_slots[i] >= b_slots[i]:
                a_slots[i] -= b_slots[i]
                b_slots[i] = 0
                break
            else:
                b_slots[i] -= a_slots[i]
                a_slots[i] = 0
        if b_slots[i]:
            return False
    a_skills = {}
    if 'skills' in a:
        for skill in a['skills']:
            a_skills[skill['name']] = skill['level']
    b_skills = {}
    if 'skills' in b:
        for skill in b['skills']:
            b_skills[skill['name']] = skill['level']
    for skill in a_skills:
        if skill in b_skills:
            common_level = min(a_skills[skill], b_skills[skill])
            a_skills[skill] -= common_level
            b_skills[skill] -= common_level
    for skill in b_skills:
        if b_skills[skill]:
            if skill in jewels:
                skill_slot = jewels[skill]['slot'] - 1
                for i in range(skill_slot, 3):
                    if a_slots[i] >= b_skills[skill]:
                        a_slots[i] -= b_skills[skill]
                        b_skills[skill] = 0
                        break
                    else:
                        b_skills[skill] -= a_slots[i]
                        a_slots[i] = 0
                if b_skills[skill]:
                    return False
            else:
                return False
    return True
    

def make_trans(armor_list):
    for part in armor_list:
        for a in armor_list[part]:
            for b in armor_list[part]:
                if a['name'] == '锁甲手套β' and b['name'] == '锁甲手套α':
                    s=1
                if a is not b:
                    if can_trans(a, b):
                        a.setdefault('can_trans', [])
                        a['can_trans'].append(b['name'])


def main():
    load_database()
    make_jewels_dict()
    armors = make_armor()
    max_level = make_max_level()
    if not check_skills(armors, max_level):
        print('Check Failure.')
        return
    armor_list = make_armor_list(armors)
    count_items(armor_list)
    make_trans(armor_list)
    for part in armor_list:
        for a in armor_list[part]:
            if 'can_trans' in a:
                print(a['name'], a['can_trans'])


if __name__ == '__main__':
    main()
