

function love.load()
    normal_cursor = love.graphics.newImage("normal-cursor.png")
    clicked_cursor = love.graphics.newImage("clicked-cursor.png")
    -- 载入两张图片

    now_cursor = normal_cursor  -- 设置默认鼠标

    love.mouse.setVisible(false)  -- 设置鼠标不可见
    love.mouse.setGrab(true)   -- 捕获鼠标
end




function love.draw()
    
    love.graphics.draw(now_cursor, 
        love.mouse.getX() - now_cursor:getWidth() / 2, 
        love.mouse.getY() - now_cursor:getHeight() / 2)

end




function love.update(dt)

end




function love.mousepressed(x, y, button)
    now_cursor = clicked_cursor
end


function love.mousereleased(x, y, button)
    now_cursor = normal_cursor
end




-- 按ESC退出
function love.keypressed(key)   -- we do not need the unicode, so we can leave it out
   if key == "escape" then
      love.event.push("quit")   -- actually causes the app to quit
   end
end

