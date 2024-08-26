run = True
while run:
    equip = input("switch/router/server? \n")
    if equip == "switch" or equip == "router":
        import sr_main
        run = False
    elif equip == "server":
        import server_main
        run = False