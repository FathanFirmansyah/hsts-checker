# HSTS Checker by SOC

![License](https://img.shields.io/badge/license-MIT-blue.svg)
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
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**HSTS Checker by SOC** adalah sebuah tools command-line yang memungkinkan Anda untuk memeriksa apakah satu atau lebih website menerapkan **HTTP Strict Transport Security (HSTS)**. HSTS adalah kebijakan keamanan web yang membantu melindungi website dari serangan man-in-the-middle dengan memaksa penggunaan HTTPS.

Dengan **HSTS Checker by SOC**, Anda dapat:

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

Sebelum menginstal **HSTS Checker by SOC**, pastikan Anda memenuhi persyaratan berikut:

- **Operating System**: Kali Linux atau distribusi Linux lainnya.
- **Python**: Python 3.6 atau lebih baru.
- **Pip**: Python package manager.

## Installation

### 1. Clone Repository

Pertama, clone repository ini ke direktori lokal Anda:

```bash
git clone https://github.com/FathanFirmansyah/hsts-checker.git
