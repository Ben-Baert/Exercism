Bob = {}

function Bob.hey (input_str)
    if input_str == '' then
        return 'Fine, be that way.'
    end
    if input_str:match('?$') then
        return 'Sure'
    end
    _, count = input_str:gsub('[A-Z!]', '')
    if count > 2 then
        return 'Whoa, chill out!'
    end
    return 'Whatever'
end

return Bob