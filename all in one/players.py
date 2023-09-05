team_gs = []
team_fb = []
team_bjk = []


def teams(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    oyuncu = liste[0] + "\n"
    takim = liste[1]
    if takim == "Galatasaray":
        team_gs.append(oyuncu)
    elif takim == "Beşiktaş":
        team_bjk.append(oyuncu)
    elif takim == "Fenerbahçe":
        team_fb.append(oyuncu)


with open("players.txt", "r", encoding="utf-8") as file:
    for i in file:
        teams(i)
with open("team_galatasaray.txt", "w+", encoding="utf-8") as gs_file:
    for i in team_gs:
        gs_file.write(i)
with open("team_fenerbahce.txt", "w+", encoding="utf-8") as fb_file:
    for i in team_fb:
        fb_file.write(i)
with open("team_besiktas.txt", "w+", encoding="utf-8") as bjk_file:
    for i in team_bjk:
        bjk_file.write(i)
