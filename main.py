import decode
import encode
import spoil

encode.run()
spoil.run()
decode.run()

print(f"Кол-во внесенных ошибок {spoil.error_count}")
print(f"Кол-во итоговых ошибок: {spoil.compare()}")
