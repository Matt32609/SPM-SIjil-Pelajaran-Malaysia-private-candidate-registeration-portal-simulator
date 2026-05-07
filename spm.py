#!/usr/bin/env python3

import datetime
import json
import re

def spm_registeration():
    try:
        while True:
            print("Selamat datang ke aplikasi simulasi pendaftaran calon persendirian peperiksaan Sijil Pelajaran Malaysia (SPM). Sila pilih jenis pilihan dengan masukkan digit 1 atau 2.")
            print("(1) Mula | (2) Keluar")
            options_input = int(input("Masukkan digit di sini:"))
            if options_input == 1:
                return bahasa_malaysia()
            elif options_input == 2:
                exit()
            else:
                print("Respon yang tidak sah.")
    except ValueError:
        print("Respon yang tidak sah.")
        return spm_registeration()

def bahasa_malaysia():
    try:
        while True:
            print("--- PORTAL PENDAFTARAN PEPERIKSAAN CALON PERSENDIRIAN SIJIL PELAJARAN MALAYSIA (SPM) ---")
            print("Sila pilih jenis pilihan yang disenaraikan di bawah")
            print("(1) --- Daftar Calon Baharu")
            print("(2) --- Daftar Calon Mengulang")
            print("(3) --- Semakan Status")
            print("(4) --- Kembali")
            print("(5) --- Tetap semula")
            option_input = int(input("Masukkan digit di sini:"))
            if option_input == 1:
                calon_baharu()
                break
            elif option_input == 2:
                calon_mengulang()
                break
            elif option_input == 3:
                semakan_status()
                break
            elif option_input == 4:
                return spm_registeration()
            elif option_input == 5:
                with open("pendaftaran_spm.json", "w") as fail:
                    json.dump({}, fail) 
                print("Sistem telah berjaya ditetapkan semula.")
            else:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()
    except ValueError:
        print("Respon yang tidak sah.")
        return bahasa_malaysia()

def calon_mengulang():
    while True:
        try:
            kp = input("Sila masukkan nombor kad pengenalan anda: (12 digit)")
            try:
                with open("pendaftaran_spm.json", "r") as fail:
                    database = json.load(fail)
                
                if kp not in database:
                    print(f"Permohonan anda tidak boleh diteruskan kerana maklumat yang dimasukkan tidak dijumpai.")
                    return bahasa_malaysia() 
            except (FileNotFoundError, json.JSONDecodeError):
                pass
            if len(kp) < 12 or len(kp) > 12:
                print("Nombor kad pengenalan adalah tidak sah.")
                return bahasa_malaysia()
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()
        else:
            year_part = int(kp[0:2])
            month_part = int(kp[2:4])
            day_part = int(kp[4:6])

            current_year = datetime.datetime.now().year
            year_cutoff = current_year % 100 
                    
            if year_part <= year_cutoff:
                full_year = 2000 + year_part
            else:
                full_year = 1900 + year_part

            if full_year >= 2010:
                print(f"Nombor kad pengenalan yang dimasukkan adalah tidak sah.")
                continue
            valid_date = datetime.date(full_year, month_part, day_part)
            print(f"Nombor kad pengenalan diri: {kp}")
            print("(1) Teruskan | (2) Kembali")
            print("Adakah anda ingin teruskan pendaftaran ini?")
            confirmation_bm = int(input("Masukkan digit di sini:"))
            if confirmation_bm == 1:
                calon_mengulang_pendaftaran(kp)
                break
            elif confirmation_bm == 2:
                return bahasa_malaysia()
            else:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()

