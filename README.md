# Tugas 1 Progjar

## Anggota Kelompok
| Nama                              |       NRP      |
|    :----                          |    :----       |
| Aji Rindra Fakhrezi Putra Faisal  | 05111940000205 |
| Inez Yulia Amanda                 | 05111940000208 |

## Task

### Klien
1. Meminta ke server untuk mengunduh salah satu file pada folder dataset (*.html, *.mp3, *.mp4, *.png, dan *.txt) dengan cara mengirim string: "unduh nama_file". Ukuran file lebih dari 1 MB
2. Menerima isi file dari server
3. Melakukan parsing message header. Message header tidak ikut ditulis ke dalam file
4. Isi file yang telah diterima dari server, disimpan dalam sebuah file sesuai ekstensi filenya.

### Server
1. Menerima pesan berupa "unduh nama_file"
2. Membaca file yang diminta oleh klien
3. Menambahkan message header yang diletakkan sebelum isi file dengan struktur sebagai berikut (contoh raw message header):<br>
    file-name: contoh.html,\n<br>
	file-size: 2048,\n<br>
	\n\n
4. Mengirim isi file yang telah dibaca ke klien
5. Server dapat menangani banyak klien (gunakan modul select DAN serversocket pada Python).

### Challenge:
1. Membaca/menulis file dalam mode biner.
2. Mengirim/menerima file yang ukurannya lebih besar daripada buffer pada socket (gunakan loop untuk send/recv
3. Menggunakan virtual box untuk simulasi dua host atau lebih.

## How To Run
1. Go to folder named "server" with command 
    ```
    cd server
    ```
2. Run the server first with command 
    ```
    python3 server_select.py
    ```
2. Go to folder named "client" with command
    ```
    cd client
    ```
    , then run the client by using command 
    ```
    python3 client_select.py
    ```
    or just use command 
    ```
    python3 client/client_select.py
    ``` 
    if you don't want to go to folder "client"