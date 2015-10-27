
require ("player")
require ("map")


function love.load()
    love.graphics.setBackgroundColor(255, 255, 255)
end


-- 逻辑更新
function love.update()
    player_move() -- 玩家的更新逻辑
    map_collide() -- 检测人物是否到了窗口边缘
end



-- 图像绘制
function love.draw()
    player_draw()   -- 绘制玩家
end