def calon_baharu():
    while True:
        try:
            kp = input("Sila masukkan nombor kad pengenalan anda: (12 digit) ")
            try:
                with open("pendaftaran_spm.json", "r") as fail:
                    database = json.load(fail)
                
                if kp in database:
                    print(f"Permohonan anda tidak boleh diteruskan kerana rekod permohonan anda telah wujud.")
                    return bahasa_malaysia() 
            except (FileNotFoundError, json.JSONDecodeError):
                pass
            if len(kp) < 12 or len(kp) > 12:
                print("Nombor kad pengenalan adalah tidak sah.")
                return bahasa_malaysia()
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()
        else:
            try:
                year_part = int(kp[0:2])
                month_part = int(kp[2:4])
                day_part = int(kp[4:6])

                current_year = datetime.datetime.now().year
                year_cutoff = current_year % 100 
                    
                if year_part <= year_cutoff:
                    full_year = 2000 + year_part
                else:
                    full_year = 1900 + year_part

                if full_year >= 2010:
                    print(f"Nombor kad pengenalan yang dimasukkan adalah tidak sah.")
                    continue
                valid_date = datetime.date(full_year, month_part, day_part)
                print(f"Nombor kad pengenalan diri: {kp}")
                print("(1) Teruskan | (2) Kembali")
                print("Adakah anda ingin teruskan pendaftaran ini?")
                confirmation_bm = int(input("Masukkan digit di sini:"))
                if confirmation_bm == 1:
                    calon_baharu_pendaftaran(kp)
                    break
                elif confirmation_bm == 2:
                    return bahasa_malaysia()
                else:
                    print("Respon yang tidak sah.")
                    return bahasa_malaysia()
            except ValueError:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()

def calon_mengulang_pendaftaran(kp):
    while True:
        try:
            nama_calon = str(input("Sila masukkan nama penuh anda.")).strip().upper()
            if len(nama_calon) == 0 or nama_calon.isdigit():
                print("Nama calon yang tidak sah.")
                return bahasa_malaysia()

            surat_anak = (input("Sila masukkan nombor surat beranak anda. (7 digit)"))
            if len(surat_anak) != 7 or not surat_anak.isdigit():
                print("Nombor surat beranak yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Lelaki | (2) Perempuan")
            jantina = int(input("Sila masukkan jantina anda dengan menekan digit 1 atau 2."))
            pilihan_jantina = {1: "Lelaki", 2: "Perempuan"}
            if jantina in pilihan_jantina:
                jantina_dipilih = pilihan_jantina[jantina]
            else:
                print("Pilihan jantina yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Melayu/Bumiputera | (2) Cina | (3) India | (4) Lain-lain")
            kaum = int(input("Sila masukkan kaum anda dengan menekan digit 1 , 2 , 3 atau 4."))
            pilihan_kaum = {1: "Melayu/Bumiputera", 2: "Cina", 3: "India", 4: "Lain-lain"}
            if kaum in pilihan_kaum:
                kaum_dipilih = pilihan_kaum[kaum]
            else:
                print("Pilihan kaum yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Islam | (2) Lain-lain ")
            agama = int(input("Sila masukkan agama anda dengan menekan digit 1 atau 2."))
            pilihan_agama = {1: "Islam", 2: "Lain-lain"}
            if agama in pilihan_agama:
                agama_dipilih = pilihan_agama[agama]
            else:
                print("Pilihan agama yang tidak sah.")
                return bahasa_malaysia()
            
            alamat = str(input("Sila masukkan alamat anda.")).strip().upper()
            if len(alamat) == 0:
                print("Alamat yang tidak sah.")
                return bahasa_malaysia()

            negeri_dan_bandar = str(input("Sila masukkan bandar dan negeri anda.")).strip().upper()
            if len(negeri_dan_bandar) == 0:
                print("Negeri dan/atau bandar yang tidak sah.")
                return bahasa_malaysia()

            poskod = input("Sila masukkan poskod anda.")
            if len(poskod) != 5 or not poskod.isdigit():
                print("Nombor poskod yang tidak sah.")
                return bahasa_malaysia()
            
            telefon = input("Sila masukkan nombor telefon anda.")
            if len(telefon) < 10 or len(telefon) > 16 or not telefon.isdigit():
                print("Nombor telefon yang tidak sah.")
                return bahasa_malaysia()
            
            print("Maklumat peribadi anda telah lengkap.")
            calon_mengulang_pilihan_MP(kp, surat_anak, agama_dipilih, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih)
            break
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()

