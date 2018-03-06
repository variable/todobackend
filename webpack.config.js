const path = require('path');

module.exports = {
  entry: './todobackend/static_src/js/todo/todo.js',
  output: {
    filename: 'todo.js',
    path: path.resolve(__dirname, 'todobackend', 'static', 'js', 'todo')
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
    }
  }
};
