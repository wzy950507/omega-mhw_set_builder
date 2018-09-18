<template>
<el-row>
  <el-col :span="8">
    <el-form :model="builder" label-width="80px">
      <el-form-item label="武器">
        <el-select v-model="builder.weapon" placeholder="请选择武器">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="头">
        <el-select v-model="builder.head" placeholder="请选择头">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="胸">
        <el-select v-model="builder.chest" placeholder="请选择胸">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="手">
        <el-select v-model="builder.hand" placeholder="请选择手">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="腰">
        <el-select v-model="builder.waist" placeholder="请选择腰">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="腿">
        <el-select v-model="builder.leg" placeholder="请选择腿">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="护石">
        <el-select v-model="builder.stone" placeholder="请选择护石">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
  </el-col>
  <el-col :span="16">
    <el-form label-position="top">
      <el-form-item label="1级槽">
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择1级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="2级槽">
        <el-select v-model="builder.leg" placeholder="请选择2级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择2级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择2级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择2级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择2级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="3级槽">
        <el-select v-model="builder.leg" placeholder="请选择3级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
        <el-select v-model="builder.leg" placeholder="请选择3级槽珠子">
          <el-option label="武器一" value="weapon1"></el-option>
          <el-option label="武器二" value="weapon2"></el-option>
        </el-select>
      </el-form-item>
    </el-form>
  </el-col>
  <el-col :span="24">
    <h1>----------TODO: 放置配装信息---------</h1>
  </el-col>
</el-row>
</template>

<script>
export default {
  name: 'StandardSetBuilder',
  data: function () {
    return {
      builder: { }
    }
  }
}
</script>

<style lang="stylus">
h1
  color red
</style>
