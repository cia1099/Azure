Create a Azure Function
---
You can refer [Quickstart: Create a Python function in Azure from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators#create-venv)
```shell
func init basicAzureFunction --worker-runtime python
cd basicAzureFunction
func new --name httpexample --template "HTTP trigger" --authlevel "anonymous"
```
执行完上面的指令会生成[basicAzureFunction/function_app.py](function_app.py)等必要档案。\
要执行本地环境，需要[Run Azurite](https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=npm#run-azurite):
```shell
# npm install -g azurite
# open a new terminal, you don't need to exchange rosetta here
azurite --silent
```
* #### How to emulate x86 in Arm use Rosetta
[x86 emulation on ARM64](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python#x86-emulation-on-arm64)
切换到Rosetta模式，安装所有相依软件，Rosetta模式会自动安装在`/usr/local`里面，不会和系统冲突。
https://stackoverflow.com/questions/64882584/how-to-run-the-homebrew-installer-under-rosetta-2-on-m1-macbook
设定`~/.zshrc`让Mac区分x86和arm环境:
```shell
# <<< Rosetta mode; default PS1="%n@%m %1~ %#"
if [ "i386" = $(arch) ]; then
    export PS1="%B%F{green}%n@%m%f%b:%F{4}%1~%f%# "
    eval "$(/usr/local/bin/brew shellenv)"
    alias python3="/usr/local/bin/python3"
else
    export PS1="%B%F{195}%n@%m%f%b:%F{103}%1~%f%# "
    eval "$(/opt/homebrew/bin/brew shellenv)"
    unalias python3
fi
```
切换到**rosetta**的终端执行：
```shell
cd basicAzureFunction
func start
# 此时rosetta的终端会被http://localhost:7071/api/httpexample占据
# 在随便一个终端执行，就可以成功了
curl "http://localhost:7071/api/httpexample?name=shit&pp=jj"
```

#### Deploy
安装[az_cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
```shell
# 用safari登入会失败，将网址贴到edge就能登入成功
az login
# 查看登录资讯
az account list
# Set a subscription to be the current active subscription.
az account set -n 'basic subscription'
# *** Deploy ***
cd basicAzureFunction
func azure functionapp publish <FunctionAppName>
#func azure functionapp publish functionGPT
```
* 其中\<FunctionAppName>是你在Azure账号里创建的Function名称。

[更多az-cli操作](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-list-locations)