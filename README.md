# FakeTranslate

## 安装(一定要全局安装，这样才能在任何地方打开终端窗口就能使用)
```
pip3 install fake-translate -i https://pypi.douban.com/simple
或
pipenv install fake-translate
```

## 使用
```
Usage: trans [OPTIONS] word

Options:
  --where             Output project home information.
  --envs              Output Environment Variable options.
  --man               Display manpage.
  --support           Output diagnostic information for use in GitHub issues.
  --clear             Clears caches
  -y                  有道翻译源
  -b                  百度翻译源
  -g                  谷歌翻译源
  -p                  金山词霸翻译源
  -v, --version       Show the version and exit.
  -h, --help          Show this message and exit.

Usage Examples:
  检测翻译源是否可用:
  $ trans check

  进入翻译环境:
  $ trans shell 

Commands:
  check      Checks for security vulnerabilities and against PEP 508 markers
             provided in Pipfile.
  clean      清理翻译缓存.
  shell      Spawns a shell within the virtualenv.
  update     更新翻译缓存.
  upgrade    升级库版本.

```

## 使用截图
![实例](https://github.com/HeywoodKing/faketranslate "实例")

## License
[GNU Affero General Public License v3 or later (AGPLv3+)](https://github.com/HeywoodKing/faketranslate "GNU Affero General Public License v3 or later (AGPLv3+)")


