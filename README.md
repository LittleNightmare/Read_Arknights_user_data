# Read_Arknights_user_data
处理明日方舟自身仓库数据，方便支持的的网页工具箱导入
# 注意事项
该工具的基础数据需要自行抓包

**有可能**违反明日方舟相关条例
# 使用说明
### Prepare
抓取登陆明日方舟的数据包，涉及到解HTTPS

#### 数据包特征
```
之前的包:
https://ak-gs.hypergryph.com:8443/account/login
数据来源:
https://ak-gs.hypergryph.com:8443/account/syncData
```
### First
需要将json数据手动创建并导入 ~~复制粘贴~~ 到`arknights user data_login.json`中
然后运行`reader.py`
### Final
随后会生成两个文件`ArkPlaner.json`和`lolicon.txt`

可以直接通过复制粘贴的方式导入到对应网站
# 支持网站
可能支持其他明日方舟网页计算器
### ArkPlaner.json
[ArkPlaner](https://github.com/ycremar/ArkPlanner)
### lolicon.txt
[arknights-toolbox](https://github.com/Tsuk1ko/arknights-toolbox)
# 鸣谢
文件`item_table.json`来自 [明日方舟游戏数据](https://github.com/Perfare/ArknightsGameData)

网页列表来自[awesome-Arknights](https://github.com/cyf-gh/awesome-Arknights)