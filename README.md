# omega-mhw_set_builder
MHW配装器

# 开发环境
1. [VS Code](https://aka.ms/win32-x64-user-stable)
2. [Git for Windows](https://github.com/git-for-windows/git/releases/download/v2.19.0.windows.1/Git-2.19.0-64-bit.exe)
3. [node.js](https://nodejs.org/dist/v8.12.0/node-v8.12.0-x64.msi)
4. [vue](https://cn.vuejs.org/)
5. [element-ui](http://element-cn.eleme.io/#/zh-CN)
6. [git工作流说明](https://zhuanlan.zhihu.com/p/39148914)

# 数组库
数据库存放技能、珠子、武器、防具、套装效果等信息，供配装器使用。数据采用[json](http://www.runoob.com/json/json-syntax.html)描述。
## 技能
技能数据存放在"skills"数组内，包含以下若干字段
+ 定义：（TODO：考虑加上技能效果）
    * "name": 技能名称
    * "max_level": 最高等级
+ 样例
``` json
{
    "skills": [{
        "name": "毒耐性",
        "max_level": 3
    }]
}
```
## 珠子
珠子数据存放在"jewels"数组内，包含以下若干字段
+ 定义：
    * "name": 珠子名称，string
    * "slot": 插孔等级，int
    * "rare": 稀有度，int
    * "skill": 技能名称，string
+ 样例
``` json
{
    "jewels": [{
        "name": "耐毒珠",
        "slot": 1,
        "rare": 5,
        "skill": "毒耐性"
    }]
}
```
## 防具
防具数据存放在"armor"数组内，包含以下若干字段
+ 定义：
    * "name": 套装名称，string
    * "resist": 属性耐性，[火，水，雷，冰，龙]，array of int
    * "contains": 套装包含的防具列表，array
        - "part": <头|胸|手|腰|腿> 装备部位，string
        - "slots": 插槽数量，[1级，2级，3级]，array of int
        - "skills": 技能列表，当且仅当有技能时字段存在
            + "name": 技能名称
            + "level": 技能等级
    * "skill": 套装效果的技能名，当且仅当存在套装效果时存在
+ 样例:
``` json
{
    "armors": [{
        "name": "火龙β",
        "resist": [3, 1, -2, 1, -3],
        "contains": [{
            "name": "火龙头盔β",
            "part": "头",
            "slots": [1, 0, 0],
            "skills": [{
                "name": "攻击",
                "level": 2
            }]
        }, {
            "name": "火龙铠甲β",
            "part": "胸",
            "slots": [1, 0, 0],
            "skills": [{
                "name": "弱点特效",
                "level": 2
            }]
        }, {
            "name": "火龙腕甲β",
            "part": "手",
            "slots": [1, 0, 0],
            "skills": [{
                "name": "火耐性",
                "level": 2
            }]
        }, {
            "name": "火龙腰甲β",
            "part": "腰",
            "slots": [0, 1, 0],
            "skills": [{
                "name": "火属性攻击强化",
                "level": 2
            }]
        }, {
            "name": "火龙护腿β",
            "part": "腿",
            "slots": [0, 0, 1],
            "skills": [{
                "name": "跳跃铁人",
                "level": 1
            }]
        }],
        "skill": "火龙奥秘"
    }]
}
```

# 需求列表（*少的为主要功能）
1. （*）完善数据库
2. （*）基本配装界面
    + 左侧选取装备
        * 武器
        * 头
        * 胸
        * 手
        * 腰
        * 腿
        * 护石
    + 右侧根据所选装备统计插槽，供插珠子使用
        * 1级插槽
        * 2级插槽
        * 3级插槽
    + 下方输出配装信息
        * 部位装备名称
        * 技能发动
        * 所需珠子列表
3. （**）高级配装界面
    + 根据技能检索搭配，给出列表，选中后填入基本配装界面
    + （没想好）
4. （***）配装的导出与存储
    + 优先导出，格式json（这样可以直接挂在gitpage不用自己建服务器）
    + 配套导入功能