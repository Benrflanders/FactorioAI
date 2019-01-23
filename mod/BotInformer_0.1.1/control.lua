require "util"

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