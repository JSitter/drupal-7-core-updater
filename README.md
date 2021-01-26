# Drupal 7 Updater

## Version 1.0
This script updates your current Drupal 7 installation with the newest release available.
Latest available versions are available [here](https://www.drupal.org/project/drupal).

## Usage
`-h`, `--help` Help text with usage and available flags.

`-d`, `--download` Download Drupal from drupal.org. Automatically downloads latest version or specify different version to install.

`-f`, `--file` Specify local version of zipped Drupal package.

`--replace` Replace all existing files. **Warning** This will overwrite many custom files and should be used with great caution.

`-l`,  `--list` Display list of available versions. Provide an argument to limit to last N.

`-i`, `--install=INSTALL_LOCATION` Drupal installation location.

## MIT License

Copyright 2020 Justin Sitter

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.