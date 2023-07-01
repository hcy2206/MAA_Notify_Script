# MAA Notify Script

[![Pyhthon Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/downloads/release/python-370/)
[![GPLv3 License](https://img.shields.io/github/license/hcy2206/FIRMS_Data_Visualization)](https://opensource.org/licenses/GPL-3.0)

本项目是[MaaAssistantArknights](https://maa.plus)的一款辅助脚本，用于解决用户在电脑上通过定时运行 MAA 的方式进行自动化刷图时，无法及时得知本次运行的结果的问题。

基于 [PushDeer](http://pushdeer.com) 提供的 API，实现了一个简单的通知脚本，通过对于 MAA 运行日志的分析，实现了当 MAA 一次运行结束之后，通过 Pushdeer 的方式 向用户推送此次运行的结果，包括是否出错、一些错误日志以及本次运行所掉落的物品。

下图是一个通知的样例：
![IMG_5382](https://markdown-tuchuang-hcy2206.oss-cn-shanghai.aliyuncs.com/img/202307011605689.jpg)

## 使用方法

1. 安装 python，并确保它可以在命令行中运行，即打开命令行，输入`python -v`，如果出现 python 的版本信息，则说明安装成功。 如果你明确知道你没有安装 python，又不知道应该如何安装，推荐从 Microsoft Store 中安装 [Python3.11](https://www.microsoft.com/store/productId/9NRWMJP3717K)，点击安装即可，无需额外配置即可运行
5. 将脚本 `MAA-Notification.bat` 的绝对路径添加到 MAA 的`设置-连接设置-结束后脚本`中
6. 将`MAA-Notification.bat`中的`Your Path to main.py`替换为`main.py`的绝对路径
7. 在`main.py`中的`LOG_PATH`填入 MAA 日志文件`gui.log`的绝对路径，其应当位于 MAA 文件夹下`MAA-Arknights\debug\gui.log`如果没有，请先完整运行一次 MAA，确保其生成
8. 在`main.py`中的`PUSHDEER_SERVER`填入你的 PushDeer 服务器地址，如果使用官方服务器请留空，如`PUSHDEER_SERVER = ''`
9. 在`main.py`中的`PUSHDEER_KEY`填入你的key，简单来说需要使用 PushDeer 客户端获得 key，然后将其填入`PUSHDEER_KEY`中。如果使用官方服务器，iOS/iPadOS/MacOS 用户 请在 AppStore 中下载 [PushDeer](https://apps.apple.com/cn/app/pushdeer/id1596771139)，注册登录后即可获得 key。安卓用户和自架服务器版本请参考[PushDeer官网](http://pushdeer.com)的文档
10. Enjoy!
