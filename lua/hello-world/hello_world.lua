local HelloWorld = {}

function HelloWorld.hello(name)
  name = name or "world"
  return "Hello, " .. name .. "!"
  end

return HelloWorld