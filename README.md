# Weather-Assistant
这是一个使用LangChain、DeepSeek和Weather API实现的天气智能体，能够查询指定城市的实时天气信息并提供出行建议。

在代码中我提供了两种构造方法：<br>
&#160;&#160;&#160;&#160;&#160;1.use_get_weather : 使用函数get_weather模拟外部工具，可以让DeepSeek自动调用以完成任务————“查找深圳的天⽓，然后⽤⼀句话告诉我出⻔要不要带伞”<br>

&#160;&#160;&#160;&#160;&#160;2.use_api : 使用Weather API获取实时天气数据，让DeepSeek调用以得到更优质准确的结果，适用于更广泛的场景<br>

使用的模型与API：DeepSeek-V3-0324 , Weather API<br>
# 运行方法：
  &#160;&#160;&#160;下载后先将两个文件夹中的main.py0中的密钥和大模型调用URL换成自己的，如果你要使用use_api版，还要将fun_get_weather.py中的URL换成你要调用API的URL（如果你使用的大模型和天气API和我一样，则只需要更改密钥）<br>
  &#160;&#160;&#160;完成以上步骤后，直接运行两个文件夹中的main.py即可

# 运行结果：

# 1.use_get_weather：<br>
<img width="630" height="173" alt="屏幕截图 2025-07-25 003908" src="https://github.com/user-attachments/assets/d60c2a85-19ae-4452-966a-1101f34dba72" />

# 2.use_api：<br>
<img width="991" height="737" alt="屏幕截图 2025-07-25 003953" src="https://github.com/user-attachments/assets/7738b367-9052-4bd4-aeb3-8d2ebde686a9" />
<br>
<br>
<br>


借助搜索部分：在编写use_get_weather的过程中，不记得prompt的标准格式，导致智能体陷入循环，问了ai后才修改正确
