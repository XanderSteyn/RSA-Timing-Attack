---

# 🔓 RSA Timing Attack

A Python-based tool that simulates a timing attack on an RSA private key using the public key and private exponent. The script uses a multiprocessing approach to optimize the attack.

⚠️ **Use responsibly** – Only run this tool on systems you own or have explicit permission to test.

## ⚙️ Features
- Simulates a timing attack on RSA encryption by exploiting the time differences in modular exponentiation.
- Leverages multiprocessing for faster bit guessing and key recovery.
- Allows for experimentation with various key sizes and attack parameters.

## 🚀 Installation

### Prerequisites

To run this project, you'll need Python 3.x installed and the following dependencies :

```bash
pip install pycryptodome
```

### 🛠️ Setup

1. Clone the repository to your local machine :

   ```bash
   git clone https://github.com/XanderSteyn/RSA-Timing-Attack.git
   cd RSA-Timing-Attack
   ```

2. Run the script :

   ```bash
   python RSATiming.py
   ```

### 📦 Dependencies

- `pycryptodome` A library for cryptographic operations, used for key generation and modular arithmetic.

## 🛑 How It Works

1. **Key Generation** : The script generates a 512-bit RSA key pair (public and private keys) using prime numbers and modular arithmetic.
2. **Timing Attack** : It then attempts to recover the private key by observing the time differences when performing modular exponentiation with bits of the private exponent.
3. **Parallel Processing** : The script uses Python's `multiprocessing` module to parallelize the bit-guessing process, speeding up the attack.
4. **Bit Guessing** : For each bit of the private key, it guesses whether the bit is 0 or 1 by measuring the time taken for each modular exponentiation and choosing the bit corresponding to the longest time.

## 📝 Usage

1. Run the script :
   ```bash
   python RSATiming.py
   ```

2. The script will continuously try to guess the private key by performing the timing attack and outputting the guessed key vs the actual key.
3. If the guessed key matches the actual private key, the attack is complete, and the script will print a success message.

## ⚙️ Configuration

- **NumTrials** : The number of trials for each bit guess. You can adjust this for more accurate results, though more trials will take longer.
- **BatchSize** : Number of bits to process in parallel. You can adjust this for performance optimization.

## 🧰 Example Output

```text
Guessed private key
110101110101...
Actual private key
110101110101...

Match found!
```

---
