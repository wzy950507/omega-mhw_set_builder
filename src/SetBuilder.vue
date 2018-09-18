<template>
  <div id="app">
    <el-container>
      <el-main>
        <standard-set-builder />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import StandardSetBuilder from './components/standard-set-builder/standard-set-builder'

export default {
  name: 'SetBuilder',
  components: {
    StandardSetBuilder: StandardSetBuilder
  }
}
</script>
<style lang="stylus">
#app
  margin 0
  padding 0
  vertical-align bottom
</style>