def calon_baharu_pendaftaran(kp):
    while True:
        try:
            nama_calon = str(input("Sila masukkan nama penuh anda.")).strip().upper()
            if len(nama_calon) == 0 or nama_calon.isdigit():
                print("Nama calon yang tidak sah.")
                return bahasa_malaysia()

            surat_anak = (input("Sila masukkan nombor surat beranak anda. (7 digit)"))
            if len(surat_anak) != 7 or not surat_anak.isdigit():
                print("Nombor surat beranak yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Lelaki | (2) Perempuan")
            jantina = int(input("Sila masukkan jantina anda dengan menekan digit 1 atau 2."))
            pilihan_jantina = {1: "Lelaki", 2: "Perempuan"}
            if jantina in pilihan_jantina:
                jantina_dipilih = pilihan_jantina[jantina]
            else:
                print("Pilihan jantina yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Melayu/Bumiputera | (2) Cina | (3) India | (4) Lain-lain")
            kaum = int(input("Sila masukkan kaum anda dengan menekan digit 1 , 2 , 3 atau 4."))
            pilihan_kaum = {1: "Melayu/Bumiputera", 2: "Cina", 3: "India", 4: "Lain-lain"}
            if kaum in pilihan_kaum:
                kaum_dipilih = pilihan_kaum[kaum]
            else:
                print("Pilihan kaum yang tidak sah.")
                return bahasa_malaysia()
            
            print("(1) Islam | (2) Lain-lain ")
            agama = int(input("Sila masukkan agama anda dengan menekan digit 1 atau 2."))
            pilihan_agama = {1: "Islam", 2: "Lain-lain"}
            if agama in pilihan_agama:
                agama_dipilih = pilihan_agama[agama]
            else:
                print("Pilihan agama yang tidak sah.")
                return bahasa_malaysia()
            
            alamat = str(input("Sila masukkan alamat anda.")).strip().upper()
            if len(alamat) == 0:
                print("Alamat yang tidak sah.")
                return bahasa_malaysia()

            negeri_dan_bandar = str(input("Sila masukkan bandar dan negeri anda.")).strip().upper()
            if len(negeri_dan_bandar) == 0:
                print("Negeri dan/atau bandar yang tidak sah.")
                return bahasa_malaysia()

            poskod = input("Sila masukkan poskod anda.")
            if len(poskod) != 5 or not poskod.isdigit():
                print("Nombor poskod yang tidak sah.")
                return bahasa_malaysia()
            
            telefon = input("Sila masukkan nombor telefon anda.")
            if len(telefon) < 10 or len(telefon) > 16 or not telefon.isdigit():
                print("Nombor telefon yang tidak sah.")
                return bahasa_malaysia()
            
            print("Maklumat peribadi anda telah lengkap.")
            calon_baharu_pilihan_MP(kp, surat_anak, agama_dipilih, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih)
            break
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()

