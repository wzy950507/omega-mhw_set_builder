<template>
  <el-collapse-item :name="level" :title="`${level}级槽`">
    <el-select v-for="i in count" v-model="selected[i-1]" value-key="name" :key="i" :placeholder="`请选择${level}级槽珠子`" @change="select(selected)" filterable clearable>
      <el-option v-for="jewel in jewelList" :key="jewel.name" :value="jewel" :label="jewel.displayName" />
    </el-select>
  </el-collapse-item>
</template>

<script>
import { makeJewel } from '../utils/data-builder'
export default {
  name: 'SlotSelector',
  props: {
    value: {
      type: Array
    },
    level: {
      type: Number,
      default: 0
    },
    count: {
      type: Number,
      default: 0
    }
  },
  data: function () {
    return {
      jewelList: makeJewel(this.level),
      selected: []
    }
  },
  methods: {
    select: function (value) {
      this.$emit('input', value)
    }
  }
}
</script>
