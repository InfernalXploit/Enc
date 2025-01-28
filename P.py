import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import subprocess  # Untuk menjalankan MPV

# Informasi pembuat dan media sosial
AUTHOR = "INFERNALXPLOIT"
TOOL_NAME = "INFERNALXPLOIT TOOLS"
INSTAGRAM = "Instagram: infernalxploit"
TIKTOK = "TikTok: renxploit1"

# ANSI escape code untuk warna hijau
GREEN = '\033[92m'
RESET = '\033[0m'

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('clear')  # Gunakan 'cls' jika menggunakan Windows

# Fungsi untuk memainkan file audio menggunakan MPV
def play_audio(file_name):
    try:
        subprocess.run(["mpv", file_name], check=True)
    except FileNotFoundError:
        print(f"{GREEN}MPV tidak ditemukan. Pastikan MPV terinstal di sistem Anda!{RESET}")
    except Exception as e:
        print(f"{GREEN}Gagal memutar file: {e}{RESET}")

# Fungsi untuk enkripsi file
def encrypt_file(file_name, key):
    cipher = AES.new(key, AES.MODE_CBC)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    
    # Enkripsi data file
    ct_bytes = cipher.encrypt(pad(file_data, AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    
    # Simpan data terenkripsi ke file baru
    with open(file_name + '.enc', 'w') as enc_file:
        enc_file.write(iv + '\n' + ct)
    
    print(f'\n{GREEN}File terenkripsi disimpan sebagai {file_name}.enc{RESET}')

# Fungsi untuk dekripsi file
def decrypt_file(file_name, key):
    with open(file_name, 'r') as enc_file:
        iv, cipher_text = enc_file.read().splitlines()
    
    iv = base64.b64decode(iv)
    cipher_text = base64.b64decode(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Dekripsi file
    decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size)
    
    # Simpan hasil dekripsi ke file baru
    with open(file_name.replace('.enc', '.dec'), 'wb') as dec_file:
        dec_file.write(decrypted_data)
    
    print(f'\n{GREEN}File terdekripsi disimpan sebagai {file_name.replace(".enc", ".dec")}{RESET}')

# Key harus 16, 24, atau 32 bytes untuk AES
key = b'Sixteen byte key'

# Putar audio saat program dijalankan
play_audio("P.mp3")

# Menu utama
while True:
    clear_screen()
    print(GREEN + "########################################")
    print(f"# Tool   : {TOOL_NAME:<28}#")
    print(f"# Author : {AUTHOR:<28}#")
    print(f"# {INSTAGRAM:<36}#")
    print(f"# {TIKTOK:<36}#")
    print("########################################")
    print("# 1. Enkripsi file                      #")
    print("# 2. Dekripsi file                      #")
    print("# 3. Keluar                             #")
    print("########################################" + RESET)

    choice = input("Pilih opsi (1/2/3): ")

    if choice == '1' or choice == '2':
        play_audio("P.mp3")  # Putar audio saat memilih menu
        clear_screen()
        
        # Menambahkan bagian untuk memilih file .enc
        if choice == '2':  # Untuk opsi dekripsi
            file_name = input("Masukkan nama file .enc yang ingin didekripsi: ")
        else:
            file_name = input("Masukkan nama file yang ingin dienkripsi: ")

        if choice == '1':
            encrypt_file(file_name, key)
        elif choice == '2':
            decrypt_file(file_name, key)

        input(f"\n{GREEN}Tekan Enter untuk kembali ke menu...{RESET}")
    elif choice == '3':
        play_audio("P.mp3")  # Putar audio saat keluar
        clear_screen()
        print(GREEN + "Keluar dari program. Sampai jumpa!" + RESET)
        break
    else:
        print(f"\n{GREEN}Pilihan tidak valid!{RESET}")
        input(f"\n{GREEN}Tekan Enter untuk kembali ke menu...{RESET}")