def calon_mengulang_pilihan_MP(kp, surat_anak, agama_dipilih, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih):
    try:
        pilihan_MP_input = {1: ["1103", "Bahasa Melayu", 12.00],
            2: ["1119", "Bahasa Inggeris", 20.50],
            3: ["1223", "Pendidikan Islam", 12.00],
            4: ["1225", "Pendidikan Moral", 10.50],
            5: ["1249", "Sejarah", 10.50],
            6: ["1449", "Matematik", 10.50],
            7: ["1511", "Sains", 10.50],
            8: ["2206", "Kesusasteraan Inggeris", 10.50],
            9: ["2280", "Geografi", 10.50],
            10: ["2361", "Bahasa Arab", 12.00],
            11: ["3472", "Matematik Tambahan", 10.50],
            12: ["3756", "Prinsip Perakaunan", 12.00],
            13: ["3666", "Perniagaan", 12.00],
            14: ["3667", "Ekonomi", 10.50],
            15: ["4531", "Fizik", 12.00],
            16: ["4541", "Kimia", 12.00],
            17: ["4551", "Biologi", 12.00],
            18: ["4561", "Sains Tambahan", 12.00],
            19: ["5226", "Tasawwur Islam", 10.50],
            20: ["5227", "Pendidikan Al-Quran dan Al-Sunnah", 12.00],
            21: ["5228", "Pendidikan Syariah Islamiah", 10.50],
            22: ["6351", "Bahasa Cina", 12.00],
            23: ["6354", "Bahasa Tamil", 12.00],
            24: ["6356", "Bahasa Iban", 12.00],
            25: ["6357", "Bahasa Kadazandusun", 12.00],
            26: ["6358", "Bahasa Semai", 10.50],
            27: ["9216", "Kesusasteraan Cina", 10.50],
            28: ["9217", "Kesusasteraan Tamil", 10.50],
            29: ["9221", "Bible Knowledge", 10.50],
            30: ["9378", "Bahasa Punjabi", 10.50]
        }
 
        while True:
            print("(1) --- 1103 Bahasa Melayu (RM12)")
            print("(2) --- 1119 Bahasa Inggeris (RM20.50)")
            print("(3) --- 1223 Pendidikan Islam (RM12)")
            print("(4) --- 1225 Pendidikan Moral (RM10.50)")
            print("(5) --- 1249 Sejarah (RM10.50)")
            print("(6) --- 1449 Matematik (RM10.50)")
            print("(7) --- 1511 Sains (RM10.50)")
            print("(8) --- 2206 Kesusasteraan Inggeris (RM10.50)")
            print("(9) --- 2280 Geografi (RM10.50)")
            print("(10) --- 2361 Bahasa Arab (RM12)")
            print("(11) --- 3472 Matematik Tambahan (RM10.50)")
            print("(12) --- 3756 Prinsip Perakaunan (Kertas 1 , 2 dan 4) (RM12)")
            print("(13) --- 3666 Perniagaan (Kertas 1 , 2 dan 4) (RM12)")
            print("(14) --- 3667 Ekonomi (RM10.50)")
            print("(15) --- 4531 Fizik (RM12)")
            print("(16) --- 4541 Kimia (RM12)")
            print("(17) --- 4551 Biologi (RM12)")
            print("(18) --- 4561 Sains Tambahan (RM12)")
            print("(19) --- 5226 Tawassur Islam (RM10.50)")
            print("(20) --- 5227 Pendidikan Al-Quran dan Al-Sunnah (RM12)")
            print("(21) --- 5228 Pendidikan Syariah Islamiah (RM10.50)")
            print("(22) --- 6351 Bahasa Cina (RM12)")
            print("(23) --- 6354 Bahasa Tamil (RM12)")
            print("(24) --- 6356 Bahasa Iban (RM12)")
            print("(25) --- 6357 Bahasa Kadazandusun (RM12)")
            print("(26) --- 6358 Bahasa Semai (RM10.50)")
            print("(27) --- 9216 Kesusasteraan Cina (RM10.50)")
            print("(28) --- 9217 Kesusasteraan Tamil (RM10.50)")
            print("(29) --- 9221 Bible Knowledge (RM10.50)")
            print("(30) --- 9378 Bahasa Punjabi (RM10.5)")
            mata_pelajaran_input = input("Sila pilih mata pelajaran anda dengan masukkan digit antara julat 1 hingga 30. Tekan butang 'Enter' untuk keluar ke menu utama. Contoh masukkan: 1 , 2 , 3(ATAU)4 , 5 , 6 , 7")
            raw_digit = re.findall(r'\d+', mata_pelajaran_input)
            senarai_pilihan = list(set([int(d)for d in raw_digit]))
            jumlah_dikesan = len(senarai_pilihan)

            if not senarai_pilihan:
                print("Sila pilih mata pelajaran yang anda ingin mendaftarkan.")
                return bahasa_malaysia()
        
            error = False
            sains_tulen = {15, 16, 17, 18}
            jumlah_sains_tulen = len([d for d in senarai_pilihan if d in sains_tulen])

            for d in senarai_pilihan:
                if d not in pilihan_MP_input:
                    print("Pilihan anda tidak sah. Sila pilih semula.")
                    error = True

            if len(senarai_pilihan) < 1:
                print("SIla pilih sekurang-kurangnya satu(1) mata pelajaran.")
                error = True
            if len(senarai_pilihan) > 12:
                print("Calon hanya dibenarkan untuk mendaftar maksimum 12 mata pelajaran sahaja.")
                error = True
            if agama_dipilih == "Lain-lain" and 21 in senarai_pilihan:
                print("Mata Pelajaran Pendidikan Moral (1225) tidak boleh mengambil bersama-sama dengan mata pelajaran Pendidikan Syariah Islamiah (5228)")
                error = True
            if 7 in senarai_pilihan and 15 in senarai_pilihan:
                print("Mata pelajaran Sains (1511) dan Fizik (4531) tidak boleh mengambil bersama-sama.")
                error = True
            if 17 in senarai_pilihan and 13 in senarai_pilihan:
                print("Mata pelajaran Biologi (4551) dan Perniagaan (3666) tidak boleh mengambil bersama-sama.")
                error = True
            if agama_dipilih == "Islam" and 21 in senarai_pilihan:
                print("Mata pelajaran Pendidikan Islam (1223) dan mata pelajaran Pendidikan Syariah Islamiah (5228) tidak boleh mengambil bersama-sama .")
                error = True
            if 16 in senarai_pilihan and 18 in senarai_pilihan:
                print("Mata pelajaran Kimia (4541) dan Sains Tambahan (18) tidak boleh mengambil bersama-sama. ")
                error = True
            if error:
                print("Pilihan anda tidak sah . Sila pilih semula.")
                continue
        
            print("(1) Teruskan | (2) Kembali")
            print(f"Anda telah memilih {jumlah_dikesan} mata pelajaran . Adakah anda ingin teruskan? Masukkan digit 1 atau 2.")
            confirmation = int(input("Masukkan digit di sini:"))
            if confirmation == 1:
                pilih_sekolah(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input)
                break
            elif confirmation == 2:
                continue
            else:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()
    except ValueError:
        print("Respon yang tidak sah.")
        return bahasa_malaysia()

