#!/usr/bin/env python3
import requests
from requests.exceptions import SSLError, ConnectionError
import sys
import argparse
from colorama import init, Fore, Style

def cek_hsts(url):
    # Pastikan URL dimulai dengan https://
    if not url.startswith('https://'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=10)
        hsts = response.headers.get('Strict-Transport-Security')

        if hsts:
            return True, hsts
        else:
            return False, None
    except SSLError as e:
        print(f"{Fore.RED}SSL Error saat mengakses {url}: {e}{Style.RESET_ALL}")
        return False, None
    except ConnectionError as e:
        print(f"{Fore.RED}Gagal terhubung ke {url}: {e}{Style.RESET_ALL}")
        return False, None
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan saat mengakses {url}: {e}{Style.RESET_ALL}")
        return False, None

def tampilkan_header():
    init(autoreset=True)  # Inisialisasi colorama
    header = f"""
{Fore.CYAN}========================================
          HSTS CHECKER
========================================{Style.RESET_ALL}
"""
    print(header)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="HSTS Checker - Memeriksa apakah website menggunakan HSTS."
    )
    parser.add_argument(
        'domains',
        metavar='DOMAIN',
        type=str,
        nargs='*',  # Mengubah dari '+' menjadi '*' agar opsional
        help='Satu atau lebih domain yang ingin diperiksa (misal: example.com)'
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        help='Path ke file yang berisi daftar domain, satu per baris.'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Path ke file output untuk menyimpan hasil (format CSV).'
    )
    return parser.parse_args()

def main():
    tampilkan_header()
    args = parse_arguments()

    # Jika file disediakan, baca domain dari file
    domains = set()  # Gunakan set untuk menghindari duplikasi
    if args.file:
        try:
            with open(args.file, 'r') as file:
                file_domains = [line.strip() for line in file if line.strip()]
                domains.update(file_domains)
        except FileNotFoundError:
            print(f"{Fore.RED}File tidak ditemukan: {args.file}{Style.RESET_ALL}")
            sys.exit(1)
        except Exception as e:
            print(f"{Fore.RED}Terjadi kesalahan saat membaca file: {e}{Style.RESET_ALL}")
            sys.exit(1)

    # Tambahkan domain dari argumen
    domains.update(args.domains)

    if not domains:
        print(f"{Fore.YELLOW}Tidak ada domain yang diberikan untuk diperiksa. Gunakan argumen DOMAIN atau opsi -f.{Style.RESET_ALL}")
        sys.exit(0)

    print(f"\n{Fore.GREEN}Hasil Pengecekan HSTS:{Style.RESET_ALL}\n")

    hasil = []

    for domain in domains:
        if not domain:
            continue  # Lewati domain kosong
        status, header = cek_hsts(domain)
        if status:
            print(f"{Fore.GREEN}{domain}: Yes{Style.RESET_ALL}")
            hasil.append({'domain': domain, 'HSTS': 'Yes', 'Header': header})
        else:
            print(f"{Fore.RED}{domain}: No{Style.RESET_ALL}")
            hasil.append({'domain': domain, 'HSTS': 'No', 'Header': header})

    # Simpan hasil ke file jika opsi output diberikan
    if args.output:
        try:
            with open(args.output, 'w', newline='') as csvfile:
                import csv
                fieldnames = ['domain', 'HSTS', 'Header']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in hasil:
                    writer.writerow(row)
            print(f"\nHasil telah disimpan ke {args.output}")
        except Exception as e:
            print(f"{Fore.RED}Gagal menyimpan hasil ke file: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Skrip dihentikan oleh pengguna.{Style.RESET_ALL}")
        sys.exit(0)
