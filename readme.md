# 空闲机器监听脚本
从学院白嫖的机子不再独享，需要一个脚本监听机器是否空闲。

---

## 总结

函数作为函数参数时 `**` 和 `*` 包运算符不生效。（python3.8）:

```
# Traceback (most recent call last):
#     TypeError: default_when_idle() takes 0 positional arguments but 6 were given
```

vscode settings.json：
```json
"python.autoComplete.extraPaths":[] 控制pylint代码提示路径
"terminal.integrated.env.linux": { //可控制程序运行时环境变量
        "PYTHONPATH":"${workspaceFolder}/waitting_machine"
    },
```

vscode launch.json：
```json
{
    "name": "Python: 当前文件",
    "type": "python",
    "cwd": "${workspaceFolder}",
    "env": { "PYTHONPATH": "${workspaceFolder}"},//控制debug时环境变量
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal"
},
```