def calon_baharu_pilihan_MP(kp, surat_anak, agama_dipilih, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih):
    try:
        pilihan_MP_input = {1: ["1103", "Bahasa Melayu", 12.00],
            2: ["1119", "Bahasa Inggeris", 20.50],
            3: ["1223", "Pendidikan Islam", 12.00],
            4: ["1225", "Pendidikan Moral", 10.50],
            5: ["1249", "Sejarah", 10.50],
            6: ["1449", "Matematik", 10.50],
            7: ["1511", "Sains", 10.50],
            8: ["2206", "Kesusasteraan Inggeris", 10.50],
            9: ["2280", "Geografi", 10.50],
            10: ["2361", "Bahasa Arab", 12.00],
            11: ["3472", "Matematik Tambahan", 10.50],
            12: ["3756", "Prinsip Perakaunan", 12.00],
            13: ["3666", "Perniagaan", 12.00],
            14: ["3667", "Ekonomi", 10.50],
            15: ["4531", "Fizik", 12.00],
            16: ["4541", "Kimia", 12.00],
            17: ["4551", "Biologi", 12.00],
            18: ["4561", "Sains Tambahan", 12.00],
            19: ["5226", "Tasawwur Islam", 10.50],
            20: ["5227", "Pendidikan Al-Quran dan Al-Sunnah", 12.00],
            21: ["5228", "Pendidikan Syariah Islamiah", 10.50],
            22: ["6351", "Bahasa Cina", 12.00],
            23: ["6354", "Bahasa Tamil", 12.00],
            24: ["6356", "Bahasa Iban", 12.00],
            25: ["6357", "Bahasa Kadazandusun", 12.00],
            26: ["6358", "Bahasa Semai", 10.50],
            27: ["9216", "Kesusasteraan Cina", 10.50],
            28: ["9217", "Kesusasteraan Tamil", 10.50],
            29: ["9221", "Bible Knowledge", 10.50],
            30: ["9378", "Bahasa Punjabi", 10.50]
        }
 
        while True:
            print("(1) --- 1103 Bahasa Melayu (RM12)")
            print("(2) --- 1119 Bahasa Inggeris (RM20.50)")
            print("(3) --- 1223 Pendidikan Islam (RM12)")
            print("(4) --- 1225 Pendidikan Moral (RM10.50)")
            print("(5) --- 1249 Sejarah (RM10.50)")
            print("(6) --- 1449 Matematik (RM10.50)")
            print("(7) --- 1511 Sains (RM10.50)")
            print("(8) --- 2206 Kesusasteraan Inggeris (RM10.50)")
            print("(9) --- 2280 Geografi (RM10.50)")
            print("(10) --- 2361 Bahasa Arab (RM12)")
            print("(11) --- 3472 Matematik Tambahan (RM10.50)")
            print("(12) --- 3756 Prinsip Perakaunan (Kertas 1 , 2 dan 4) (RM12)")
            print("(13) --- 3666 Perniagaan (Kertas 1 , 2 dan 4) (RM12)")
            print("(14) --- 3667 Ekonomi (RM10.50)")
            print("(15) --- 4531 Fizik (RM12)")
            print("(16) --- 4541 Kimia (RM12)")
            print("(17) --- 4551 Biologi (RM12)")
            print("(18) --- 4561 Sains Tambahan (RM12)")
            print("(19) --- 5226 Tawassur Islam (RM10.50)")
            print("(20) --- 5227 Pendidikan Al-Quran dan Al-Sunnah (RM12)")
            print("(21) --- 5228 Pendidikan Syariah Islamiah (RM10.50)")
            print("(22) --- 6351 Bahasa Cina (RM12)")
            print("(23) --- 6354 Bahasa Tamil (RM12)")
            print("(24) --- 6356 Bahasa Iban (RM12)")
            print("(25) --- 6357 Bahasa Kadazandusun (RM12)")
            print("(26) --- 6358 Bahasa Semai (RM10.50)")
            print("(27) --- 9216 Kesusasteraan Cina (RM10.50)")
            print("(28) --- 9217 Kesusasteraan Tamil (RM10.50)")
            print("(29) --- 9221 Bible Knowledge (RM10.50)")
            print("(30) --- 9378 Bahasa Punjabi (RM10.50)")
            mata_pelajaran_input = input("Sila pilih mata pelajaran anda dengan masukkan digit antara julat 1 hingga 30. Tekan butang 'Enter' untuk keluar ke menu utama. Contoh masukkan: 1 , 2 , 3(ATAU)4 , 5 , 6 , 7")
            raw_digit = re.findall(r'\d+', mata_pelajaran_input)
            senarai_pilihan = list(set([int(d)for d in raw_digit]))
            jumlah_dikesan = len(senarai_pilihan)

            if not senarai_pilihan:
                print("Sila pilih mata pelajaran yang anda ingin mendaftarkan.")
                return bahasa_malaysia()
        
            error = False
            sains_tulen = {15, 16, 17, 18}
            jumlah_sains_tulen = len([d for d in senarai_pilihan if d in sains_tulen])

            for d in senarai_pilihan:
                if d not in pilihan_MP_input:
                    print("Pilihan anda tidak sah. Sila pilih semula.")
                    error = True

            if 1 <= len(senarai_pilihan) < 6:
                print("Enam(6) mata pelajaran mesti diambil.")
                error = True
            if len(senarai_pilihan) > 12:
                print("Calon hanya dibenarkan untuk mendaftar maksimum 12 mata pelajaran sahaja.")
                error = True
            if agama_dipilih == "Islam" and 4 in senarai_pilihan:
                print("Mata pelajaran Pendidikan Islam (1223) dan Pendidikan Moral (1225) tidak boleh mengambil bersama-sama.")
                error = True
            if agama_dipilih == "Lain-lain" and 3 in senarai_pilihan:
                print("Mata pelajaran Pendidikan Islam (1223) dan Pendidikan Moral (1225) tidak boleh mengambil bersama-sama.")
                error = True
            if agama_dipilih == "Lain-lain" and 21 in senarai_pilihan:
                print("Mata Pelajaran Pendidikan Moral (1225) tidak boleh mengambil bersama-sama dengan mata pelajaran Pendidikan Syariah Islamiah (5228)")
                error = True
            if 7 in senarai_pilihan and 15 in senarai_pilihan:
                print("Mata pelajaran Sains (1511) dan Fizik (4531) tidak boleh mengambil bersama-sama.")
                error = True
            if 17 in senarai_pilihan and 13 in senarai_pilihan:
                print("Mata pelajaran Biologi (4551) dan Perniagaan (3666) tidak boleh mengambil bersama-sama.")
                error = True
            if 7 in senarai_pilihan and jumlah_sains_tulen >= 2:
                print("Mata pelajaran Sains (1511) tidak boleh mengambil dengan Dua(2) atau lebih mata pelajaran Sains Tulen.")
                error = True
            if agama_dipilih == "Islam" and 21 in senarai_pilihan:
                print("Mata pelajaran Pendidikan Islam (1223) dan mata pelajaran Pendidikan Syariah Islamiah (5228) tidak boleh mengambil bersama-sama .")
                error = True
            if 16 in senarai_pilihan and 18 in senarai_pilihan:
                print("Mata pelajaran Kimia (4541) dan Sains Tambahan (18) tidak boleh mengambil bersama-sama. ")
                error = True
            if error:
                print("Pilihan anda tidak sah . Sila pilih semula.")
                continue
        
            print("(1) Teruskan | (2) Kembali")
            print(f"Anda telah memilih {jumlah_dikesan} mata pelajaran . Adakah anda ingin teruskan? Masukkan digit 1 atau 2.")
            confirmation = int(input("Masukkan digit di sini:"))
            if confirmation == 1:
                pilih_sekolah(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input)
                break
            elif confirmation == 2:
                continue 
            else:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()
    except ValueError:
        print("Respon yang tidak sah.")
        return bahasa_malaysia()

