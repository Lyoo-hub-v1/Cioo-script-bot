import os
import discord
from discord.ext import commands

TOKEN_SCRIPT = os.getenv("TOKEN_SCRIPT")
SCRIPT_CHANNEL_ID = 1575068304542933013

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def S(name, url):
    return (name, f'loadstring(game:HttpGet("{url}"))()')

SPEED_X = "https://raw.githubusercontent.com/AhmadV99/Speed-Hub-X/main/Speed%20Hub%20X.lua"
CHILLI = "https://raw.githubusercontent.com/tienkhanh1/spicy/main/Chilli.lua"
LUMIN = "https://luminon.top/loader.lua"
KENNIEL = "https://raw.githubusercontent.com/Kenniel123/BrainRot-Tools/refs/heads/main/BrainRotTools"
LIME = "https://welikelimes.vercel.app/scripts/sab.lua"

SCRIPTS = {
    "Steal An Egg": [S("Speed Hub X", SPEED_X), S("Miranda Hub", "https://raw.githubusercontent.com/MirandaHub/MirandaHub/main/MirandaHub.lua"), S("Lumin Hub", LUMIN), S("Kenniel Hub", KENNIEL), S("Chilli Hub", CHILLI), S("Lime Hub", LIME), S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua"), S("Neox Hub", "https://raw.githubusercontent.com/hassanxzayn-lua/NEOXHUBMAIN/refs/heads/main/StealABrainrot"), S("Overflow Hub", "https://raw.githubusercontent.com/OverflowBGSI/Overflow/refs/heads/main/loader.txt"), S("Trax Hub", "https://raw.githubusercontent.com/gumanba/Scripts/refs/heads/main/StealaBrainrotMOD"), S("Redz Hub", "https://raw.githubusercontent.com/RedzHub/RedzHub/main/RedzHub.lua"), S("Sena Hub", "https://raw.githubusercontent.com/SenaHub/SenaHub/main/SenaHub.lua"), S("Nat Hub", "https://raw.githubusercontent.com/NatHub/NatHub/main/NatHub.lua"), S("Zenith Hub", "https://raw.githubusercontent.com/ZenithHub/ZenithHub/main/ZenithHub.lua"), S("Blue Hub", "https://raw.githubusercontent.com/BlueHub/BlueHub/main/BlueHub.lua"), S("Forge Hub", "https://raw.githubusercontent.com/ForgeHub/ForgeHub/main/ForgeHub.lua"), S("Rails Hub", "https://raw.githubusercontent.com/RailsHub/RailsHub/main/RailsHub.lua"), S("TSB Hub", "https://raw.githubusercontent.com/TSBHub/TSBHub/main/TSBHub.lua"), S("MM2 Hub", "https://raw.githubusercontent.com/MM2Hub/MM2Hub/main/MM2Hub.lua"), S("Strongest Hub", "https://raw.githubusercontent.com/StrongestHub/StrongestHub/main/StrongestHub.lua")],
    "Throw Food For Animals": [S("Speed Hub X", SPEED_X), S("Lumin Hub", LUMIN), S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua")],
    "Hyper Realistic Ragdoll": [S("Lumin Hub", LUMIN), S("Speed Hub X", SPEED_X)],
    "Dandy's World": [S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua"), S("Lumin Hub", LUMIN)],
    "Anime Crusaders X": [S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua"), S("Lumin Hub", LUMIN)],
    "Fish It!": [S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua"), S("Speed Hub X", SPEED_X)],
    "Plants vs Brainrots": [S("Speed Hub X", SPEED_X), S("Space Hub", "https://raw.githubusercontent.com/SpaceHub/SpaceHub/main/SpaceHub.lua"), S("Lumin Hub", LUMIN), S("Chilli Hub", CHILLI)],
    "Grow a Garden 2": [S("Speed Hub X", SPEED_X), S("Lumin Hub", LUMIN), S("Than Hub", "https://raw.githubusercontent.com/thantzy/thanhub/refs/heads/main/thanv1")],
    "Steal a Brainrot": [S("Kenniel Hub", KENNIEL), S("Lime Hub", LIME), S("Chilli Hub", CHILLI), S("Speed Hub X", SPEED_X), S("Lumin Hub", LUMIN), S("Redz Hub", "https://raw.githubusercontent.com/RedzHub/RedzHub/main/RedzHub.lua"), S("Sena Hub", "https://raw.githubusercontent.com/SenaHub/SenaHub/main/SenaHub.lua"), S("Nat Hub", "https://raw.githubusercontent.com/NatHub/NatHub/main/NatHub.lua"), S("Zenith Hub", "https://raw.githubusercontent.com/ZenithHub/ZenithHub/main/ZenithHub.lua"), S("Blue Hub", "https://raw.githubusercontent.com/BlueHub/BlueHub/main/BlueHub.lua"), S("Forge Hub", "https://raw.githubusercontent.com/ForgeHub/ForgeHub/main/ForgeHub.lua"), S("Rails Hub", "https://raw.githubusercontent.com/RailsHub/RailsHub/main/RailsHub.lua"), S("TSB Hub", "https://raw.githubusercontent.com/TSBHub/TSBHub/main/TSBHub.lua"), S("MM2 Hub", "https://raw.githubusercontent.com/MM2Hub/MM2Hub/main/MM2Hub.lua"), S("Legacy Hub", "https://raw.githubusercontent.com/LegacyHub/LegacyHub/main/LegacyHub.lua"), S("Plants Hub", "https://raw.githubusercontent.com/PlantsHub/PlantsHub/main/PlantsHub.lua"), S("Pet Hub", "https://raw.githubusercontent.com/PetHub/PetHub/main/PetHub.lua"), S("Blade Hub", "https://raw.githubusercontent.com/BladeHub/BladeHub/main/BladeHub.lua"), S("Doors Hub", "https://raw.githubusercontent.com/DoorsHub/DoorsHub/main/DoorsHub.lua"), S("Strongest Hub", "https://raw.githubusercontent.com/StrongestHub/StrongestHub/main/StrongestHub.lua")],
    "Blox Fruits": [S("Redz Hub", "https://raw.githubusercontent.com/RedzHub/RedzHub/main/RedzHub.lua"), S("Zenith Hub", "https://raw.githubusercontent.com/ZenithHub/ZenithHub/main/ZenithHub.lua"), S("Speed Hub X", SPEED_X)],
    "Grow A Garden": [S("Speed Hub X", SPEED_X), S("Nat Hub", "https://raw.githubusercontent.com/NatHub/NatHub/main/NatHub.lua")],
    "99 Night": [S("Speed Hub X", SPEED_X)],
    "Blue Lock": [S("Blue Hub", "https://raw.githubusercontent.com/BlueHub/BlueHub/main/BlueHub.lua")],
    "The Forge": [S("Forge Hub", "https://raw.githubusercontent.com/ForgeHub/ForgeHub/main/ForgeHub.lua")],
    "Dead Rails": [S("Rails Hub", "https://raw.githubusercontent.com/RailsHub/RailsHub/main/RailsHub.lua")],
    "TSB": [S("TSB Hub", "https://raw.githubusercontent.com/TSBHub/TSBHub/main/TSBHub.lua")],
    "MM2": [S("MM2 Hub", "https://raw.githubusercontent.com/MM2Hub/MM2Hub/main/MM2Hub.lua")],
    "King Legacy": [S("Legacy Hub", "https://raw.githubusercontent.com/LegacyHub/LegacyHub/main/LegacyHub.lua")],
    "Brookhaven": [S("Brookhaven Hub", "https://raw.githubusercontent.com/BrookhavenHub/BrookhavenHub/main/BrookhavenHub.lua")],
    "Adopt Me": [S("Adopt Hub", "https://raw.githubusercontent.com/AdoptHub/AdoptHub/main/AdoptHub.lua")],
    "Doors": [S("Doors Hub", "https://raw.githubusercontent.com/DoorsHub/DoorsHub/main/DoorsHub.lua")],
    "Blade Ball": [S("Blade Hub", "https://raw.githubusercontent.com/BladeHub/BladeHub/main/BladeHub.lua")],
    "Bloxburg": [S("Bloxburg Hub", "https://raw.githubusercontent.com/BloxburgHub/BloxburgHub/main/BloxburgHub.lua")],
    "Bedwars": [S("Bedwars Hub", "https://raw.githubusercontent.com/BedwarsHub/BedwarsHub/main/BedwarsHub.lua")],
    "Arsenal": [S("Arsenal Hub", "https://raw.githubusercontent.com/ArsenalHub/ArsenalHub/main/ArsenalHub.lua")],
    "Tower of Hell": [S("TOH Hub", "https://raw.githubusercontent.com/TOHHub/TOHHub/main/TOHHub.lua")],
    "Anime Vanguards": [S("Vanguards Hub", "https://raw.githubusercontent.com/VanguardsHub/VanguardsHub/main/VanguardsHub.lua")],
    "Anime Defenders": [S("Defenders Hub", "https://raw.githubusercontent.com/DefendersHub/DefendersHub/main/DefendersHub.lua")],
    "Toilet Tower Defense": [S("TTD Hub", "https://raw.githubusercontent.com/TTDHub/TTDHub/main/TTDHub.lua")],
    "Fisch": [S("Fisch Hub", "https://raw.githubusercontent.com/FischHub/FischHub/main/FischHub.lua")],
    "Rivals": [S("Rivals Hub", "https://raw.githubusercontent.com/RivalsHub/RivalsHub/main/RivalsHub.lua")],
    "Jailbreak": [S("Jailbreak Hub", "https://raw.githubusercontent.com/JailbreakHub/JailbreakHub/main/JailbreakHub.lua")],
    "Bee Swarm": [S("Bee Hub", "https://raw.githubusercontent.com/BeeHub/BeeHub/main/BeeHub.lua")],
    "Slap Battles": [S("Slap Hub", "https://raw.githubusercontent.com/SlapHub/SlapHub/main/SlapHub.lua")],
    "Build A Boat": [S("Boat Hub", "https://raw.githubusercontent.com/BoatHub/BoatHub/main/BoatHub.lua")],
    "Piggy": [S("Piggy Hub", "https://raw.githubusercontent.com/PiggyHub/PiggyHub/main/PiggyHub.lua")],
    "Evade": [S("Evade Hub", "https://raw.githubusercontent.com/EvadeHub/EvadeHub/main/EvadeHub.lua")],
    "War Tycoon": [S("War Hub", "https://raw.githubusercontent.com/WarHub/WarHub/main/WarHub.lua")],
    "Da Hood": [S("Hood Hub", "https://raw.githubusercontent.com/HoodHub/HoodHub/main/HoodHub.lua")],
    "Shindo Life": [S("Shindo Hub", "https://raw.githubusercontent.com/ShindoHub/ShindoHub/main/ShindoHub.lua")],
    "Your Bizarre Adventure": [S("YBA Hub", "https://raw.githubusercontent.com/YBAHub/YBAHub/main/YBAHub.lua")],
    "A Universal Time": [S("AUT Hub", "https://raw.githubusercontent.com/AUTHub/AUTHub/main/AUTHub.lua")],
    "Anime Champions": [S("Champions Hub", "https://raw.githubusercontent.com/ChampionsHub/ChampionsHub/main/ChampionsHub.lua")],
    "Muscle Legends": [S("Muscle Hub", "https://raw.githubusercontent.com/MuscleHub/MuscleHub/main/MuscleHub.lua")],
    "Ro Ghoul": [S("Ghoul Hub", "https://raw.githubusercontent.com/GhoulHub/GhoulHub/main/GhoulHub.lua")],
    "Project Slayers": [S("Slayers Hub", "https://raw.githubusercontent.com/SlayersHub/SlayersHub/main/SlayersHub.lua")],
    "Demonfall": [S("Demonfall Hub", "https://raw.githubusercontent.com/DemonfallHub/DemonfallHub/main/DemonfallHub.lua")],
    "Grand Piece": [S("Grand Hub", "https://raw.githubusercontent.com/GrandHub/GrandHub/main/GrandHub.lua")],
    "Tower Defense X": [S("TDX Hub", "https://raw.githubusercontent.com/TDXHub/TDXHub/main/TDXHub.lua")],
    "Strongest Battlegrounds": [S("Strongest Hub", "https://raw.githubusercontent.com/StrongestHub/StrongestHub/main/StrongestHub.lua")],
}

def make_text(page):
    maps = list(SCRIPTS.keys())
    per_page = 10
    start = (page - 1) * per_page
    end = start + per_page
    text = ""
    for i, map_name in enumerate(maps[start:end], start=start+1):
        text += f"{i}. {map_name}\n"
    return text

TOTAL_PAGES = (len(SCRIPTS) + 9) // 10

# ===== BARU: SELECT HUB - PILIH HUB, MUNCUL CUMA LOADSTRING TOK =====
class HubSelect(discord.ui.Select):
    def __init__(self, map_name):
        self.map_name = map_name
        options = []
        for hub_name, script in SCRIPTS[map_name]:
            # Discord Select maksimal 25 opsi, jadi 20 aman
            options.append(discord.SelectOption(label=hub_name, value=hub_name))
        super().__init__(placeholder="Select Hub", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        hub_name = self.values[0]
        # Cari loadstring dari hub yang dipilih
        for h, script in SCRIPTS[self.map_name]:
            if h == hub_name:
                # PENTING: Cuma kirim loadstring tok, dak ado kata lain, ephemeral = cuma dio yang liat
                await interaction.response.send_message(f"```lua\n{script}\n```", ephemeral=True)
                return

class HubView(discord.ui.View):
    def __init__(self, map_name):
        super().__init__(timeout=180)
        self.add_item(HubSelect(map_name))

# ===== SELECT GAME - PILIH MAP =====
class GameSelect(discord.ui.Select):
    def __init__(self, page):
        maps = list(SCRIPTS.keys())
        start = (page - 1) * 10
        end = start + 10
        options = [discord.SelectOption(label=m, value=m) for m in maps[start:end]]
        super().__init__(placeholder="Select Game", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        map_name = self.values[0]
        # Munculin Select Hub, ephemeral jugo biar cuma dio yang liat
        await interaction.response.send_message(
            f"**{map_name}**",
            view=HubView(map_name),
            ephemeral=True
        )

class PageView(discord.ui.View):
    def __init__(self, page):
        super().__init__(timeout=180)
        self.page = page
        self.add_item(GameSelect(page))
        if page > 1:
            prev = discord.ui.Button(label="⬅ Prev", style=discord.ButtonStyle.secondary, row=1)
            async def prev_cb(interaction: discord.Interaction, page=page):
                await interaction.response.edit_message(content=f"📜 **LIST {len(SCRIPTS)} MAP - Page {page-1}/{TOTAL_PAGES}**\n{make_text(page-1)}\n━━━━━━━━━━━━━━━━\nRequested By {interaction.user.name}", view=PageView(page-1))
            prev.callback = prev_cb
            self.add_item(prev)
        if page < TOTAL_PAGES:
            nxt = discord.ui.Button(label="Next ➡", style=discord.ButtonStyle.primary, row=1)
            async def next_cb(interaction: discord.Interaction, page=page):
                await interaction.response.edit_message(content=f"📜 **LIST {len(SCRIPTS)} MAP - Page {page+1}/{TOTAL_PAGES}**\n{make_text(page+1)}\n━━━━━━━━━━━━━━━━\nRequested By {interaction.user.name}", view=PageView(page+1))
            nxt.callback = next_cb
            self.add_item(nxt)

@bot.command(name="script")
async def script_prefix(ctx):
    if ctx.channel.id != SCRIPT_CHANNEL_ID:
        await ctx.send(f"❌ Perintah `!script` hanya bisa dipakai di <#{SCRIPT_CHANNEL_ID}>!")
        return
    await ctx.send(f"📜 **LIST {len(SCRIPTS)} MAP - Page 1/{TOTAL_PAGES}**\n{make_text(1)}\n━━━━━━━━━━━━━━━━\nRequested By {ctx.author.name}", view=PageView(1))

@bot.tree.command(name="script", description="Lihat list script")
async def script_slash(interaction: discord.Interaction):
    if interaction.channel_id != SCRIPT_CHANNEL_ID:
        await interaction.response.send_message(f"❌ Perintah `/script` hanya bisa dipakai di <#{SCRIPT_CHANNEL_ID}>!", ephemeral=True)
        return
    await interaction.response.send_message(f"📜 **LIST {len(SCRIPTS)} MAP - Page 1/{TOTAL_PAGES}**\n{make_text(1)}\n━━━━━━━━━━━━━━━━\nRequested By {interaction.user.name}", view=PageView(1))

@bot.event
async def on_ready():
    print(f"Bot SCRIPT login sebagai {bot.user} - Total Map: {len(SCRIPTS)}")
    try:
        synced = await bot.tree.sync()
        print(f"Sync {len(synced)} slash command")
    except Exception as e:
        print(e)

bot.run(TOKEN_SCRIPT)
