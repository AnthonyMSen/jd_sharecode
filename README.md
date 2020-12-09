# jd_sharecode

在`jd_shareCode.json`中填写你拥有的账号信息，包含`cookie`的写在`own`中，只有`sharecode`的写在`frd`中，注意格式正确，建议复制粘贴后修改。

把 `jd_shareCode.py`和`jd_shareCode.json`文件放在同一目录下，运行
```sh
python jd_shareCode.py
```
即可输出组合完的sharecode，可以方便地复制到`docker-compose.yml`中

你可以根据你的拥有的账号和朋友的sharecode放置在json文件中的不同位置，尽量填满，不然可能会有bug，需要手动检查一下是否符合规则

值得注意的是，`pt_kry`和`pt_pin`这两项，不需要`;`，标点符号会在汇总时加入的，后期可能会多加点判断规则吧。。。

