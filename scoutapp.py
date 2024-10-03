import tkinter as tk
from tkinter import ttk, messagebox
import statbotics  # Takım bilgilerini almak için
import webbrowser

"""
WoxicDEV - 2024 
Scout App - 2024
Instagram - mertt.js_
LinkedIn : Mert Ali Kaya
chiefdelphi : mrtalikyaa
medium : mrtalikyaa
////////////////////////////////////
Tasarımdan yana çok sıkıntı yaşadım bu sebepten sadece işlevsel olacak şekidle bıraktım.
Ekran büyüme küçülme ayarını sildim.
Değişken adlarını porgramlarda ingilizce yapmıyorum yurtdışında da 
kullanım olur diye ülkemizde de kullanılmıyorlarmış :D
"""

def open_link(url):
    webbrowser.open(url)

# Uygulama penceresi
root = tk.Tk()
root.title("FRC 2024 Crescendo Scout App -  Mert Ali Kaya")
root.geometry("700x700")

# Tab Kontrol
tab_control = ttk.Notebook(root)

# Tab 1: Bilgi Girme Kısmı
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Maç Bilgileri")

# Tab 2: Kayıtlı Maçlar
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Kayıtlı Maçlar")

# Tab 3: Takım Sorgulama
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Takım Sorgulama")

# Tab 4: Kaynak Yardım Bölümü
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text="FRC Kaynak")


("""##Tab 5: Ben
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text="Yapan Hakkında")
####""")

tab_control.pack(expand=1, fill="both")

# --- Tab 1 içeriği Bölümü---

# Takım Numarası Girişi
team_number_label = tk.Label(tab1, text="Takım Numarası:")
team_number_label.grid(row=0, column=0, padx=10, pady=10)

team_number_entry = tk.Entry(tab1)
team_number_entry.grid(row=0, column=1, padx=10, pady=10)

# Otonom ve Oyun İçi Bölüm
auton_frame = tk.LabelFrame(tab1, text="Otonom Zamanı", padx=10, pady=10)
auton_frame.grid(row=1, column=0, padx=20, pady=20)

teleop_frame = tk.LabelFrame(tab1, text="Oyun İçi Zaman", padx=10, pady=10)
teleop_frame.grid(row=1, column=1, padx=20, pady=20)

# Otonom modda nota atma sayacı
auton_count = tk.IntVar()
auton_count.set(0)

def increment_auton():
    auton_count.set(auton_count.get() + 1)

def decrement_auton():
    if auton_count.get() > 0:
        auton_count.set(auton_count.get() - 1)

auton_label = tk.Label(auton_frame, text="Kaç Nota Attı:")
auton_label.grid(row=0, column=0, padx=10, pady=10)

auton_counter = tk.Label(auton_frame, textvariable=auton_count, font=("Helvetica", 14))
auton_counter.grid(row=0, column=1, padx=10, pady=10)

auton_increment_button = tk.Button(auton_frame, text="+", command=increment_auton)
auton_increment_button.grid(row=0, column=2, padx=10, pady=10)

auton_decrement_button = tk.Button(auton_frame, text="-", command=decrement_auton)
auton_decrement_button.grid(row=0, column=3, padx=10, pady=10)

# Otonom modda notlar
auton_notes_label = tk.Label(auton_frame, text="Notlar:")
auton_notes_label.grid(row=1, column=0, padx=10, pady=10)

auton_notes = tk.Text(auton_frame, height=5, width=30)
auton_notes.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Oyun içi modda nota atma sayacı (bozulmaması için dokunmanızı önermem)
teleop_count = tk.IntVar()
teleop_count.set(0)

def increment_teleop():
    teleop_count.set(teleop_count.get() + 1)

def decrement_teleop():
    if teleop_count.get() > 0:
        teleop_count.set(teleop_count.get() - 1)

teleop_label = tk.Label(teleop_frame, text="Kaç Nota Attı:")
teleop_label.grid(row=0, column=0, padx=10, pady=10)

