## デスクトップアプリからCLI版Claude Codeへの移行

**決定日**: 2026-06-20

**理由**: 
デスクトップアプリはディレクトリ変更が複雑で、ユーザーがGドライブのマウント問題に直面した。CLI版ならPowerShellから直接パスを指定できるため。

**内容**: 
Claude CodeはCLI版 `claude.exe` を使用して起動する。

実行方法：
```powershell
claude "G:\マイドライブ\Claude\セッション"
```

デ
