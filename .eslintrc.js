module.exports = {
  'root': true,
  'env': {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  'rules': {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-invalid-this': 0,
    'indent': ['error', 2],
    'no-process-env': 0
  },
  'parserOptions': {
    parser: 'babel-eslint'
  }
}
