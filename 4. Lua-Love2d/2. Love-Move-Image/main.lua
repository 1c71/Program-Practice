


function love.load()

    medium = love.graphics.newFont(45)

    pic = love.graphics.newImage('2.jpg')
    picx = 200
    picy = 200


end


function love.update()

    if love.keyboard.isDown('up') then
        picy = picy - 5
    elseif love.keyboard.isDown('down') then
        picy = picy + 5
    elseif love.keyboard.isDown('left') then
        picx = picx - 5
    elseif love.keyboard.isDown('right') then
        picx = picx + 5
    end

    
end





function love.draw()
    love.graphics.draw(pic, picx, picy)
end



