Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Mirage III Jet')
m.hexdigest()
'4a7d98e720b85de3643bbdd71d71617f63d37564280d4124604af056e05a1ffb'
