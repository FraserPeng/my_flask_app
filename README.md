# my_flask_app

###  虚拟环境创建

> 安装 虚拟环境

```
pip install virtualenv

pip install virtualenvwrapper  # 这是对virtualenv的封装版本，一定要在virtualenv后安装 
```
> 新建项目--my_flask_app,安装虚拟环境
```
cd my_flask_app
virtualenv envn

```
> 启动虚拟环境

> 注意：在VS code Powershell 中可能启动不了虚拟环境，需要把切换成PowerShell Integrated Console环境才能启动。
切换方式，打开activate.ps1文件，自动切换成功
```
# 进入虚拟环境文件
cd envname
# 进入相关的启动文件夹
cd Scripts

activate  # 启动虚拟环境
deactivate # 退出虚拟环境
```
