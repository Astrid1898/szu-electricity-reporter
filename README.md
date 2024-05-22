
# SZU 宿舍电量微信提醒

## 简介

1. 使用 python 简单获取深圳大学特定的宿舍电量情况。
2. 借助 [Server 酱](http://sc.ftqq.com) 将电量情况发送至微信上。
3. 可配合开机自启动完成每日电量提醒功能。

<br/>

## 提醒内容

- 每日使用电量情况
- 每日剩余电量情况
- 近几日电量详表
- 每日购入电量情况

<br/>

## 效果

微信信息提醒：

![msg.jpg](https://i.loli.net/2019/10/22/9pOLRsrvIWe5Tqn.jpg)

详细数据：

![detail.jpg](https://i.loli.net/2019/10/22/H2w1zFVvcltLjA6.jpg)

<br/>

## 注意

- 项目简陋，仅为正好可用的程度，存在许多可以优化与改进的空间；
- 电量查询表单的更新存在延迟，如果 remind_time 设置了过早的时间，可能无法获取到前一天的电量情况；
- 2021 年 4 月起，Server 酱对微信通知服务进行了升级，服务细节需自行确认；

<br/>

## 项目结构

- [main.py](main.py)  
  主程序，获得数据并计算电量的报表数值

- [crawler.py](crawler.py)  
  发送电量查询请求，并进行简单数据整理的代码

- [scsender.py](scsender.py)  
  通过 Server 酱 进行微信提醒

<br/>

## 使用方法

注意：本脚本需要配置 config.json 文件的内容

必填参数含义：

| 参数名       | 含义                           | 例子            |
| ------------ | ------------------------------ | --------------- |
| room_name    | 宿舍房间号（下面有获取教程）   | "1101"          |
| room_id      | 宿舍楼栋 id（下面有获取教程）  | "7596"          |
| client       | （含义不清楚，下面有获取教程） | "192.168.84.87" |
| interval_day | 报表所要拉取的最近天数范围     | 14              |

选填参数含义：

| 参数名          | 含义                                        | 例子                             |
| --------------- | ------------------------------------------- | -------------------------------- |
| remind_daily    | 是否需要每日提醒（需要和 server 酱配合）    | true                             |
| server_chan_key | server 酱的密钥，用于微信提醒               | "https://sc.ftqq.com/xxxxx.send" |
| remind_time     | 每日提醒的时间（单位：时，整数，范围 0~23） | 9                                |

环境：深大校内网

1. 获取指定的宿舍信息。参数值获取途径（以 Chrome 浏览器 为例）：

   校内网环境，点击<kbd>F12</kbd>键或空白处`右键-检查`打开开发者工具，选择 Network 选项卡，登录深大 [SIMS 电控网上查询系统](http://192.168.84.3:9090/cgcSims/)，填写宿舍信息后，随便选择开始时间、结束时间、查询类型，点击查询，在开发者工具中选择 `selectList.do` 文件（如果没有该条记录，则尝试刷新页面），查看它的 POST 请求参数。

   ![network.jpg](https://ftp.bmp.ovh/imgs/2019/09/2021ada6023d5368.jpg)

   将 config.json 文件内的配置对应地替换为图中红框所包含的 `client`、`roomId`、`roomName` 参数即可。

2. 运行 `run_with_windows.exe`，或者用命令行执行 `python main.py`（需要安装 python 环境），稍等片刻即可得到电费报表。

   ![run_with_windows](https://i.loli.net/2021/01/15/aGRXeqSjpKyCdlE.png)

如果无需每日提醒，则到这里就结束了；

如果需要实现每日微信提醒的功能，可继续往下阅读：

3. 注册 Server 酱 账号，获得 SCKEY，填入 config.json 的 `server_chan_key`。

4. 运行 `run_with_windows.exe`，或者用命令行执行 `python main.py` 即可收到微信提醒。

5. 配置 `remind_daily` 为 `true`，则脚本将不会退出而常驻后台。我们可以选择运行 `run.exe`，该编译版本会在后台静默运行，而不会弹出命令行窗口。如果使用 `run_with_windows.exe` 或执行 `main.py`，会有命令行窗口常驻的情况。

6. 为了避免电脑重启后需要重新手动运行该程序，我们可以将 `run.exe` 添加为启动项。

> 这里介绍其中一种添加开启启动项的方法：
>
> 我们找到“启动”文件夹，windows 一般在以下目录：`C:\Users\{你的用户名}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
>
> 将 run.exe 的快捷方式放入其中即可

<br/>

## 更新日志
### 2024-05-23
- 修正耗电量计算错误
- 更为微信推送为最新版本


### 2021-04-14

- 添加注意声明
- 停止维护本项目

### 2021-01-31

- 添加 room_id 对照表

### 2021-01-15

- 将需要手动修改的配置抽取为 config.json 配置文件
- 使用 pyinstaller 打包 main.py 为 exe 可执行程序
- 将每日提醒逻辑移入程序中，弃用依赖系统提供的定时任务的方法
- 更新使用方法教程
- 项目更名为 szu-electricity-reporter

### 2019-10-25

- 修复永远显示“数据未更新”的 bug
- 修复控制台打印电量信息错误的问题
- 添加个人的计划任务配置参考图片

### 2019-10-22

- 完善了代码，改用字典存储
- 添加了部分注释便于阅读
- 修改了某些糟糕的代码写法
- 修改返回数据格式为“| 日期 | 今日用电 | 可用电量 | 今日充电 |”更加实用
- 修改了表格样式为居中对齐，效果相对有所改善
- 增加了爬取数据失败的提示

### 2019-09-24

添加判断是否充电并输出昨日充电额度

### 2019-09-23

发布项目

<br/>

## room_id 对照表

### 斋区

| 位置     | id    |
| -------- | ----- |
| 桃李斋   | 58    |
| 银桦斋   | 61    |
| 米兰斋   | 56    |
| 山茶斋   | 54    |
| 凌霄斋   | 59    |
| 海桐斋   | 57    |
| 红榴斋   | 55    |
| 聚翰斋   | 18118 |
| 红豆斋   | 18120 |
| 紫薇斋   | 18119 |
| 风槐斋   | 7126  |
| 雨鹃斋   | 7603  |
| 蓬莱客舍 | 17887 |

### 西南

| 位置            | id   |
| --------------- | ---- |
| 杜衡阁          | 73   |
| 文杏阁          | 70   |
| 海棠阁          | 71   |
| 辛夷阁          | 74   |
| 紫藤轩          | 77   |
| 紫檀轩          | 65   |
| 石楠轩          | 66   |
| 芸香阁          | 68   |
| 云杉轩          | 76   |
| 韵竹阁          | 75   |
| 疏影阁          | 72   |
| 木犀轩          | 63   |
| 丹枫轩          | 64   |
| 苏铁轩          | 67   |
| 丁香阁          | 69   |
| 乔梧阁 2-10 层  | 7724 |
| 乔梧阁 11-20 层 | 7725 |
| 乔森阁 11-20 层 | 6876 |
| 乔森阁 2-10 层  | 6875 |
| 乔木阁 1-10 层  | 6122 |
| 乔木阁 11-12 层 | 6364 |
| 乔相阁 2-10 层  | 6877 |
| 乔相阁 11-20 层 | 6878 |
| 乔林阁 1-10 层  | 6121 |
| 乔林阁 11-12 层 | 6363 |
| 留学生公寓      | 8147 |

### 西丽校区

| 位置       | id    |
| ---------- | ----- |
| A 栋风信子 | 10057 |
| B 栋山楂树 | 10934 |
| C 栋胡杨林 | 10935 |

### 南校区

| 位置          | id   |
| ------------- | ---- |
| 春笛 3-8 楼   | 6875 |
| 春笛 9-17 楼  | 7119 |
| 夏筝 3-17 楼  | 6876 |
| 秋瑟 3-8 楼   | 6877 |
| 秋瑟 9-17 楼  | 7828 |
| 冬筑 3-6 楼   | 6878 |
| 冬筑 7-10 楼  | 8240 |
| 冬筑 11-14 楼 | 8241 |
| 冬筑 15-17 楼 | 8242 |

<br/>
