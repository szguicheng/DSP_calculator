# 规范的项目目录结构
```
project_name/
├── LICENSE                # 许可证文件
├── README.md              # 项目简介和使用说明
├── .gitignore             # Git忽略规则
├── requirements.txt       # 依赖库列表
├── setup.py               # 安装和打包脚本（可选）
├── docs/                  # 文档目录
│   └── index.md           # 文档首页
├── tests/                 # 测试代码
│   └── test_main.py       # 测试主模块
├── src/                   # 主代码目录
│   ├── main.py            # 程序入口
│   ├── calculator.py      # 核心逻辑
│   ├── models/            # 数据模型
│   │   └── product.py     # 产品数据类
│   ├── ui/                # UI模块
│   │   └── main_window.py # 主窗口代码
└── resources/             # 静态资源
    ├── icons/             # 图标
    └── styles/            # 样式文件
```
# 文件/目录说明：

- LICENSE: 包含MIT许可证的内容，告知用户许可证信息。
- README.md: 使用Markdown格式撰写的文件，提供项目的功能概述、安装步骤、使用方法等。
- requirements.txt: 列出依赖库，例如PyQt5等，可用pip install -r requirements.txt安装。
- setup.py: 可选，用于将项目打包为可安装模块。
- docs/: 存放开发文档和用户手册，推荐使用工具如Sphinx或Markdown撰写。
- tests/: 包含单元测试，使用工具如pytest进行测试。
- src/: 主代码目录，包含逻辑、UI、数据模型等模块，分层设计便于扩展。
- resources/: 存放静态资源，例如图标、样式等，统一管理以便替换。
- 使用 Sphinx 风格的注释：使用 :param、:type、:return、:rtype 和 :raises 等标签来描述参数、返回值和异常。
- 使用 .. attention:: 提示语句：在文档字符串中使用 .. attention:: 提示语句来添加注意事项。

# 项目命名规范

- 项目名称：简洁易懂，建议采用全小写，下划线分隔，例如``product_calculator``。
- 模块名称：与项目类似，使用小写字母和下划线，例如``calculator.py``。
- 类名：使用“帕斯卡命名法”，每个单词首字母大写，例如``ProductManager``。
- 函数和变量名：采用“蛇形命名法”，单词间用下划线分隔，例如``calculate_total_price``。
- 测试函数命名：以``test_``开头，描述测试内容，例如``test_addition_functionality``。

# 维护及升级的相关事宜

1.	版本控制
•	使用Git进行版本管理，推荐在GitHub创建远程仓库。
•	遵循分支模型：
•	main分支：发布稳定版本。
•	dev分支：用于开发和测试。
•	feature分支（如feature/add-ui）：实现新功能。
2.	代码规范
•	遵循PEP 8（Python编码规范），可用工具flake8或black检查代码格式。
•	在关键函数和模块添加文档字符串（``docstring``），例如：
```python
def calculate_total(price, quantity):
    """
    for calculating total price

    Args:
        price (float): 单价
        quantity (int): 数量

    Returns:
        float: 总价
    """
    return price * quantity
```

3.	自动化测试
•	编写单元测试，覆盖主要功能，确保代码的稳定性和正确性。
•	使用pytest或unittest进行测试。
•	在GitHub上配置CI/CD工具（如GitHub Actions）以自动运行测试。
4.	文档维护
•	使用工具如Sphinx或Jupyter Notebook编写详细的开发文档和用户指南。
•	定期更新文档以反映新功能。
5.	代码扩展性
•	避免硬编码，尽量通过配置文件管理参数（如JSON或YAML格式）。
•	使用设计模式（如工厂模式、单例模式）提升代码复用性。
6.	多平台兼容性
•	在Windows和Mac上测试程序，确保界面和功能一致。
•	使用pyinstaller生成可执行文件，支持跨平台部署：``pyinstaller --onefile --windowed src/main.py``
在开发阶段可以用 ``pip freeze > requirements.txt`` 自动生成依赖

# 未来维护和升级

- 规划版本：遵循语义化版本控制，如1.0.0表示初始稳定版本。
- 定期检查依赖：使用``pip list --outdated``检查依赖库的更新，并在升级前测试兼容- 用户反馈：在GitHub上利用Issues收集用户反馈，优先解决用户报告的问题。  
      
- MAJOR（重大更改）：不兼容的更新。
- MINOR（新增功能）：向后兼容的更新。
- PATCH（修复问题）：向后兼容的修补。