def pilih_sekolah(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input):
    while True:
        try:
            print("(1) Wilayah Persekutuan Kuala Lumpur | (2) Selangor | (3) Kembali ke menu utama ")
            negeri_pilih = int(input("Sila pilih negeri dengan masukkan digit 1 hingga 3."))
            if negeri_pilih == 1:
                kuala_lumpur(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, negeri_pilih)
                break
            elif negeri_pilih == 2:
                selangor(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, negeri_pilih)
                break
            elif negeri_pilih == 3:
                return bahasa_malaysia()
                break
            else:
                print("Respon yang tidak sah.")
                return bahasa_malaysia()
        except ValueError:
            return bahasa_malaysia() 

def kuala_lumpur(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, negeri_pilih):
    while True:
        try:
            print("(1) SMK Seri Mutiara | (2) SMK Amiruddin Baki | (3) Victoria Institution | (4) St. John Institution | (5) Convent Bukit Nanas | (6) Kembali ke pilihan negeri")
            sek_dipilihkl = int(input("Sila pilih pusat peperiksaan dengan masukkan digit 1 hingga 6: "))
            senarai_sekkl = {1: "SMK Seri Mutiara", 2: "SMK Amiruddin Baki", 3: "Victoria Institution", 4: "St. John Institution", 5: "Convent Bukit Nanas"}

            if sek_dipilihkl in senarai_sekkl:
                sekolahkl = senarai_sekkl[sek_dipilihkl] 
                bayaran(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, sekolahkl, None)
                break
            if sek_dipilihkl == 6:
                return pilih_sekolah(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input)
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()

