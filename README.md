## 自动化项目
> 快速回归app前后端业务,保障产品质量
### app前端目录结构
```
- appPage           前端页面
- common    
    - LocateUtil    定位、事件、断言通用类

- testcase          测试用例库
- testdata          基础测试数据
- config            设备配置
- App.py            设备启动类
```
### 后端目录结构
```
- constant    封装通用类和定义常量
    - RequestUtil               请求类封装
    - JsonUtil                  json库封装

- devApi      后端开发接口
    - homePage                  首页
    - bargainPagge              交易页面
    - financialManagementPage   理财页面
    - propertyPage              资产页面

- features    BDD(行为驱动开发) 暂未启用
- tests       测试用例(集合)
```

### GUI项目快速开始
```
# 打开一个终端(命令窗口)
appium --session-override

# 找到testcase文件
python -m unittest '文件夹.文件名'
```
### 注意事项
- appGui.config.EnvSwitch 切换 线上/测试环境
### 待办事项
- [ ] 日志收集
- [ ] 前端测试,执行未通过截图
- [ ] 测试报告
- [ ] PO对象对应页面脚本导航图片