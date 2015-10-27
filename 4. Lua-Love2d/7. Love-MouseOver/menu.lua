mouseover = false

button = {}


-- 设置按钮
function button_add(x, y, text, id)
    table.insert(button, {x = x, y = y, text = text, id = id, mouseover = false})
end


-- 画按钮
-- 根据按钮的mouseover属性为true或false 修改颜色
function button_draw()
    for i,v in ipairs(button) do 
        if v.mouseover == false then
            love.graphics.setColor(0, 0, 0)
        elseif v.mouseover == true then 
            love.graphics.setColor(45, 122, 33)
        end 

        love.graphics.setFont(medium)
        love.graphics.print(v.text, v.x, v.y)
    end
end 


-- 按钮按下
-- 传入xy, 循环按钮table, 根据xy判断是否有按钮被按下了, 再判断它的id来知道是哪个按钮被按下了
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



-- 
function button_mouseover(x,y)
    for i,v in ipairs(button) do 
        if x > v.x 
        and x < v.x + medium:getWidth(v.text) 
        and y > v.y 
        and y < v.y + medium:getHeight() then
            v.mouseover = true
        else 
            v.mouseover = false
        end
    end 
end




