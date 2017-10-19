# -*- mode: python -*-

block_cipher = None


a = Analysis(['App.py'],
             pathex=['C:\\Users\\Dennic\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\Dennic\\Desktop\\PyQtÑ§Ï°\\´®¿ÚÖúÊÖ'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='App',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico')
