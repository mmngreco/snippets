local bufnr = 17

vim.api.nvim_create_autocmd("BufWritePost", {
  group = vim.api.nvim_create_augroup("MakeMG", { clear = true }),
  pattern = "schema.sql",
  callback = function()
    vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, {})
    vim.fn.jobstart({"make", "run"}, {
      stdout_buffered = false,
      on_stdout = function(_, data, _)
        if data then
          vim.api.nvim_buf_set_lines(bufnr, -1, -1, false, data)
        end
      end,
      on_stderr = function(_, data, _)
        if data then
          vim.api.nvim_buf_set_lines(bufnr, -1, -1, false, data)
        end
      end,
    })
  end
})
