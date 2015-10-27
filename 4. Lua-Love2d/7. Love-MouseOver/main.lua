

require ("player")
require ("map")
require ("menu")



function love.load()
    gameState = 'menu'  -- 游戏状态

    medium = love.graphics.newFont(45)
    love.graphics.setBackgroundColor(255, 255, 255) -- 窗口背景颜色

    -- 设置按钮(还没画)
    button_add(5, 200, "Start", 'start')
    button_add(5, 300, "Quit", 'quit')

end





-- 逻辑更新
-- dt = delta time
function love.update(dt)


    if gameState == 'playing' then
        player_move(dt) -- 玩家的更新逻辑
        map_collide() -- 检测人物是否到了窗口边缘
    end 

    if gameState == 'menu' then
        mousex = love.mouse.getX()
        mousey = love.mouse.getY()
        button_mouseover(mousex, mousey) 
        -- button_mouseover 检测鼠标是否悬浮在某按钮上, 
        -- 如果是, 设置按钮的mouseover属性为true, 否则为false
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

