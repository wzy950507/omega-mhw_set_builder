module.exports = {
  baseUrl: process.env.NODE_ENV === 'production' ? '/omega-mhw_set_builder/dist/' : '/',
  lintOnSave: true,
  configureWebpack: {
    mode: process.env.NODE_ENV
  }
}
