<template>
<el-tabs :value="tabSelect">
  <el-tab-pane label="mhw-ω-database" name="equip-database">
    <equip-database />
  </el-tab-pane>
  <el-tab-pane label="基本配装" name="standard-builder">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-collapse :value="euqipSelect">
          <equip-selector part="武器" />
          <equip-selector v-model="builder.head" part="头" />
          <equip-selector v-model="builder.chest" part="胸" />
          <equip-selector v-model="builder.hand" part="手" />
          <equip-selector v-model="builder.waist" part="腰" />
          <equip-selector v-model="builder.leg" part="腿" />
          <equip-selector v-model="builder.charm" part="护石" />
        </el-collapse>
      </el-col>
      <el-col :span="16">
        <el-collapse :value="slotSelect">
          <slot-selector v-model="builder.slots[0]" :level="1" :count="slots[0]" />
          <slot-selector v-model="builder.slots[1]" :level="2" :count="slots[1]" />
          <slot-selector v-model="builder.slots[2]" :level="3" :count="slots[2]" />
        </el-collapse>
        <el-table :data="[resist]">
          <el-table-column align="center" label="配装详情">
            <el-table-column align="center" label="装备耐性">
              <el-table-column align="center" label="火耐性" prop="[0]"></el-table-column>
              <el-table-column align="center" label="水耐性" prop="[1]"></el-table-column>
              <el-table-column align="center" label="雷耐性" prop="[2]"></el-table-column>
              <el-table-column align="center" label="冰耐性" prop="[3]"></el-table-column>
              <el-table-column align="center" label="龙耐性" prop="[4]"></el-table-column>
            </el-table-column>
          </el-table-column>
        </el-table>
        <el-alert v-for="(level, name) in skills" :key="name" :title="`${level}级${name}`" :type="skillClass(name, level)"/>
        <h1>jewels: {{ jewels }}</h1>
      </el-col>
    </el-row>
  </el-tab-pane>
  <el-tab-pane label="高级配装" name="advanced-set-builder">
    <advanced-set-builder />
  </el-tab-pane>
</el-tabs>
</template>

<script>
import EquipDatabase from './equip-database/equip-database'
import EquipSelector from './equip-selector/equip-selector'
import SlotSelector from './equip-selector/slot-selector'
import AdvancedSetBuilder from './advanced-set-builder/advanced-set-builder'
import { getSkillMaxLevel } from './utils/data-builder'

export default {
  name: 'StandardSetBuilder',
  components: {
    EquipDatabase,
    EquipSelector,
    SlotSelector,
    AdvancedSetBuilder
  },
  data: function () {
    return {
      tabSelect: 'equip-database',
      euqipSelect: ['头', '胸', '手', '腰', '腿', '护石'],
      slotSelect: [1, 2, 3],
      builder: {
        slots: []
      }
    }
  },
  computed: {
    resist: function () {
      const resist = [0, 0, 0, 0, 0]
      for (const equip in this.builder) {
        if (this.builder[equip].resist !== undefined) {
          this.builder[equip].resist.forEach((r, i) => {
            resist[i] += r
          })
        }
      }
      return resist
    },
    slots: function () {
      const slots = [0, 0, 0]
      for (const equip in this.builder) {
        if (this.builder[equip].slots !== undefined) {
          this.builder[equip].slots.forEach((r, i) => {
            slots[i] += r
          })
        }
      }
      return slots
    },
    jewels: function () {
      const jewels = {}
      const slots = this.slots
      for (let i = 0; i < 3; i++) {
        for (let j = 0; this.builder.slots[i] !== undefined && j < slots[i]; j++) {
          const jewel = this.builder.slots[i][j]
          const name = jewel === undefined || jewel === '' ? `${i + 1}级槽` : jewel.name
          const skill = name === `${i + 1}级槽` ? undefined : jewel.skill
          if (!(name in jewels)) {
            jewels[name] = {
              count: 0,
              skill: skill
            }
          }
          jewels[name].count += 1
        }
      }
      return jewels
    },
    skills: function () {
      const skills = {}
      const updateSkill = function (name, level) {
        if (!(name in skills)) {
          skills[name] = 0
        }
        skills[name] += level
      }
      for (const equip in this.builder) {
        const equipSkills = this.builder[equip].skills
        if (equipSkills !== undefined) {
          equipSkills.forEach(skill => {
            updateSkill(skill.name, skill.level)
          })
        }
      }
      for (const name in this.jewels) {
        const jewel = this.jewels[name]
        if (jewel.skill !== undefined) {
          updateSkill(jewel.skill, jewel.count)
        }
      }
      return skills
    }
  },
  methods: {
    skillClass: function (skill, level) {
      const maxLevel = getSkillMaxLevel(skill)
      if (level < maxLevel) {
        return 'info'
      } else if (level === maxLevel) {
        return 'warning'
      }
      return 'error'
    }
  }
}
</script>
