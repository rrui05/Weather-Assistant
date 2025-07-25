import requests
import os


def get_weather(city: str) -> str:
    api_key = os.getenv("WEATHERAPI_KEY")
    api_url = os.getenv("WEATHERAPI_BASE")
    if not api_key:
        return "错误:未配置WeatherAPI密钥"

    url = f"{api_url}?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()

        # 提取需要的天气信息（根据API返回结构解析）
        current = data.get("current", {})
        location = data.get("location", {})

        return {
            "城市": location.get("name", ""),
            "地区": location.get("region", ""),
            "当前温度(°C)": current.get("temp_c", ""),
            "体感温度(°C)": current.get("feelslike_c", ""),
            "天气状况": current.get("condition", {}).get("text", ""),
            "降雨概率(%)": current.get("precip_mm", 0) * 10,  # 转换为近似概率
            "湿度(%)": current.get("humidity", ""),
            "风速(km/h)": current.get("wind_kph", ""),
            "日出时间": current.get("sunrise", ""),
            "日落时间": current.get("sunset", ""),
            "月升时间": current.get("moonrise", ""),
            "月落时间": current.get("moonset", ""),
            "紫外线指数": current.get("uv", ""),
            "能见度(km)": current.get("vis_km", "")
        }
    except Exception as e:
        return f"获取天气失败：{str(e)}"