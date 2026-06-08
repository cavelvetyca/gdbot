import os
import random
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Missing TOKEN environment variable")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

THEMES = [
    "Factory", "Abandoned Factory", "Cyberpunk City", "Ancient Temple", "Volcano",
    "Space Station", "Haunted Castle", "Deep Sea Lab", "Crystal Cave", "Nuclear Bunker",
    "Backrooms", "Floating Islands", "Desert Ruins", "Arctic Base", "Jungle Temple",
    "Mechanical Core", "Abandoned City", "Sky Fortress", "Lava Cavern", "Neon Highway",
    "Toxic Sewer", "Clock Tower", "Alien Planet", "Digital World", "Glitch Dimension",
    "Stormy Ocean", "Underground Mine", "Moon Base", "Dream World", "Nightmare Realm",
    "Power Plant", "Military Base", "Cold War Facility", "Tank Battlefield", "Airfield",
    "Harbor", "Train Yard", "Destroyed City", "Laboratory", "Prison Complex",
    "Cyber Lab", "Ice Palace", "Fire Temple", "Shadow Realm", "Crystal Kingdom",
    "Radioactive Zone", "Robot Factory", "Ancient Library", "Sunken City", "Meteor Crash Site",
    "Data Center", "Portal Dimension", "Floating Castle", "Toxic Wasteland", "Laser Grid",
    "Neon Arcade", "Underground Bunker", "Forgotten Shrine", "Demon Fortress", "Skyline Chase",
    "Corrupted Forest", "Gravity Chamber", "Rusty Machine", "Starship Interior", "Asteroid Field",
    "Monster Cave", "Pixel World", "Retro Arcade", "Solar Temple", "Frozen Tundra",
    "Thunderstorm", "Chemical Plant", "Warzone", "Castle Siege", "City Rooftops",
    "Dreamscape", "Void Realm", "Ocean Monument", "Slime Factory", "Electric Tower",
    "Mirror World", "Crystal Mines", "Ancient Pyramid", "Rocket Launch Site", "Broken Simulation",
    "Giant Computer", "Dimension Rift", "Redstone Machine", "Beacon Tower", "Endless Corridor",
    "Mechanical Jungle", "Cyber Desert", "Space Elevator", "Abandoned Mall", "Flooded Subway",
    "Lunar Colony", "Sky Ruins", "Doomsday Shelter", "Magma Reactor", "Dark Cathedral"
]

COLORS = [
    "Red + Black", "Blue + Cyan", "Purple + Pink", "Green + Gray", "Gold + White",
    "Neon Rainbow", "Monochrome", "Orange + Brown", "Lime + Purple", "Yellow + Blue",
    "Crimson + Silver", "Teal + Black", "Magenta + Cyan", "Gray + Red", "Dark Blue + White",
    "White + Cyan", "Black + Neon Green", "Orange + Black", "Purple + Gold", "Pink + White",
    "Blue + Purple", "Red + Yellow", "Green + Black", "Cyan + Magenta", "Brown + Gold",
    "Dark Red + Gray", "Ice Blue + White", "Lava Orange + Red", "Toxic Green + Yellow", "Space Blue + Black",
    "Pastel Rainbow", "Deep Purple + Black", "Neon Pink + Black", "Mint + White", "Royal Blue + Gold",
    "Bronze + Brown", "Silver + Cyan", "Dark Green + Tan", "Blood Red + Black", "Electric Blue + Yellow",
    "White + Gold", "Charcoal + Orange", "Violet + Cyan", "Rust + Gray", "Sky Blue + White",
    "Black + Red Glow", "Cyber Green + Black", "Solar Yellow + Orange", "Aqua + Navy", "Hot Pink + Purple"
]

GAMEPLAY = [
    "Wave Heavy", "Ship Heavy", "Cube Timing", "Mixed Gameplay", "Fast-paced Flow",
    "Memory-based", "Spider Heavy", "UFO Spam", "Robot Jumps", "Dual Gameplay",
    "Mini Gameplay", "Speed Changes", "Portal Spam", "Tight Timings", "Slow Sync",
    "Fast Sync", "Straight Fly", "Wave Spam", "Click Sync", "Orb Timing",
    "Dash Orb Gameplay", "Gravity Portal Switching", "Mirror Portal Gameplay", "Asymmetrical Dual",
    "Symmetrical Dual", "Bossfight Gameplay", "Chokepoint Gameplay", "Short Burst Gameplay",
    "Long Endurance Gameplay", "Slope Gameplay", "Platformer Style", "Classic 1.9 Gameplay",
    "Modern Flow", "XL Level Gameplay", "Short Challenge", "Ship Corridors", "Wave Corridors",
    "Cube Maze", "Robot Timing", "Spider Timing", "UFO Timing", "Ball Timing",
    "Speedcore Gameplay", "Calm Sync", "Drop-based Gameplay", "Pre-drop Build-up", "Finale Spam",
    "Two-player Inspired", "Mini Wave", "Mini Ship", "Mixed Demon Gameplay"
]

