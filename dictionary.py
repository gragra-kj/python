# friends=["Millena", "Phoebe", "Joy" ,"Gregory" ,"Veronica"]
# places=["Ruiru","Mwiki","KU","Karen","Ngong"]
#friends are the keys and the location is the value
# friends={"Millena":"Ruiru",
#          "Phoebe":"Mwiki",
#          "Joy":"KU",
#          "Gregory":"Karen",
#          "Veronica":"Ngong"}
# for friend in friends:
#     print(friend, friends[friend], sep=":")

friends=[
    {"name":"Millena","location":"Ruiru","career":"ux designer"},
    {"name":"Phoebe","location":"Mwiki","career":"Data analyst"},
    {"name":"Joy","location":"KU","career":"Accounting"},
    {"name":"Gregory","location":"Karen","career":"Chemical Engineer"},
    {"name":"Veronica","location":"Ngong","career":"HR"}
]
for friend in friends:
    print(friend["name"],friend["location"],friend["career"],sep=" :")