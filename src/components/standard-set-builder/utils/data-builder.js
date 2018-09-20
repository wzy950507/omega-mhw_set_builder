import database from '@/assets/database/mhw-omega.json'

function makeArmor () {
  const armors = []
  database.armors.forEach(armorGroup => {
    armorGroup.contains.forEach(item => {
      const jsonItem = JSON.stringify(item)
      const armor = JSON.parse(jsonItem)
      armor.group = armorGroup.name
      armor.resist = armorGroup.resist
      if (armorGroup.skill !== undefined) {
        armor.skill = armorGroup.skill
      }
      armors.push(armor)
    })
  })
  return armors
}

function getSkillMaxLevel (skill) {
  let maxLevel = 0
  database.skills.forEach(item => {
    if (item.name === skill) {
      maxLevel = item.maxLevel
    }
  })
  return maxLevel
}

function makeJewel (slot) {
  const jewels = []
  database.jewels.forEach(item => {
    if (item.slot <= slot) {
      const jsonItem = JSON.stringify(item)
      const jewel = JSON.parse(jsonItem)
      jewel.displayName = `${jewel.name}【${jewel.slot}】（${jewel.skill}）`
      jewel.maxLevel = getSkillMaxLevel(jewel.skill)
      jewels.push(jewel)
    }
  })
  return jewels
}

function makeCharm () {
  const charms = []
  database.charms.forEach(item => {
    const jsonItem = JSON.stringify(item)
    const charm = JSON.parse(jsonItem)
    charm.displayName = `${charm.name}（${charm.skills[0].name}${charm.skills[1] ? `&${charm.skills[1].name}` : ''}）`
    charm.skills.forEach(skill => {
      skill.maxLevel = getSkillMaxLevel(skill.name)
    })
    charms.push(charm)
  })
  return charms
}

function generateSuits() {
  const armors = makeArmor()
  let suits = []
  makeCharm().forEach(charm => {
    suits.push({
      charm: charm
    })
  })
  const armorParts = {
    head: '头',
    chest: '胸',
    hand: '手',
    waist: '腰',
    leg: '腿'
  }
  for (let part in armorParts) {
    const tmpSuits = []
    armors.forEach(armor => {
      if (armor.part === armorParts[part]) {
        suits.forEach(item => {
          const jsonItem = JSON.stringify(item)
          const suit = JSON.parse(jsonItem)
          suit[part] = armor
          tmpSuits.push(suit)
        })
      }
    })
    suits = tmpSuits
  }
  return suits
}

export { makeArmor, makeJewel, makeCharm, getSkillMaxLevel, generateSuits }
