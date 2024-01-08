from SaveLoadManager import saveloadsystem


saveloadmanager = saveloadsystem(".save","save_data")


entities = saveloadmanager.load_game_data(["entities"],[[]])

#onder quit
saveloadmanager.save_game_data([entities],["entities"])

