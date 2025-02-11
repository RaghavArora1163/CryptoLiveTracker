# CryptoLiveTracker

## 📌 Project Overview
CryptoLiveTracker is a Python-based project that fetches live cryptocurrency data, analyzes it, and updates an Excel sheet (`crypto_data.xlsx`) every 5 minutes. The data includes real-time prices, market capitalization, trading volume, and percentage price changes.

## 🚀 Features
- ✅ Fetches the **top 50 cryptocurrencies** by market capitalization using the CoinGecko API.
- ✅ **Updates an Excel sheet (`crypto_data.xlsx`)** with real-time data every 5 minutes.
- ✅ **Performs basic analysis** (top 5 cryptos, average price, highest & lowest 24h price change).

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
 git clone https://github.com/yourusername/CryptoLiveTracker.git
 cd CryptoLiveTracker
```

### **2️⃣ Install Dependencies**
Make sure you have Python **3.x** installed, then run:
```sh
 pip install -r scripts/requirements.txt
```

### **3️⃣ Run the Tracker**
```sh
 python scripts/crypto_tracker.py
```

### **4️⃣ Check Live Data in Excel**
The script will update the **Excel file (`data/crypto_data.xlsx`)** every 5 minutes.

---

## 🛠 Running the Script

### **Windows**
- Run the script manually:
  ```sh
  python scripts/crypto_tracker.py
  ```
- Or double-click `run_tracker.bat` to execute automatically.

### **Mac/Linux**
- Run the script manually:
  ```sh
  python scripts/crypto_tracker.py
  ```
- Make the script executable and run it:
  ```sh
  chmod +x run_tracker.sh
  ./run_tracker.sh
  ```
- To run in the background:
  ```sh
  nohup python scripts/crypto_tracker.py &
  ```

---

## 📊 How It Works
1. The script **fetches** live cryptocurrency data from the **CoinGecko API**.
2. It **analyzes** the top 50 cryptos, extracting:
   - **Top 5 by market cap**
   - **Average price** of the top 50 cryptos
   - **Highest & lowest 24h price change**
3. The script **updates the Excel sheet (`crypto_data.xlsx`)** every 5 minutes.

---

## 🤝 Contributing
Feel free to contribute to this project by submitting issues or pull requests!

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📧 Contact
For any issues, feel free to contact **[Raghav Arora]** at [raghavarora1163@gmail.com].

