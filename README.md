# 🌤️ Weather CLI v1.0.0

## Info

Author: Sebastian-GOAT
Current version: 1.0.0

## ⬇️ Download

Make sure you have installed Python v3.8+ and git. Then run the following scripts:

```bash
mkdir weather-cli
cd weather-cli
pip install requests python-dotenv
git clone https://github.com/Sebastian-GOAT/weather-cli.git
```

Then add the project path (e.g. C:/Users/USERNAME/Desktop/weather-cli) to your system PATH.

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