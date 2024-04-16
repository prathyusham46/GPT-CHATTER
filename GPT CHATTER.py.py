import time
import pyttsx3
from pyowm import OWM

def get_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    return f"The current time is {current_time}."

def get_weather(city): 
    owm = OWM('a557346d87cba6ec43dce614637cf774')  
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temperature = weather.temperature('celsius')['temp']
    return f"The current temperature in {city} is {temperature}°C."

def main():
    engine = pyttsx3.init()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if "time" in user_input:
            response = get_time()
        elif "weather" in user_input:
            city = input("Which city's weather do you want to know? ")
            response = get_weather(city)
        else:
            response = "I'm not sure how to respond to that."

        print("ChatGPT:", response)
        engine.say(response)
        engine.runAndWait()

if __name__ == "__main__":
    main()