teleop_counter = tk.Label(teleop_frame, textvariable=teleop_count, font=("Helvetica", 14))
teleop_counter.grid(row=0, column=1, padx=10, pady=10)

teleop_increment_button = tk.Button(teleop_frame, text="+", command=increment_teleop)
teleop_increment_button.grid(row=0, column=2, padx=10, pady=10)

teleop_decrement_button = tk.Button(teleop_frame, text="-", command=decrement_teleop)
teleop_decrement_button.grid(row=0, column=3, padx=10, pady=10)

# Oyun içinde notlar
teleop_notes_label = tk.Label(teleop_frame, text="Notlar:")
teleop_notes_label.grid(row=1, column=0, padx=10, pady=10)

teleop_notes = tk.Text(teleop_frame, height=5, width=30)
teleop_notes.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Tırmanma kısmı
climb_label = tk.Label(tab1, text="Tırmanma Yaptı mı?")
climb_label.grid(row=3, column=0, padx=10, pady=10)

climb_var = tk.BooleanVar()

climb_checkbox = tk.Checkbutton(tab1, text="Evet", variable=climb_var)
climb_checkbox.grid(row=3, column=1, padx=10, pady=10)

# Eğer tırmanma yaptıysa ek not girilecektir
climb_notes_label = tk.Label(tab1, text="Tırmanma Notları:")
climb_notes_label.grid(row=4, column=0, padx=10, pady=10)

climb_notes = tk.Text(tab1, height=3, width=40)
climb_notes.grid(row=4, column=1, padx=10, pady=10)

# Kaydetme 
matches = []

def save_match():
    team_number = team_number_entry.get()
    auton_score = auton_count.get()
    teleop_score = teleop_count.get()
    auton_note = auton_notes.get("1.0", tk.END).strip()
    teleop_note = teleop_notes.get("1.0", tk.END).strip()
    climb_done = "Evet" if climb_var.get() else "Hayır"
    climb_note = climb_notes.get("1.0", tk.END).strip()

    match_data = {
        "Takım No": team_number,
        "Otonom Nota": auton_score,
        "Teleop Nota": teleop_score,
        "Otonom Notlar": auton_note,
        "Teleop Notlar": teleop_note,
        "Tırmanma": climb_done,
        "Tırmanma Notlar": climb_note
    }

    matches.append(match_data)
    messagebox.showinfo("Kaydedildi - :D", "Maç başarıyla kaydedildi!")
    update_table()

# Kaydet butonu
save_button = tk.Button(tab1, text="Kaydet", command=save_match, bg="#4CAF50", fg="white", width=15)
save_button.grid(row=5, column=1, padx=10, pady=20)

# --- Tab 2 içeriği ---
columns = ("Takım No", "Otonom Nota", "Teleop Nota", "Otonom Notlar", "Teleop Notlar", "Tırmanma", "Tırmanma Notlar")

match_table = ttk.Treeview(tab2, columns=columns, show="headings")
match_table.pack(fill="both", expand=True)

for col in columns:
    match_table.heading(col, text=col)

# Kayıtlı maçları tabloya ekleme fonksiyonu (Özelleştirmeye gerek yok bu bölümde)
def update_table():
    for row in match_table.get_children():
        match_table.delete(row)

    for match in matches:
        match_table.insert("", "end", values=(match["Takım No"], match["Otonom Nota"], match["Teleop Nota"], 
                                              match["Otonom Notlar"], match["Teleop Notlar"], match["Tırmanma"], 
                                              match["Tırmanma Notlar"]))

# --- Tab 3 içeriği (Team Search Programımdan aldım aynı işlevde sadece bir arada) ---
def get_team_info():
    try:
        team_number = int(team_number_sorgu_entry.get())
        team_info = sb.get_team(team_number)

        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)

        for key, value in team_info.items():
            text_box.insert(tk.END, f"{key.capitalize()}: {value}\n")

        text_box.config(state=tk.DISABLED)
    except ValueError:
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, "Geçerli bir takım numarası girmediniz.")
        text_box.config(state=tk.DISABLED)

