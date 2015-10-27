
button = {}

-- 设置按钮
function button_spawn(x, y, text, id)
    table.insert(button, {x = x, y = y, text = text, id = id})
end


-- 画按钮
function button_draw()
    for i,v in ipairs(button) do 
        love.graphics.setColor(0, 0, 0)
        love.graphics.setFont(medium)
        love.graphics.print(v.text, v.x, v.y)
    end
end 


-- 按钮按下
function button_click(x,y)
    for i,v in ipairs(button) do 
        if x > v.x 
        and x < v.x + medium:getWidth(v.text) 
        and y > v.y 
        and y < v.y + medium:getHeight() then
            if v.id == 'quit' then
                love.event.push('quit')
            end
            if v.id == 'start' then
                gameState = 'playing'
            end
        end
    end 
end 




