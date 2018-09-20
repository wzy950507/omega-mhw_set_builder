<template>
  <div>{{ suits.length }}</div>
</template>

<script>
import { generateSuits } from '../utils/data-builder'

export default {
  name: 'AdvancedSetBuilder',
  data: function () {
    return {
      suits: []
    }
  }
}
</script>
