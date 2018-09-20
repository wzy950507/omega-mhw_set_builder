<template>
<el-collapse-item :name="part" :title="part">
  <el-row>
    <el-col :span="8">
      <el-select v-model="selected" value-key="name" :placeholder="`请选择${part}`" @change="select" filterable clearable>
        <el-option v-for="equip in equipList" :key="equip.name" :label="equip.displayName || equip.name" :value="equip" />
      </el-select>
    </el-col>
    <el-col :span="16">
      <ul v-if="selected">
        <p>{{ selected }}</p>
      </ul>
    </el-col>
  </el-row>
</el-collapse-item>
</template>

<script>
import { makeArmor, makeCharm } from '../utils/data-builder'
export default {
  name: 'EquipSelector',
  props: {
    value: {
      type: Object
    },
    part: {
      type: String,
      default: '装备部位'
    }
  },
  data: function () {
    return {
      equipList: undefined,
      selected: undefined
    }
  },
  mounted: function () {
    if (this.part === '护石') {
      this.equipList = makeCharm()
    } else {
      this.equipList = makeArmor().filter(armor => {
        return armor.part === this.part
      })
    }
  },
  methods: {
    select: function (value) {
      this.$emit('input', value)
    }
  }
}
</script>
