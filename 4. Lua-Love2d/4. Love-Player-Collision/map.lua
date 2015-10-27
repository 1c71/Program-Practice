

-- collide 碰撞
-- 函数负责检测人物与窗口的碰撞 然后处理它
function map_collide()

    -- 最左
    if player.x < 0 then
        player.x = 0
    end

    -- 最上
    if player.y < 0 then
        player.y = 0
    end

    -- 拿到窗口的宽和高
    screen_width = love.graphics.getWidth()
    screen_height = love.graphics.getHeight()


    -- 最下
    if player.y + player.pic:getHeight() > screen_height then
        player.y = screen_height - player.pic:getHeight()
    end

    -- 最右
    if player.x + player.pic:getWidth() > screen_width then
        player.x = screen_width - player.pic:getWidth()
    end

end