def selangor(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, negeri_pilih):
    while True:
        try:
            print("(1) SMK Bandar Tun Hussein Onn 2 | (2) SMK Bandar Baru Ampang | (3) SMJK Yoke Kuan | (4) SMK Gombak Setia | (5) SMK Pandan Indah | (6) Kembali ke pilihan negeri")
            sek_dipilihsl = int(input("Sila pilih pusat peperiksaan dengan masukkan digit 1 hingga 6: "))
            senarai_seksl = {1: "SMK Bandar Tun Hussein Onn 2", 2: "SMK Bandar Baru Ampang", 3: "SMJK Yoke Kuan", 4: "SMK Gombak Setia", 5: "SMK Pandan Indah"}

            if sek_dipilihsl in senarai_seksl:
                sekolahsl = senarai_seksl[sek_dipilihsl] 
                bayaran(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, None, sekolahsl)
                break
            if sek_dipilihsl == 6:
                return pilih_sekolah(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, agama_dipilih, kaum_dipilih, pilihan_MP_input)
        except ValueError:
            print("Respon yang tidak sah.")
            return bahasa_malaysia()

def bayaran(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, sekolahkl, sekolahsl):
    try:
        print("--- PORTAL PEMBAYARAN LEMBAGA PEPERIKSAAN ---")
        print(f"Nama calon : {nama_calon}")
        print(f"Nombor pengenalan diri: {kp}")
        print(f"Alamat calon : {alamat}")
        print(f"Bandar / Negeri : {negeri_dan_bandar}")
        print(f"Poskod : {poskod}")
        print(f"Jumlah mata pelajaran didaftarkan: {jumlah_dikesan}")

        pusat_peperiksaan = sekolahkl if sekolahkl else sekolahsl
        print(f"Pusat peperiksaan: {pusat_peperiksaan}")

        subject_price = sum(pilihan_MP_input[d][2] for d in senarai_pilihan)
        summation_total = 20.00 + subject_price
        print(f"Jumlah bayaran: RM{summation_total:.2f}")

        data_pendaftaran = {"nama": nama_calon, "alamat": alamat, "bandar / negeri" : negeri_dan_bandar, "poskod": poskod, "pusat": pusat_peperiksaan, "subjek": [pilihan_MP_input[d][1] for d in senarai_pilihan], "bayaran": f"RM{summation_total:.2f}", "tarikh": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "kp": kp, "nombor surat beranak": surat_anak, "Telefon": telefon, "Jantina": jantina_dipilih, "Agama": agama_dipilih, "Kaum": kaum_dipilih}

        print("(1) Hantar permohonan dan bayar | (2) Kembali")  
        payment_confirmation = int(input("Masukkan digit 1 atau 2 di sini: "))
        
        if payment_confirmation == 1:
            try:
                with open("pendaftaran_spm.json", "r") as fail:
                    database = json.load(fail)
            except (FileNotFoundError, json.JSONDecodeError):
                database = {}

            database[kp] = data_pendaftaran
            with open("pendaftaran_spm.json", "w") as fail:
                json.dump(database, fail, indent=4)
                
            print("Terima kasih, pendaftaran anda telah disimpan.")
            exit()
            
        elif payment_confirmation == 2:
            print("(1) Kembali ke menu utama (Tanpa simpan) | (2) Teruskan pembayaran")
            final_chance = int(input("Masukkan digit 1 atau 2 di sini: "))
            if final_chance == 1:
                return bahasa_malaysia()
            else:
                return bayaran(kp, surat_anak, mata_pelajaran_input, raw_digit, senarai_pilihan, jumlah_dikesan, nama_calon, alamat, negeri_dan_bandar, poskod, telefon, jantina_dipilih, kaum_dipilih, agama_dipilih, pilihan_MP_input, sekolahkl, sekolahsl)
    except ValueError:
        print("Respon yang tidak sah.")

def semakan_status():
    print("--- SEMAKAN STATUS CALON ---")
    kp_semak = input("Sila masukkan nombor kad pengenalan: ")

    try:
        with open("pendaftaran_spm.json", "r") as fail:
            database = json.load(fail)

        if kp_semak in database:
            rekod = database[kp_semak]
            print(f"Nama Calon: {rekod['nama']}")
            print(f"Nombor Pengenalan Diri: {kp_semak}") 
            print(f"Jumlah Bayaran: {rekod['bayaran']}")
            print(f"Pusat peperiksaan: {rekod['pusat']}")
        else:
            print("Tiada rekod yang ditemui.")

    except FileNotFoundError:
        print("Tiada rekod yang ditemui.")

    input("Tekan Enter untuk kembali ke menu utama...")
    return bahasa_malaysia()

spm_registeration()

                