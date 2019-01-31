require "util"

scripts.on_nth_tick(4, function(event)
    game.take_screenshot()

end)

script.on_event(defines.events.on_player_mined_entity, function(event)
    --check if mined entity is copper
    --if event.entity == 

    ---local player_index = event.player_index
    ---local player = game.players[player_index]
    game.print("An entity was mined")
    game.print(event.entity.name)
end)

script.on_event(defines.events.on_player_mined_item, function(event)
    game.print(event.item_stack.name)
    local item_name = event.item_stack.name

    if item_name == "copper-ore" then
        game.print("A Copper Ore was mined. Adding to curr_sess.txt")
        --write to a file that an ore was mined
        game.write_file("curr_sess.txt", "copper-ore\n", true)
    end

end)

script.on_event(defines.events.on_gui_closed, function(event)

    --delete out the current session on game close/end
    game.write_file("curr_sess.txt", "", false)
end)

script.on_event(defines.events.on_gui_opened, function(event)

    --delete out the current session on game close/end
    game.write_file("curr_sess.txt", "", false)
end)

--if player changes position, check what type of surface they are on
script.on_event(defines.events.on_player_changed_position, function(event)
    --get player index
    local player_index = event.player_index
    local player_coords = game.players[player_index].position

    --get the name of the surface the player is standing on
    local tile_name = game.players[player_index].surface.get_tile_properties(player_coords)
    game.print(tile_name)
    --check if the tile name is a resource tile
    game.write_file("curr_sess.txt", "player-moved\n", true)


end)