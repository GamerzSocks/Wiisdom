class Wiisdom:
    def __init__(self):
        self.knowledge_base = {
            "What is the Wii?": "The Wii is a home video game console released by Nintendo.",
            "When was the Wii released?": "The Wii was released on November 19, 2006.",
            "What are the main features of the Wii?": "The Wii introduced motion-sensing controls through the Wii Remote.",
            "What are some popular games for the Wii?": "Some popular games for the Wii include Mario Kart Wii, Wii Sports, and The Legend of Zelda: Twilight Princess.",
            "How many units of the Wii were sold?": "Over 101 million units of the Wii were sold worldwide, making it one of the best-selling game consoles of all time.",
            "Is the Wii still in production?": "No, Nintendo discontinued the Wii in 2013.",
            "What accessories are available for the Wii?": "The Wii had various accessories, including the Nunchuk, Classic Controller, and Wii Balance Board.",
            "What is the Virtual Console on the Wii?": "The Virtual Console was a service that allowed users to purchase and download games from older Nintendo consoles.",
            "What is the Wii U?": "The Wii U is the successor to the Wii, featuring a tablet-like GamePad controller.",
            "Can I play GameCube games on the Wii?": "Yes, early versions of the Wii were compatible with GameCube games.",
            "How do I connect the Wii to a TV?": "The Wii can be connected to a TV using AV cables or an HDMI adapter (for Wii U models).",
            "What are some exclusive titles for the Wii?": "Some exclusive titles for the Wii include Super Mario Galaxy, Metroid Prime 3: Corruption, and Xenoblade Chronicles.",
            "What is Wii MotionPlus?": "Wii MotionPlus is an accessory for the Wii Remote that provides more precise motion-sensing capabilities.",
            "What is the Wii Shop Channel?": "The Wii Shop Channel was an online shop where users could download games, channels, and applications for their Wii console.",
            "What is the Mii Channel on the Wii?": "The Mii Channel allows users to create and customize avatars called Miis, which can be used in various games and applications.",
            "What is Wii Fit?": "Wii Fit is a fitness game that uses the Wii Balance Board to provide exercise routines and track fitness progress.",
            "What is the maximum resolution supported by the Wii?": "The Wii supports a maximum resolution of 480p.",
            "What are some popular third-party games on the Wii?": "Some popular third-party games on the Wii include Just Dance, Rayman Raving Rabbids, and Call of Duty: Modern Warfare.",
            "What is the Wii Menu?": "The Wii Menu is the main user interface of the Wii, where users can access channels, settings, and games.",
            "What is the Message Board on the Wii?": "The Message Board allows users to send and receive messages, as well as receive news and updates from Nintendo.",
            "What is the Nintendo Wi-Fi Connection?": "The Nintendo Wi-Fi Connection was an online gaming service for the Wii that allowed players to compete or cooperate with each other over the internet.",
            "Can I use GameCube controllers with the Wii U?": "Yes, the Wii U has ports for GameCube controllers and supports them for certain games.",
            "What is the Wii Speak?": "Wii Speak was an accessory for the Wii that allowed voice chat in supported games.",
            "What is the Wii Zapper?": "The Wii Zapper is an accessory that allows players to use the Wii Remote and Nunchuk as a gun-like controller in compatible games.",
            "What is the Nintendo Channel?": "The Nintendo Channel was a service on the Wii that provided information about games, including trailers, demos, and user reviews.",
            "Can I play DVDs on the Wii?": "No, the Wii does not have built-in DVD playback capabilities.",
            "What is the Wii Remote Jacket?": "The Wii Remote Jacket was a protective cover provided by Nintendo to prevent damage to the Wii Remote during intense gameplay.",
            "What is WiiConnect24?": "WiiConnect24 was a feature that allowed the Wii to receive messages, game updates, and other data while in standby mode.",
            "What is the Wii System Menu?": "The Wii System Menu is the user interface that appears when you start the Wii console. It allows access to channels, settings, and other features.",
            "What is Wii Party?": "Wii Party is a party game for the Wii that offers a variety of mini-games and activities for multiplayer fun.",
            "What is the Wii LAN Adapter?": "The Wii LAN Adapter is an accessory that allows you to connect the Wii to the internet through a wired connection.",
            "What is the Wii Wheel?": "The Wii Wheel is an accessory designed for use with racing games on the Wii, providing a steering wheel-like interface for the Wii Remote.",
            "What is Wii Sports Resort?": "Wii Sports Resort is a sequel to Wii Sports, featuring a variety of new sports and activities designed to showcase the Wii MotionPlus accessory.",
            "What is the Wii Fit Plus?": "Wii Fit Plus is an enhanced version of Wii Fit, offering additional exercises and activities for fitness and balance training.",
            "What is the Wii Speak Channel?": "The Wii Speak Channel was a feature that allowed users to chat with friends using the Wii Speak accessory.",
            "What is Wii Music?": "Wii Music is a music video game that allows players to simulate playing various musical instruments using the Wii Remote and Nunchuk.",
            "What is Wii Homebrew?": "Wii Homebrew refers to unofficial software and applications developed by the homebrew community for the Wii console. These applications are not officially endorsed or supported by Nintendo.",
            "How can I install Wii Homebrew?": "To install Wii Homebrew, you'll need to use an exploit to run custom code on your Wii. There are various methods and tools available online, but it's important to follow instructions carefully and ensure that you're using trusted sources.",
            "What are some popular Wii Homebrew applications?": "Some popular Wii Homebrew applications include the Homebrew Channel, which serves as a platform for running other homebrew software, and emulators for playing games from older consoles.",
            "Can using Wii Homebrew void my warranty?": "Yes, using Wii Homebrew may void your warranty with Nintendo, as it involves modifying the console's software which is not supported by the manufacturer.",
            "Is using Wii Homebrew legal?": "Using Wii Homebrew itself is not illegal, but it's important to be aware that certain homebrew applications or activities may infringe on copyrights or violate terms of service, so it's crucial to use homebrew responsibly and legally.",
            "Can Wii Homebrew harm my Wii console?": "Improper use of Wii Homebrew can potentially harm your console, as it involves running custom code that hasn't been officially tested or approved by Nintendo. It's important to exercise caution and follow instructions carefully when using Wii Homebrew."
        }

    def get_response(self, question):
        return self.knowledge_base.get(question, "I'm sorry, I don't have information on that.")

# Create an instance of the WiiAI
wii_ai = Wiisdom()

# Interactive loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = wii_ai.get_response(user_input)
    print("Wii AI:", response)
