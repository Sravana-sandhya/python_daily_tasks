# Q12 : Smart Home Devices (Multiple Inheritance) 
# A smart home device may have both WiFi connectivity and Voice control features. 
# Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that 
# inherits from both using multiple inheritance. 
class WiFiDevice:
    def wifi(self):
        print("WiFi Connected")
class VoiceAssistant:
    def voice(self):
        print("Voice Assistant Enabled")
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker Ready")
s = SmartSpeaker()
s.wifi()
s.voice()
s.display()