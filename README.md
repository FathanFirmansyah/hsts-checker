# HSTS Checker 

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![GitHub Issues](https://img.shields.io/github/issues/FathanFirmansyah/hsts-checker)
![GitHub Forks](https://img.shields.io/github/forks/FathanFirmansyah/hsts-checker)
![GitHub Stars](https://img.shields.io/github/stars/FathanFirmansyah/hsts-checker)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Using a File](#using-a-file)
  - [Combining Arguments and File](#combining-arguments-and-file)
  - [Saving Results to CSV](#saving-results-to-csv)
- [Examples](#examples)

## Overview

**HSTS Checker** adalah sebuah tools command-line yang memungkinkan Anda untuk memeriksa apakah satu atau lebih website menerapkan **HTTP Strict Transport Security (HSTS)**. HSTS adalah kebijakan keamanan web yang membantu melindungi website dari serangan man-in-the-middle dengan memaksa penggunaan HTTPS.

Dengan **HSTS Checker**, Anda dapat:

- Memeriksa banyak domain sekaligus.
- Menggunakan input domain langsung atau melalui file.
- Mendapatkan hasil yang jelas dan terstruktur.
- Menyimpan hasil pengecekan ke dalam file CSV untuk analisis lebih lanjut.

## Features

- **Multi-Domain Check**: Memeriksa HSTS pada beberapa domain sekaligus.
- **Flexible Input**: Mendukung input domain melalui argumen atau file.
- **Colored Output**: Menampilkan hasil dengan warna untuk memudahkan identifikasi.
- **Output to CSV**: Menyimpan hasil pengecekan ke file CSV.
- **Easy Integration**: Mudah diintegrasikan ke dalam workflow Anda di Kali Linux atau sistem berbasis Linux lainnya.

## Prerequisites

Sebelum menginstal **HSTS Checker**, pastikan Anda memenuhi persyaratan berikut:

- **Operating System**: Kali Linux atau distribusi Linux lainnya.
- **Python**: Python 3.6 atau lebih baru.
- **Pip**: Python package manager.

## Installation

### 1. Clone Repository

Pertama, clone repository ini ke direktori lokal Anda:

```bash
git clone https://github.com/FathanFirmansyah/hsts-checker.git
```

### 2. Navigasi ke Direktori

Masuk ke direktori proyek:

```bash
cd hsts-checker
```

### 3. Install Dependencies

Instal dependensi yang diperlukan menggunakan pip:

```bash
pip install -r requirements.txt
```

### 4. Berikan Izin Eksekusi

Pastikan skrip memiliki izin eksekusi:

```bash
chmod +x hsts_checker
```

### 5. Pindahkan ke Direktori yang Ada di PATH

Untuk menjalankan tools dari mana saja, pindahkan skrip ke /usr/local/bin/:

```bash
sudo mv hsts_checker /usr/local/bin/hsts_checker
```

## Usage

Setelah instalasi selesai, Anda dapat menggunakan HSTS Checker  melalui terminal.

### Basic Usage

Memeriksa satu atau lebih domain secara langsung:

```bash
hsts_checker domain1.com domain2.com domain3.com
```

### Using a File

Memeriksa domain yang terdaftar dalam file, satu domain per baris:

```bash
hsts_checker -f domains.txt
```

### Combining Arguments and File

Anda juga dapat menggabungkan input dari argumen dan file:

```bash
hsts_checker domain1.com -f domains.txt
```

### Saving Results to CSV

Menyimpan hasil pengecekan ke file CSV untuk analisis lebih lanjut:

```bash
hsts_checker domain1.com domain2.com -o results.csv
```

## Examples

### 1. Memeriksa Beberapa Domain Langsung

```bash
hsts_checker google.com example.com github.com
```

- Output:

```bash
========================================
          HSTS CHECKER 
========================================

Hasil Pengecekan HSTS:

google.com: Yes
example.com: No
github.com: Yes
```

### 2. Memeriksa Domain dari File

Buat file domains.txt dengan isi:

```bash
google.com
example.com
github.com
```

Kemudian jalankan:

```bash
hsts_checker -f domains.txt
```

- Output:

```bash
========================================
          HSTS CHECKER 
========================================

Hasil Pengecekan HSTS:

google.com: Yes
example.com: No
github.com: Yes
```

### 3. Menggabungkan Argumen dan File

```bash
hsts_checker yahoo.com -f domains.txt
```

- Output:
```bash
========================================
          HSTS CHECKER 
========================================

Hasil Pengecekan HSTS:

yahoo.com: Yes
google.com: Yes
example.com: No
github.com: Yes
```

### 4. Menyimpan Hasil ke File CSV
```bash
hsts_checker google.com example.com -o hasil.csv
```
- Output di Terminal:

```bash
========================================
          HSTS CHECKER 
========================================

Hasil Pengecekan HSTS:

google.com: Yes
example.com: No

Hasil telah disimpan ke hasil.csv
```

Isi hasil.csv:

```bash
domain,HSTS,Header
google.com,Yes,max-age=31536000; includeSubDomains; preload
example.com,No,
```
