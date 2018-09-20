<template>
<el-tabs type="border-card" :value="tabSelect">
  <el-tab-pane label="武器" name="weapons" />
  <el-tab-pane label="防具" name="armors">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-table :data="equipList" :height="tableHeight">
          <el-table-column label="装备组" prop="name" width="120px" />
          <el-table-column label="装备部位">
            <template slot-scope="scope">
              <el-button v-if="scope.row.contains.map(item => item.part).indexOf('头') === -1" type="danger" icon="el-icon-close" plain circle disabled />
              <el-button v-else type="primary" plain circle @click="showInfo(scope.row, '头')">头</el-button>
              <el-button v-if="scope.row.contains.map(item => item.part).indexOf('胸') === -1" type="danger" icon="el-icon-close" plain circle disabled />
              <el-button v-else type="primary" plain circle @click="showInfo(scope.row, '胸')">胸</el-button>
              <el-button v-if="scope.row.contains.map(item => item.part).indexOf('手') === -1" type="danger" icon="el-icon-close" plain circle disabled />
              <el-button v-else type="primary" plain circle @click="showInfo(scope.row, '手')">手</el-button>
              <el-button v-if="scope.row.contains.map(item => item.part).indexOf('腰') === -1" type="danger" icon="el-icon-close" plain circle disabled />
              <el-button v-else type="primary" plain circle @click="showInfo(scope.row, '腰')">腰</el-button>
              <el-button v-if="scope.row.contains.map(item => item.part).indexOf('腿') === -1" type="danger" icon="el-icon-close" plain circle disabled />
              <el-button v-else type="primary" plain circle @click="showInfo(scope.row, '腿')">腿</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
      <el-col :span="16">
        <el-card class="box-card" :height="tableHeight">
          <div slot="header" class="clearfix">
            <span>装备详情</span>
          </div>
          <el-form v-if="selectedItem" label-width="80px">
            <el-form-item label="装备组">
              <span v-text="selectedItem.group" />
            </el-form-item>
            <el-form-item label="装备名称">
              <span v-text="selectedItem.name" />
            </el-form-item>
            <el-table :data="[selectedItem.resist]">
              <el-table-column align="center" label="装备耐性">
                <el-table-column align="center" label="火耐性" prop="[0]"></el-table-column>
                <el-table-column align="center" label="水耐性" prop="[1]"></el-table-column>
                <el-table-column align="center" label="雷耐性" prop="[2]"></el-table-column>
                <el-table-column align="center" label="冰耐性" prop="[3]"></el-table-column>
                <el-table-column align="center" label="龙耐性" prop="[4]"></el-table-column>
              </el-table-column>
            </el-table>
            <el-form-item v-if="selectedItem.slots.map(i => i > 0).indexOf(true) !== -1" label="装备插槽">
              <div v-for="(slot, index) in selectedItem.slots" :key="index">
                <span v-if="slot" v-text="`${slot}个${index+1}级插槽`" />
              </div>
            </el-form-item>
            <el-form-item v-if="selectedItem.skills" label="装备技能">
              <div v-for="(skill, index) in selectedItem.skills" :key="index">
                <span v-text="`${skill.level}级${skill.name}`" />
              </div>
            </el-form-item>
          </el-form>
        </el-card>
      </el-col>
    </el-row>
  </el-tab-pane>
  <el-tab-pane label="护石" name="charms">
    <el-table :data="charmList" :height="tableHeight" :row-class-name="({row, rowIndex}) => row.color">
      <el-table-column type="index" />
      <el-table-column label="护石" prop="name" />
      <el-table-column label="技能（技能最高等级）" sortable :sort-method="(a, b) => getSkillMaxLevel(a.skills[0].name) - getSkillMaxLevel(b.skills[0].name)">
        <template slot-scope="scope">
          <div v-for="skill in scope.row.skills" :key="skill.name">
            {{ `${skill.name}（${getSkillMaxLevel(skill.name)}）` }}
          </div>
        </template>
      </el-table-column>
      <el-table-column label="最高强化等级" prop="skills[0].level" sortable />
    </el-table>
  </el-tab-pane>
  <el-tab-pane label="珠子" name="jewels">
    <el-table :data="jewelList" :height="tableHeight">
      <el-table-column type="index" />
      <el-table-column label="装饰珠" prop="name" />
      <el-table-column label="镶嵌等级" prop="slot" sortable />
      <el-table-column label="稀有度" prop="rare" sortable />
      <el-table-column label="对应技能" prop="skill" />
      <el-table-column label="技能最高等级" prop="maxLevel" sortable />
    </el-table>
  </el-tab-pane>
  <el-tab-pane label="套装效果" name="suits" />
  <el-tab-pane label="技能" name="skills">
    <el-table :data="skillList" :height="tableHeight">
      <el-table-column type="index" />
      <el-table-column label="技能名称" prop="name" />
      <el-table-column label="技能最高等级" prop="maxLevel" sortable />
      <el-table-column label="效果（仅包含影响攻击和会心的效果）">
        <template slot-scope="scope" v-if="scope.row.effects">
          <div v-for="effect in scope.row.effects" :key="effect.level">
            <div>{{ `${effect.level}级${effect.effect.attack ? ` 攻击 +${effect.effect.attack}` : ''}${effect.effect.affinity ? ` 会心率 +${effect.effect.affinity}%` : ''}` }}</div>
          </div>
        </template>
      </el-table-column>
    </el-table>
  </el-tab-pane>
</el-tabs>
</template>

<script>
import database from '@/assets/database/mhw-omega.json'
import { getSkillMaxLevel, makeJewel, makeCharm } from '../utils/data-builder'

export default {
  name: 'EquipDatabase',
  data: function () {
    return {
      tabSelect: 'armors',
      tableHeight: 'calc(100vh - 200px)',
      equipList: database.armors,
      jewelList: makeJewel(3),
      charmList: makeCharm(),
      skillList: database.skills,
      selectedItem: undefined
    }
  },
  methods: {
    showInfo: function (row, part) {
      const itemJson = JSON.stringify(row.contains[row.contains.map(item => item.part).indexOf(part)])
      this.selectedItem = JSON.parse(itemJson)
      this.selectedItem.group = row.name
      this.selectedItem.resist = row.resist
      if (row.skill !== undefined) {
        this.selectedItem.skill = row.skill
      }
    },
    getSkillMaxLevel: function (skill) {
      return getSkillMaxLevel(skill)
    }
  }
}
</script>

<style lang="stylus">
.el-table tr
  &.米黄
    color #9CBB2B
  &.浅绿
    color #409D41
  &.深绿
    color #7496A3
  &.深紫
    color #5B6EEE
  &.浅紫
    color #A661E3
  &.橙黄
    color #F78A5B
</style>
