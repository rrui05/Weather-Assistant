# Weather-Assistant
- 这是一个使用LangChain、DeepSeek和Weather API实现的天气智能体，能够查询指定城市的实时天气信息并提供出行建议。

- 在代码中我提供了两种构造方法：<br>
&#160;&#160;&#160;&#160;&#160;1.use_get_weather : 使用函数get_weather模拟外部工具，可以让DeepSeek自动调用以完成任务————“查找深圳的天⽓，然后⽤⼀句话告诉我出⻔要不要带伞”<br>

&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;2.use_api : 使用Weather API获取实时天气数据，让DeepSeek调用以得到更优质准确的结果，适用于更广泛的场景<br>
- 使用的模型与天气API：DeepSeek-V3-0324 , Weather API<br>
<br>
- 对于这两种方法，我构造了相同的UI界面<br>
<img width="869" height="834" alt="屏幕截图 2025-07-25 134112" src="https://github.com/user-attachments/assets/4eced234-dc86-4380-a309-e5ff84ce3a54" />

# 结果展示
1. use_get_weather <br>
<img width="865" height="833" alt="屏幕截图 2025-07-25 133908" src="https://github.com/user-attachments/assets/3524b894-5fca-4666-869a-64320b0ebb85" /><br>
2. use_api <br>
<img width="861" height="755" alt="屏幕截图 2025-07-25 134019" src="https://github.com/user-attachments/assets/9fdf4570-a342-4609-9160-c3edab5386cc" />
<img width="868" height="617" alt="屏幕截图 2025-07-25 134041" src="https://github.com/user-attachments/assets/74d6a41e-b0cb-4355-9e6b-59feedba805a" />



# 运行方法：
- 下载后先在Mylangchain.py配置LLM的URL和密钥，使用use_api版时，还要配置天气API的URL和密钥<br>
- 完成以上步骤后，直接运行app.py即可

<br>
<br>
<br>


# 借助搜索部分：
1. 在编写use_get_weather的过程中，忘记prompt的标准格式，导致智能体陷入循环，问了ai后才修改正确<br>
2. 由于本人是首次将代码上传至github，上传、更新、代码仓库的方法都是网上搜的
3. UI界面主体框架由豆包完成，本人在其基础上进行了一些细节调整
