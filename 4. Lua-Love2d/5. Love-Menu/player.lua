
player = {}     -- 这是一个table
player.x = 10
player.y = 10
player.speed = 200
player.health = 100
player.damage = 2
player.pic = love.graphics.newImage('snowwhite.png')



function player_draw()
    love.graphics.setColor(255, 255, 255)
    love.graphics.draw(player.pic, player.x, player.y)
end


function player_move(dt)

    -- 处理上下左右
    if love.keyboard.isDown('up') then
        player.y = player.y - player.speed * dt 
    elseif love.keyboard.isDown('down') then
        player.y = player.y + player.speed * dt 
    elseif love.keyboard.isDown('left') then
        player.x = player.x - player.speed * dt 
    elseif love.keyboard.isDown('right') then
        player.x = player.x + player.speed * dt 
    end

end







