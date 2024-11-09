import sqlite3
from datetime import datetime

# Koneksi ke database SQLite
conn = sqlite3.connect('personal_finance.db')
cursor = conn.cursor()

# Membuat tabel untuk transaksi jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        type TEXT,
        amount REAL,
        description TEXT
    )
''')
conn.commit()

# Fungsi untuk menambahkan transaksi baru
def add_transaction(date, type, amount, description):
    cursor.execute('''
        INSERT INTO transactions (date, type, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, type, amount, description))
    conn.commit()
    print("Transaksi berhasil ditambahkan.")

# Fungsi untuk melihat semua transaksi
def view_transactions():
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    for transaction in transactions:
        print(transaction)

# Fungsi untuk mengupdate transaksi
def update_transaction(transaction_id, new_date, new_type, new_amount, new_description):
    cursor.execute('''
        UPDATE transactions
        SET date = ?, type = ?, amount = ?, description = ?
        WHERE id = ?
    ''', (new_date, new_type, new_amount, new_description, transaction_id))
    conn.commit()
    print("Transaksi berhasil diperbarui.")

# Fungsi untuk menghapus transaksi
def delete_transaction(transaction_id):
    cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
    conn.commit()
    print("Transaksi berhasil dihapus.")

# Fungsi utama untuk menu interaktif
def main():
    while True:
        print("\n=== Sistem Manajemen Keuangan Pribadi ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Update Transaksi")
        print("4. Hapus Transaksi")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1/2/3/4/5): ")
        
        if choice == '1':
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            type = input("Jenis transaksi (income/expense): ")
            amount = float(input("Jumlah: "))
            description = input("Deskripsi: ")
            add_transaction(date, type, amount, description)
        
        elif choice == '2':
            print("\n=== Daftar Semua Transaksi ===")
            view_transactions()
        
        elif choice == '3':
            transaction_id = int(input("Masukkan ID transaksi yang ingin diupdate: "))
            new_date = input("Masukkan tanggal baru (YYYY-MM-DD): ")
            new_type = input("Jenis transaksi baru (income/expense): ")
            new_amount = float(input("Jumlah baru: "))
            new_description = input("Deskripsi baru: ")
            update_transaction(transaction_id, new_date, new_type, new_amount, new_description)
        
        elif choice == '4':
            transaction_id = int(input("Masukkan ID transaksi yang ingin dihapus: "))
            delete_transaction(transaction_id)
        
        elif choice == '5':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()

# Tutup koneksi database saat program selesai
conn.close()
