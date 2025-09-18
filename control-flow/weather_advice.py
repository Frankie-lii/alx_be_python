#!/usr/bin/env python3

# weather_advice.py
# A simple program to provide clothing recommendations based on weather conditions.

# Prompt the user for input
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Decision making using if/elif/else
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
