#!/usr/bin/env python3
import pyttsx3
def main():
    engine = pyttsx3.init()
    # engine.runAndWait()
    poem = """Twinkle, twinkle, little star,
    How I wonder what you are!
    Up above the world so high,
    Like a diamond in the sky."""
    print(poem)
    engine.say(poem)
    engine.runAndWait()


if __name__ == "__main__":
    main()