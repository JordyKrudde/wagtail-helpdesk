const path = require('path');

module.exports = {
  entry: './wagtail_helpdesk/static_src/main.tsx',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.svg$/,
        use: ['@svgr/webpack'],
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: ['file-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  externals: {
    /* These are provided by Wagtail */
    'react': 'React',
    'react-dom': 'ReactDOM',
    'gettext': 'gettext',
  },
  output: {
    path: path.resolve(
      __dirname,
      'wagtail_helpdesk/static/wagtail_helpdesk/js'
    ),
    filename: 'wagtail-helpdesk.js'
  },
};