DIFFICULTIES = [
    "Auto", "Easy", "Normal", "Hard", "Harder", "Insane",
    "Easy Demon", "Medium Demon", "Hard Demon", "Insane Demon", "Extreme Demon",
    "Beginner Demon", "Low Easy Demon", "High Easy Demon", "Low Medium Demon",
    "High Medium Demon", "Low Hard Demon", "High Hard Demon", "Low Insane Demon",
    "High Insane Demon", "Entry Extreme Demon", "Top 500 Extreme Demon", "Impossible Level",
    "Challenge Level", "Layout Difficulty", "Memory Demon", "Nine Circles Difficulty"
]

GIMMICKS = [
    "Rotating World", "Fake Paths", "Darkness", "Flashlight", "Camera Effects",
    "Moving Objects", "Gravity Chaos", "Dual Section", "Reverse Gameplay", "Boss Fight",
    "Color Pulse", "Invisible Blocks", "Speed Switches", "Portal Maze", "Mini Challenge",
    "No Jump Pads", "Only Orbs", "Only One Color", "No Glow", "Extreme Glow",
    "Screen Shake", "Zoom In/Out", "Low Visibility", "Sudden Gravity Flips", "Teleport Effects",
    "Fake Coins", "Hidden Route", "Chase Sequence", "Laser Dodging", "Falling Platforms",
    "Timed Doors", "Random-looking Sync", "Background Storytelling", "One Object Style",
    "No Decorations Until Drop", "Decoration Changes Every Section", "Boss Shoots Lasers",
    "Boss Follows Player", "Pixel Art Background", "Glitch Effects", "Broken Screen Effect",
    "Music-reactive Pulses", "Reverse Drop", "Portal Overload", "Memory Maze", "Click Pattern Puzzle",
    "Dual Desync", "Gravity Chamber", "Rotating Boss Arena", "Vehicle Transformation Spam",
    "No Ground", "Fake Ending", "Sudden Calm Section", "Final 10% Speed Burst"
]

BOSSES = [
    "No Boss", "Robot", "Dragon", "Tank", "Computer Virus", "Giant Eye",
    "Spider Machine", "Flying Core", "Demon Face", "Mechanical Serpent",
    "Laser Turret", "Cyber Dragon", "Shadow Beast", "Crystal Guardian", "Giant Cube",
    "Corrupted AI", "War Machine", "Ghost King", "Lava Monster", "Ice Golem",
    "Alien Mothership", "Glitch Worm", "Train Engine", "Battleship", "Helicopter",
    "Jet Fighter", "Cursed Portal", "Clockwork Giant", "Nuclear Reactor", "Floating Skull",
    "Demon Core", "Robot Spider", "Neon Samurai", "Giant Crab", "Security System",
    "Mutant Slime", "Electric Serpent", "Mechanical Heart", "Dark Wizard", "Stone Titan",
    "Beacon Guardian", "Redstone Machine", "Void Entity", "Mirror Clone", "Final Cube"
]

ENDINGS = [
    "Escape Sequence", "Explosion", "Boss Defeated", "World Collapse", "Portal Home",
    "Dream Ends", "Nuclear Launch", "Final Drop", "Glitch Shutdown", "Victory Burst",
    "Cave Collapse", "Rocket Launch", "Simulation Breaks", "Castle Falls", "City Lights Up",
    "Reactor Meltdown", "Ocean Drains", "Sky Opens", "Boss Escapes", "Secret Door Opens",
    "Player Gets Trapped", "Darkness Takes Over", "Light Returns", "Final Laser Blast",
    "Time Freezes", "World Resets", "Portal Explosion", "Robot Powers Down",
    "Monster Disappears", "Screen Cracks", "Dimension Seals", "Beacon Activates",
    "Airship Crashes", "Train Derails", "Storm Clears", "The Level Loops",
    "Fake Ending", "Sudden Jumpscare", "Peaceful Outro", "Final Coin Reveal"
]

ATMOSPHERES = [
    "Epic", "Creepy", "Chaotic", "Peaceful", "Mysterious", "Intense",
    "Dreamlike", "Apocalyptic", "Lonely", "Heroic", "Dark", "Energetic",
    "Sad", "Retro", "Futuristic", "Mechanical", "Magical", "Cold",
    "Hot", "Toxic", "Glitchy", "Calm", "Stressful", "Beautiful",
    "Aggressive", "Industrial", "Cosmic", "Haunted", "Military", "Surreal"
]

