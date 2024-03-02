meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "tanggapan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresif/marah"
            }
word = input("Ketiklah kata yang tidak dimengerti(Huruf kapital semua)")
if word in meme_dict.keys():
    print("arti kata", word, "adalah", meme_dict[word])
else:
    print("kata ini tidak ada")
