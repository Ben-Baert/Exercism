Hamming = {}

function Hamming.compute(str1, str2)
  local distance = 0
  for i=0, str1:len() do
    if str1:sub(i,i) ~= str2:sub(i,i) then
      distance = distance + 1
    end
  end
  return distance
end

return Hamming