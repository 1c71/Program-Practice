
require ("player")


function love.load()
end



function love.update()
    player_move() -- 玩家的更新逻辑
end




function love.draw()
    player_draw()   -- 绘制玩家
end



