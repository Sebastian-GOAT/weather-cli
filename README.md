# 🌤️ Weather CLI v1.0.0

## Info

Author: Sebastian-GOAT
Current version: 1.0.0

## ⬇️ Download

```bash
Not aviable for download yet
```

## ⚙️ Requirements

- Python v3.8+
- .env file with OpenWeather API key:
```ini
WEATHER_API_KEY=your_api_key
```

## 🪧 Usage

Available commands:

```bash
weather -h
weather --help       # Shows the help commands

weather -v
weather --version    # Shows the installed version

weather <Location>   # Gets the weather
```

## 🤖 Example

```bash
weather Prague
```

Expected output:

```text
📍 Prague

☁️ Clouds
🌡️ 19°C, feels like 18°C
💧 67%
💨 6.17m/s
```