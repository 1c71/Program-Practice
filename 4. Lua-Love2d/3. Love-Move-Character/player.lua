
player = {}     -- 这是一个table
player.x = 10
player.y = 10
player.speed = 5
player.pic = love.graphics.newImage('snowwhite.png')



function player_draw()
    love.graphics.setColor(255, 255, 255)
    love.graphics.draw(player.pic, player.x, player.y)
end


function player_move()

    -- 处理上下左右
    if love.keyboard.isDown('up') then
        player.y = player.y - player.speed
    elseif love.keyboard.isDown('down') then
        player.y = player.y + player.speed
    elseif love.keyboard.isDown('left') then
        player.x = player.x - player.speed
    elseif love.keyboard.isDown('right') then
        player.x = player.x + player.speed
    end

end








