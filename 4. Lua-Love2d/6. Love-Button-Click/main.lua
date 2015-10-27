
require ("player")
require ("map")
require ("menu")


function love.load()

    medium = love.graphics.newFont(45)

    gameState = 'menu'  -- 游戏状态

    love.graphics.setBackgroundColor(255, 255, 255)

    -- 设置按钮
    button_spawn(5, 200, "Start", 'start')
    button_spawn(5, 300, "Quit", 'quit')

end





-- 逻辑更新
-- dt = delta time
function love.update(dt)

    if gameState == 'playing' then
        player_move(dt) -- 玩家的更新逻辑
        map_collide() -- 检测人物是否到了窗口边缘
    end 

end



-- 图像绘制
function love.draw()

    if gameState == 'menu' then
        button_draw()   -- 画按钮
    end
    

    if gameState == 'playing' then
        player_draw()   -- 绘制玩家
    end

end





function love.mousepressed(x, y, type)
    if gameState == 'menu' then
        button_click(x,y)
    end

end 

