import os
import discord
from discord.ext import commands

# 1. Konfigurasi Intent
# Membutuhkan Server Members Intent agar bisa mendeteksi member baru
intents = discord.Intents.default()
intents.members = True  # Mengaktifkan Privileged Member Intent

# Inisialisasi bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot berhasil login sebagai {bot.user.name} (ID: {bot.user.id})")
    print("--------------------------------------------------")

# 2. Event ketika ada member baru bergabung
@bot.event
async def on_member_join(member: discord.Member):
    # Cari channel bernama 'welcome'
    channel = discord.utils.get(member.guild.channels, name="welcome")
    
    # Jika channel 'welcome' ditemukan
    if channel:
        # Menghitung jumlah member di server saat ini
        total_members = member.guild.member_count
        
        # Membuat Embed yang keren
        embed = discord.Embed(
            title=f"🎉 Selamat Datang di {member.guild.name}!",
            description=f"Halo {member.mention}, selamat bergabung!\nSemoga betah dan have fun di sini! 🔥",
            color=discord.Color.gold()  # Warna bar samping embed (bisa diganti sesuai selera)
        )
        
        # Menampilkan Avatar Member
        avatar_url = member.avatar.url if member.avatar else member.default_avatar.url
        embed.set_thumbnail(url=avatar_url)
        
        # Menampilkan Informasi Jumlah Member di Footer
        embed.set_footer(
            text=f"Kamu adalah member ke-{total_members} di server ini!",
            icon_url=member.guild.icon.url if member.guild.icon else None
        )
        
        # Mengirim embed ke channel #welcome
        await channel.send(embed=embed)
    else:
        print(f"⚠️ Channel '#welcome' tidak ditemukan di server {member.guild.name}.")

# 3. Jalankan bot dengan Token dari Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Error: Environment variable 'DISCORD_TOKEN' tidak ditemukan!")
    print("Harap set DISCORD_TOKEN sebelum menjalankan bot.")
