-- PDF: numrerade H1 får kompakt tvådelad kapitelstart; övriga H1 (t.ex. Inledning) blir onumrerade kapitel.
function Header(el)
  if el.level ~= 1 then return nil end
  local text = pandoc.utils.stringify(el.content)
  local normalized = text:gsub("–", "-")
  local part, part_title = normalized:match("^%s*Del%s+([IVX]+)%s+%-%s+(.+)%s*$")
  if part then
    local blocks = pandoc.read(part_title, "markdown").blocks
    local inlines = (#blocks > 0 and blocks[1].content) or {pandoc.Str(part_title)}
    local title_tex = pandoc.write(pandoc.Pandoc({pandoc.Para(inlines)}), "latex"):gsub("%s+$", "")
    return pandoc.RawBlock("latex", "\\bookpart{" .. part .. "}{" .. title_tex .. "}")
  end
  local number, title = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  if number then
    local blocks = pandoc.read(title, "markdown").blocks
    local inlines = (#blocks > 0 and blocks[1].content) or {pandoc.Str(title)}
    local title_tex = pandoc.write(pandoc.Pandoc({pandoc.Para(inlines)}), "latex"):gsub("%s+$", "")
    return pandoc.RawBlock("latex", "\\bookchapter{" .. number .. "}{" .. title_tex .. "}")
  end
  local escaped = pandoc.write(pandoc.Pandoc({pandoc.Para(el.content)}), "latex"):gsub("%s+$", "")
  return pandoc.RawBlock("latex", "\\bookfrontchapter{" .. escaped .. "}")
end