# Scout bilgilerini almak için statbotics kısmı
sb = statbotics.Statbotics()

# Takım Sorgulama alanı
team_number_sorgu_label = tk.Label(tab3, text="Takım Numarası:")
team_number_sorgu_label.pack(pady=5)

team_number_sorgu_entry = tk.Entry(tab3)
team_number_sorgu_entry.pack(pady=5)

sorgula_button = tk.Button(tab3, text="Sorgula", command=get_team_info, bg="#2196F3", fg="white", width=15)
sorgula_button.pack(pady=10)

# Takım bilgilerini göstermek için metin kutusu
text_box = tk.Text(tab3, height=15, width=50, state=tk.DISABLED)
text_box.pack(pady=5)

# --- Tab 4 içeriği (Kaynak Bölümü) ---

# Kaynaklar (Başka bir FRC Takımından alıntıdır tek tek kendim eklemedim olanları direk koydum)
resources = [
    ("Temel Kaynaklar", [
        ("FIRST Robotics Competition Control System", "https://docs.wpilib.org/en/stable/"),
        ("WPILib API - Java Docs", "https://first.wpi.edu/FRC/roborio/release/docs/java/"),
        ("FRC Java Temelleri - FRCTURKEY", "https://learn.frcturkey.org/frc-yazilim/frc-java-temelleri/frc-java-temelleri"),
        ("Chiefdelphi - FRC Java Programming", "https://www.chiefdelphi.com/c/technical/java/75")
    ]),
    ("Ek Kaynaklar", [
        ("2019-2020 Team 254 FRC Programming Workshop Series by Sumi Govindaraju '20", "https://drive.google.com/drive/folders/1tZ6xdn-xzFpcAzW3VB5ttzQwuhUmvPJB"),
        ("Taking Control of Your Robot with Jared", "https://www.team254.com/documents/control/"),
        ("Integrating Computer Vision with Motion Control", "https://www.team254.com/documents/vision-control/"),
        ("FRC Team 5190 | Zero to Trajectory Tracking using FRC 2020 Software", "https://www.youtube.com/watch?v=wqJ4tY0u6IQ&list=PLeYvtE4N1NcSsFUAQI-NpFqF8KVduA_e8"),
        ("FRC Java Programming Tutorial - 1 - Installations", "https://www.youtube.com/watch?v=I7LOtI0qAl0&list=PL3BTo6bVJQFf9nCWAneScIK2OHNVVY9bq"),
        ("2015 FIRST World Championships Conference - Motion Planning & Control in FRC", "https://www.youtube.com/watch?v=8319J1BEHwM"),
        ("Git Cheat-Sheet - GitHub", "https://gist.github.com/davfre/8313299")
    ]),
    ("Örnek Robot Kodları", [
        ("FRC Team 9436 PointrGiro · GitHub", "https://github.com/PointrGiro"),
        ("FRC Team 254 Cheesy Poofs · GitHub", "https://github.com/Team254"),
        ("FRC Team 330 Beachbot · Github", "https://github.com/Beachbot330"),
        ("FRC Team 148 Robowranglers · Github", "https://github.com/team148"),
        ("FRC Team 1678: Citrus Circuits · GitHub", "https://github.com/frc1678"),
        ("FRC 5190: Green Hope Falcons · GitHub", "https://github.com/FRC5190")
    ])
]

# Kaynakları ekleyen fonksiyon
def create_resources(tab, resources):
    for section, links in resources:
        section_label = tk.Label(tab, text=section)
        section_label.pack(pady=10)

        for name, url in links:
            link_button = tk.Button(tab, text=name, fg="blue", command=lambda url=url: open_link(url))
            link_button.pack()

# Kaynakları ekleme alanı
create_resources(tab4, resources)


root.mainloop()