DECORATION = [
    "Modern", "Glow", "Core Style", "Effect Style", "Art Level", "Minimalist",
    "1.9 Style", "2.0 Style", "2.1 Style", "2.2 Style", "Pixel Art",
    "Block Design", "Neon Design", "Dark Design", "Clean Design", "Overdecorated",
    "Retro Design", "Tech Design", "Temple Design", "Nature Design", "Industrial Design",
    "Space Design", "Hell Design", "Ice Design", "Fire Design", "Cyber Design",
    "Mechanical Design", "Crystal Design", "Military Design", "Cartoon Design"
]

MUSIC = [
    "Dubstep", "Techno", "Drum and Bass", "Metal", "Synthwave", "Ambient",
    "Phonk", "Orchestral", "Piano", "Chiptune", "Hardstyle", "EDM",
    "Rock", "Glitch Hop", "Future Bass", "House", "Trance", "Breakcore",
    "Lo-fi", "Dark Ambient", "Bossfight Music", "Fast Electronic", "Calm Electronic",
    "Retro Arcade", "Cinematic", "Industrial", "Experimental", "Melodic Dubstep"
]

CHALLENGES = [
    "Use only two colors", "No glow allowed", "Only cube gameplay", "Only wave gameplay",
    "Only ship gameplay", "No move triggers", "No camera effects", "Make it sync perfectly",
    "Use one main block design", "Make every section a different color", "Add one secret coin route",
    "Make it feel like a bossfight", "Build it in 1 hour", "Make the ending harder than the drop",
    "Use no custom backgrounds", "Make a fake ending", "Use only black and white",
    "Make it look like an old GD level", "Make it look like a modern featured level",
    "Add a chase sequence", "Add a memory part", "Add a calm intro", "Add a sudden intense drop",
    "Use only circular decorations", "Use only square decorations", "Make a level around one object",
    "Make the gameplay readable", "Make the theme change halfway", "Use a portal as the main gimmick",
    "Make it possible but annoying"
]

def pick(items):
    return random.choice(items)

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"GDBot logged in as {bot.user}")
    print(f"Synced {len(synced)} global command(s)")

@bot.tree.command(name="idea", description="Generate a Geometry Dash level idea")
async def idea(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"**GDBot Level Idea**\n\n"
        f"**Theme:** {pick(THEMES)}\n"
        f"**Colors:** {pick(COLORS)}\n"
        f"**Atmosphere:** {pick(ATMOSPHERES)}\n"
        f"**Decoration:** {pick(DECORATION)}\n"
        f"**Gameplay:** {pick(GAMEPLAY)}\n"
        f"**Difficulty:** {pick(DIFFICULTIES)}\n"
        f"**Gimmick:** {pick(GIMMICKS)}\n"
        f"**Boss:** {pick(BOSSES)}\n"
        f"**Ending:** {pick(ENDINGS)}\n"
        f"**Music Style:** {pick(MUSIC)}\n"
        f"**Challenge:** {pick(CHALLENGES)}"
    )

@bot.tree.command(name="challenge", description="Generate a Geometry Dash build challenge")
async def challenge(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"**GDBot Challenge**\n\n"
        f"Build a **{pick(DIFFICULTIES)}** level.\n"
        f"Theme: **{pick(THEMES)}**\n"
        f"Gameplay: **{pick(GAMEPLAY)}**\n"
        f"Colors: **{pick(COLORS)}**\n"
        f"Rule: **{pick(CHALLENGES)}**"
    )

@bot.tree.command(name="theme", description="Generate a Geometry Dash theme")
async def theme(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"**Theme:** {pick(THEMES)}\n"
        f"**Atmosphere:** {pick(ATMOSPHERES)}\n"
        f"**Colors:** {pick(COLORS)}"
    )

@bot.tree.command(name="boss", description="Generate a Geometry Dash boss idea")
async def boss(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"**Boss Idea:** {pick(BOSSES)}\n"
        f"**Theme:** {pick(THEMES)}\n"
        f"**Attack Style:** {pick(GIMMICKS)}"
    )

@bot.tree.command(name="help", description="Show GDBot commands")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**GDBot Commands**\n\n"
        "/idea - Generate a full GD level idea\n"
        "/challenge - Generate a build challenge\n"
        "/theme - Generate a theme\n"
        "/boss - Generate a boss idea\n"
        "/help - Show commands"
    )

bot.run(TOKEN)
